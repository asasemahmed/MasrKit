# Skill authoring guide

Start with real agent decisions, not a broad topic. The description must explain when the skill applies and distinguish it from adjacent skills. Keep the entrypoint focused on purpose, routing, workflow, non-obvious constraints, anti-patterns, and a completion checklist. Move genuinely conditional detail into a linked reference; do not split content merely to create folders.

Every recommendation should make the action, context, reason, and common failure apparent. Prefer examples that clarify a decision boundary. Avoid generic engineering advice, unverifiable market claims, stereotypes, permanent copies of changing regulations, and rules based on one product's behavior.

New skills must include the required metadata from [`schemas/skill.schema.json`](../schemas/skill.schema.json) and the sections `Purpose`, `Use this skill when`, `Workflow`, and `Quality checklist`. Use lowercase hyphenated IDs and avoid overlap with existing skills.

Before opening a pull request, run all commands in the root README and exercise at least one realistic prompt. Content changes should explain their evidence and which failure they prevent.
