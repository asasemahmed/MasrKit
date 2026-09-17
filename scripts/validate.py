#!/usr/bin/env python3
"""Validate MasrKit skill metadata, structure, and local Markdown links."""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = {"name", "description", "metadata"}
REQUIRED_METADATA = {"version", "category", "locale", "tags"}
SECTIONS = {"Purpose", "Use this skill when", "Workflow", "Quality checklist"}
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
VERSION_RE = re.compile(r"^\d+\.\d+\.\d+$")
LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")


def parse_scalar(value: str):
    value = value.strip()
    if value.startswith("[") and value.endswith("]"):
        return [part.strip().strip("'\"") for part in value[1:-1].split(",") if part.strip()]
    return value.strip("'\"")


def parse_frontmatter(path: Path) -> tuple[dict, str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError("missing YAML frontmatter")
    try:
        raw, body = text[4:].split("\n---\n", 1)
    except ValueError as exc:
        raise ValueError("unclosed YAML frontmatter") from exc
    data = {}
    section = None
    for line in raw.splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            raise ValueError(f"invalid frontmatter line: {line}")
        key, value = line.split(":", 1)
        key = key.strip()
        if line.startswith("  ") and section:
            data[section][key] = parse_scalar(value)
        elif not value.strip():
            data[key] = {}
            section = key
        else:
            data[key] = parse_scalar(value)
            section = None
    return data, body


def validate_skill(path: Path, names: set[str]) -> list[str]:
    errors = []
    try:
        metadata, body = parse_frontmatter(path)
    except ValueError as exc:
        return [f"{path.relative_to(ROOT)}: {exc}"]
    missing = REQUIRED - metadata.keys()
    if missing:
        errors.append(f"{path.relative_to(ROOT)}: missing metadata: {', '.join(sorted(missing))}")
    name = metadata.get("name", "")
    if name != path.parent.name:
        errors.append(f"{path.relative_to(ROOT)}: name must match directory")
    if not NAME_RE.fullmatch(str(name)):
        errors.append(f"{path.relative_to(ROOT)}: invalid skill name")
    if name in names:
        errors.append(f"{path.relative_to(ROOT)}: duplicate skill name {name}")
    names.add(str(name))
    extension = metadata.get("metadata", {})
    if not isinstance(extension, dict):
        errors.append(f"{path.relative_to(ROOT)}: metadata must be an object")
        extension = {}
    missing_extension = REQUIRED_METADATA - extension.keys()
    if missing_extension:
        errors.append(f"{path.relative_to(ROOT)}: missing metadata fields: {', '.join(sorted(missing_extension))}")
    if not VERSION_RE.fullmatch(str(extension.get("version", ""))):
        errors.append(f"{path.relative_to(ROOT)}: version must be SemVer")
    if len(str(metadata.get("description", ""))) < 30:
        errors.append(f"{path.relative_to(ROOT)}: description is too short")
    tags = extension.get("tags", [])
    if not isinstance(tags, list) or len(tags) < 2:
        errors.append(f"{path.relative_to(ROOT)}: tags must be an inline list with at least two values")
    headings = set(re.findall(r"^## (.+?)\s*$", body, re.MULTILINE))
    for section in sorted(SECTIONS - headings):
        errors.append(f"{path.relative_to(ROOT)}: missing required section '{section}'")
    if any(token in body for token in ("TODO", "TBD", "PLACEHOLDER")):
        errors.append(f"{path.relative_to(ROOT)}: unfinished placeholder found")
    return errors


def validate_links() -> list[str]:
    errors = []
    for path in ROOT.rglob("*.md"):
        if any(part in {".git", ".venv"} for part in path.parts):
            continue
        text = path.read_text(encoding="utf-8")
        for target in LINK_RE.findall(text):
            clean = target.split("#", 1)[0]
            if not clean or clean.startswith(("http://", "https://", "mailto:")):
                continue
            if not (path.parent / clean).resolve().exists():
                errors.append(f"{path.relative_to(ROOT)}: broken link: {target}")
    return errors


def validate_examples(valid_names: set[str]) -> list[str]:
    errors = []
    manifest = ROOT / "examples" / "manifest.json"
    try:
        data = json.loads(manifest.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return [f"examples/manifest.json: {exc}"]
    for item in data.get("examples", []):
        unknown = set(item.get("skills", [])) - valid_names
        if unknown:
            errors.append(f"examples/manifest.json: {item.get('file')} uses unknown skills {sorted(unknown)}")
        if not (ROOT / "examples" / item.get("file", "")).is_file():
            errors.append(f"examples/manifest.json: missing file {item.get('file')}")
    return errors


def run() -> list[str]:
    errors: list[str] = []
    names: set[str] = set()
    skill_files = sorted((ROOT / "skills").glob("*/SKILL.md"))
    if not skill_files:
        return ["No skills found"]
    for path in skill_files:
        errors.extend(validate_skill(path, names))
    errors.extend(validate_examples(names))
    errors.extend(validate_links())
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args()
    errors = run()
    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Validation passed: skill metadata, structure, examples, and links are valid.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
