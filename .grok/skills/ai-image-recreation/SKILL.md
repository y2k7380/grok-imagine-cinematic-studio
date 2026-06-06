---
name: ai-image-recreation
description: Recreate, enhance, restyle, or transfer visual style from reference images while preserving key identity and composition.
---

# AI Image Recreation

Use this skill when the user wants a new or edited image based on one or more references.

## Workflow
1. Inspect the supplied reference image paths or generated image ids.
2. If a person or recurring character is involved, activate `character-dna-extractor` first and reuse the extracted identity language.
3. For direct edits, use `image_edit` with the source image. If only `edit_image` is exposed, use that alias.
4. For a clean recreation from scratch, use `image_gen` with the reference-derived prompt. If only `generate_image` is exposed, use that alias.
5. Save outputs under `artifacts/<project>/refs/` or `artifacts/<project>/keyframes/`.
6. Record the source image, prompt, and output path in the Project Bible when the cinematic studio is active.

## Quality Rules
- Preserve identity, pose intent, clothing, lighting direction, and composition unless the user asks to change them.
- Avoid adding text unless the user explicitly asks for text.
- For cinematic work, hand prompts through `imagine-prompt-master` and run QA before animation.
