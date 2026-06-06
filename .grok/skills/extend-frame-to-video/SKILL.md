---
name: extend-frame-to-video
description: Turn approved keyframes or final frames into short video clips while preserving continuity and motion intent.
---

# Extend Frame To Video

Use this skill when animating a still image, continuing from a prior clip, or extending a sequence.

## Workflow
1. Confirm the keyframe image is approved by QA.
2. If continuing a prior clip, load `last_frame_recap` and the extracted end-frame PNG.
3. Craft a short motion prompt through `imagine-prompt-master`.
4. Call `image_to_video(image=keyframe_path, prompt=motion_prompt, duration=6 or 10, resolution_name="720p")`.
5. Extract the last frame with ffmpeg for the next continuation when continuity matters.
6. Save clips under `artifacts/<project>/clips/` and update the Project Bible.

## Rules
- Never animate without an approved keyframe.
- Use one primary action and one camera move per clip.
- Prefer 6 seconds for action and 10 seconds for narration-heavy or emotional beats.
- Use `cinematic-sequence-extender` for 60 second or longer sequences.
