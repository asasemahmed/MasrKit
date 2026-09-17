#!/usr/bin/env python3
"""Install canonical MasrKit skills without destructive overwrites."""
from __future__ import annotations

import argparse
import os
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
TARGETS = {
    "codex": Path(os.environ.get("CODEX_HOME", Path.home() / ".codex")) / "skills",
    "claude": Path.home() / ".claude" / "skills",
    "cursor": Path.home() / ".cursor" / "skills",
    "gemini": Path.home() / ".gemini" / "skills",
}


def available() -> list[str]:
    return sorted(path.name for path in SKILLS.iterdir() if (path / "SKILL.md").is_file())


def install(names: list[str], destination: Path, dry_run: bool = False) -> list[str]:
    messages = []
    for name in names:
        source = SKILLS / name
        target = destination / name
        if not (source / "SKILL.md").is_file():
            raise ValueError(f"Unknown skill: {name}")
        if target.exists():
            raise FileExistsError(f"Refusing to overwrite existing path: {target}")
        messages.append(f"{'Would install' if dry_run else 'Installed'} {name} -> {target}")
        if not dry_run:
            destination.mkdir(parents=True, exist_ok=True)
            shutil.copytree(source, target)
    return messages


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    selection = parser.add_mutually_exclusive_group(required=True)
    selection.add_argument("--all", action="store_true", help="Install all skills")
    selection.add_argument("--skill", action="append", help="Install one skill; repeatable")
    destination = parser.add_mutually_exclusive_group(required=True)
    destination.add_argument("--target", choices=sorted(TARGETS), help="Known agent environment")
    destination.add_argument("--dest", type=Path, help="Custom skills directory")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args(argv)
    names = available() if args.all else args.skill
    dest = args.dest.expanduser().resolve() if args.dest else TARGETS[args.target].expanduser().resolve()
    try:
        for message in install(names, dest, args.dry_run):
            print(message)
    except (ValueError, FileExistsError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
