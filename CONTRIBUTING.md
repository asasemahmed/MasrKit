# Contributing to MasrKit

Thank you for helping products work better for people in Egypt. By participating, follow the [Code of Conduct](CODE_OF_CONDUCT.md).

## Before proposing a change

- Search existing skills and issues for the decision you want to improve.
- Explain the observed failure, affected audience/context, and evidence. Do not turn one preference into a universal Egyptian rule.
- For regulations, provider capabilities, numbering, time zones, or other changing facts, link a current official source and record when it was checked.
- Use the new-skill issue form for a new domain. Prefer improving an existing skill when scopes overlap.

## Content standards

- Separate universal UX, Arabic-wide behavior, and Egypt-specific guidance.
- Do not stereotype, fabricate statistics, or imply all Egyptian users behave alike.
- Write direct instructions with decision criteria, failure modes, and useful examples.
- Keep agent entrypoints focused; put conditional depth in linked references.
- Keep canonical content vendor-neutral. Add adapters rather than copied skill trees.
- Arabic examples must be natural and reviewed in context; slang is never a substitute for localization.

## Development

Use Python 3.9+ or Node.js 18+. There are no third-party runtime dependencies.

```bash
python scripts/validate.py
python scripts/install.py --all --dest ./dist/test-skills --dry-run
npx --yes . --all --dest ./dist/test-skills --dry-run
```

When changing the installer, verify overwrite refusal, dry-run behavior, single-skill installation, and all-skill installation in a temporary destination. For substantive skill changes, exercise a realistic request and summarize the observed improvement in the pull request.

## Pull requests

Keep changes scoped. Complete the pull request template, update the changelog for user-visible changes, and avoid generated or installed skill copies. Maintainers may ask for domain, language, accessibility, security, or legal review depending on the claim.

Contributions are submitted under the repository's [MIT License](LICENSE).
