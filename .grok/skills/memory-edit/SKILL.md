---
name: memory-edit
description: Record, update, or remove user preferences and durable project facts only when the user explicitly asks.
---

# Memory Edit

Use this skill only when the user explicitly asks to remember, update, or forget something durable.

## Rules
- Do not store sensitive personal data, secrets, credentials, or one-off task details.
- Confirm the exact memory change in the final response.
- If the runtime has a memory tool, use it.
- If no memory tool exists, write a short note under `artifacts/memory_notes/` for later manual import.

## Good Candidates
- Stable workflow preferences.
- Durable project conventions.
- Reusable character, brand, or production facts the user asks to keep.
