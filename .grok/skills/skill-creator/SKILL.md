---
name: skill-creator
description: Create, update, and validate Grok skills in this workspace using strict frontmatter and lean agent instructions.
---

# Skill Creator

Use this skill when creating, updating, or validating any skill under `/home/workdir/.grok/skills/`.

## Required Structure
- Create one directory per skill under `/home/workdir/.grok/skills/`.
- The directory name must be kebab-case and must match the `name` field exactly.
- Every skill must contain `SKILL.md`.
- Optional folders are `scripts/`, `references/`, and `assets/`.
- Do not create `README.md`, `CHANGELOG.md`, or user-facing documentation inside skill directories.

## Frontmatter Rules
Every `SKILL.md` must start with:

```yaml
---
name: skill-name
description: Single-line plain text describing when to use this skill.
---
```

The description must be one line, under 1024 characters, and must not contain colons or angle brackets.

## Writing Rules
- Keep `SKILL.md` under roughly 500 lines.
- Put long role cards, examples, templates, and production bibles in `references/`.
- Prefer imperative workflow instructions over persona-heavy prose.
- When a skill wraps another workflow, state the exact tool names and fallback aliases.
- Save generated outputs under `/home/workdir/artifacts/`.

## Validation
After creating or editing a skill, run:

```bash
bash /home/workdir/.grok/skills/skill-creator/scripts/validate-skill.sh /home/workdir/.grok/skills/skill-name
```

Fix all validation errors before using the skill in production.
