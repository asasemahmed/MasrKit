# Changelog

All notable changes to MasrKit are documented here. The project follows [Semantic Versioning](https://semver.org/) for repository releases; each skill also declares its content version.

## [Unreleased]

### Added

- skills.sh listing: badge, repository page link, `npx skills add asasemahmed/masrkit` as the recommended install, and `skills.sh.json` groupings.
- Dated Egypt reference facts in `egyptian-product-ux` and a data-focused version in `egyptian-backend`: phone formats, national ID, addresses, EGP display, digits, Africa/Cairo DST, weekend, payment methods, and channels.
- Form-of-address policy for gendered Egyptian Arabic in `egyptian-copy`.
- Eval cases for every skill in `evals/`, checked by the validator.
- `humanizer` skill for natural rewriting, punctuation cleanup, and meaning preservation.
- `egyptian-session-report` skill for Egyptian Arabic session summaries delivered as self-contained RTL HTML reports.
- Premium light-mode hero artwork with a cartouche emblem, used by both README files.
- Dependency-free npm and npx installer alongside the existing Python workflow.
- Egyptian flag hero artwork and expanded README installation guidance.

### Changed

- All skills bumped to 1.1.0. Descriptions now say when to load each skill, with the keywords users type.
- Overlapping topics (phone and OTP, payments, uploads, mixed-direction values) have one owner skill; generic security boilerplate and repeated verification hedges were trimmed.
- `egyptian-session-report` saves reports outside the repository by default and only requires a browser check when a browser tool exists.
- Em dashes removed from skill prose and Arabic examples.

## [0.1.0] - 2026-09-17

### Added

- Initial six skills for Arabic UI, RTL engineering, Egyptian copy, product UX, web audits, and backend architecture.
- Safe cross-platform installer with dry-run and single/all-skill selection.
- Structural validation, safe installer tooling, and lightweight GitHub Actions CI.
- English and Arabic project documentation and public contribution files.
