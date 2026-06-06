---
name: character-dna-extractor
description: Extract stable character identity details from reference images for consistent Grok Imagine generations and sequences.
---

# Character DNA Extractor

Use this skill before generating or editing recurring characters.

## Authority
Use `grok-imagine-cinematic-studio/references/agents/Character_DNA_Extractor_v3.5.md` as the role-card source when deeper detail is needed.

## Workflow
1. Inspect all provided reference images.
2. Extract stable identity fields: face shape, hair, eyes, skin tone, age range, body proportions, wardrobe anchors, expression range, and unique marks.
3. Separate fixed identity from scene-specific styling.
4. Output a reusable `Character DNA Profile` with copy-ready prompt language.
5. Hand the profile to `identity-lock-specialist` and store it in the Project Bible.

## Output
Use this structure:

```markdown
## Character DNA Profile
- Character id:
- Stable face:
- Hair:
- Eyes:
- Skin:
- Body:
- Wardrobe anchors:
- Expression range:
- Negative drift rules:
- Copy-ready identity lock:
```
