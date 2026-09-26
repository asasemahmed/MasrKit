# Evals

`cases.json` holds a small set of prompts, each tied to one skill, with the behaviors a good answer should show. They answer one question: does loading the skill change what the agent does?

## Run a case

1. Start a fresh agent session **without** MasrKit installed and send the case's `prompt`. Save the answer.
2. Start a fresh session **with** the case's skill installed and send the same prompt. Save the answer.
3. Score each answer against every line in `expect`: pass or fail, with a one-line reason.

A skill earns its place when the with-skill answer passes clearly more checks than the baseline. If both answers pass the same checks, the skill is not adding anything for that case: tighten the skill or replace the case with a harder one.

An LLM can do the scoring if you give it the prompt, the answer, and the `expect` list, and ask for pass/fail per line. Spot-check its verdicts by hand.

## Add a case

- Base it on a real failure you have seen an agent make.
- Keep `expect` lines observable in the answer, not matters of taste.
- Use an `id` that is unique and a `skill` that exists in `skills/`. `python scripts/validate.py` checks both, and checks that every skill has at least one case.
