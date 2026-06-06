---
name: custom-grok-cinematic-agent
description: Draft or update specialized cinematic agent role cards and matching Grok skill adapters.
---

# Custom Grok Cinematic Agent

Use this skill when creating a new cinematic specialist, role card, or agent adapter.

## Workflow
1. Use `skill-creator` for any new `.grok/skills/<skill-name>/` directory.
2. Keep the `SKILL.md` adapter concise and put long role-card detail in `references/agents/`.
3. Follow `grok-imagine-cinematic-studio/references/agent-skill-template.md`.
4. Add activation triggers, collaborators, output format, and safety constraints.
5. Validate with `skill-creator/scripts/validate-skill.sh`.

## Integration
- New cinematic agents must state how they coordinate with Studio Director, Imagine Prompt Master, QA Guardian, and Workflow Quota Optimizer.
- If the agent affects real asset generation, include the Grok Build tool names it expects.
