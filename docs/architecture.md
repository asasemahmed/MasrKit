# Architecture

MasrKit keeps one canonical, vendor-neutral source for every skill. A skill directory contains a readable `SKILL.md` entrypoint and only the references that materially improve conditional tasks. It does not include a second README, generated vendor copies, or empty resource directories.

The metadata contract extends the widely used `name` and `description` frontmatter with project-owned fields that remain valid plain YAML. Categories make the future boundary explicit: `arabic-foundation` can be extracted or shared across country kits; `egypt-localization` stays market-specific. SemVer records content-contract changes without pretending Markdown is an executable API.

Installer targets are thin destination adapters. The Python and Node entrypoints copy the same canonical folders and deliberately refuse overwrite. If an agent later requires format transformation rather than directory placement, add a tested adapter while preserving `skills/` as source of truth.

Validation checks metadata, required operational sections, links, manifests, unique skill identifiers, and unfinished scaffold markers. Installer changes are reviewed with dry runs and temporary destinations so the public repository stays lightweight.

This is intentionally a Markdown-first repository with dependency-free Python and Node tooling. The npm package exposes the installer without duplicating or transforming canonical skill content.
