# Agent Skill Template (Standard Structure)

Use this as a lightweight reference when creating or updating individual agent SKILL.md files. The goal is consistency without duplication.

## Recommended Frontmatter
```yaml
---
name: agent-name
description: Short role + when to activate. Use third-person. List concrete trigger phrases where possible (e.g. "Activate when you need X, Y, or Z for a scene").
version: 3.5 (or date of last major update)
---
```

## Recommended Body Structure (Imperative Style)
- Short **Role** line (1 sentence, no heavy "You are the master of...").
- ## Core Mandate (1-2 paragraphs, verb-first).
- ## Key Protocols (bullet list of named protocols with brief descriptions).
- (Optional) ## Video Execution Integration or specific flow notes.
- ## Mandatory Self-Evaluation (7 Metrics) — keep the standard 7-metric table.
- ## Studio State Fields (list of fields the agent maintains).
- ## Integration Rules (who this agent works with, hard constraints).
- Short closing sentence.

## Imperative Writing Guidance
Prefer:
- "Oversee the entire production..."
- "Maintain the Project Bible by..."
- "Activate specialist agents dynamically..."
- "Design emotional curves..."

Avoid heavy second-person persona in the body. A one-line role description at the top is acceptable for quick context.

## Cross-References (Mandatory)
- Always mention: "This agent is orchestrated by the `grok-imagine-cinematic-studio` skill. See the main SKILL.md and `references/production-protocol.md` for overall flow, keyframe-first rules, audio post-processing requirements, and title/credits guidelines."
- Reference related agents (e.g. "Works closely with Identity Lock Specialist, DoP, and Continuity Guardian.").

## Versioning
Add a small note or update the frontmatter `version` field when significant lessons are incorporated (e.g. after major production fixes for drift, audio speed, text purity, or title/credits rules).

## Progressive Disclosure
Keep this file short. Move long examples, advanced patterns, or full role cards to the main `references/agents/<agent-name>.md` (the authoritative source).

This template keeps individual agent skills focused, consistent, and easy to maintain while the heavy details live in the central references.