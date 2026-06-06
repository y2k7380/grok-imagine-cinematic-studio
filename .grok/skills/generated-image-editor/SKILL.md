---
name: generated-image-editor
description: Refine generated images through targeted edits, variations, cleanup, and continuity preserving fixes.
---

# Generated Image Editor

Use this skill when the user wants to improve an existing generated image.

## Workflow
1. Identify the source image path or image id.
2. State the exact edit target in one concise prompt.
3. Use `image_edit`; if only `edit_image` is exposed, use that alias.
4. Preserve the original composition and identity unless the user asks for a bigger change.
5. Save edited outputs under `artifacts/<project>/edits/`.
6. For cinematic sequences, run QA before using the image as an `image_to_video` keyframe.

## Edit Types
- Cleanup text artifacts, faces, hands, clothing drift, props, or backgrounds.
- Restyle while preserving identity.
- Add or remove specific objects.
- Convert a still into a stronger keyframe for animation.
