---
name: extend-frame-to-video
description: Turn approved keyframes or final frames into short video clips while preserving continuity and motion intent.
---

# Extend Frame To Video

Use this skill when animating a still image, continuing from a prior clip, or extending a sequence.

## Workflow
1. Confirm the keyframe image is approved by QA.
2. If continuing a prior clip, load `last_frame_recap`, the extracted end-frame PNG, and `handoff_packets/clip_XX_to_YY.md`.
3. Craft a short motion prompt through `imagine-prompt-master`, including the required action vector, screen direction, camera velocity, emotional handoff, and audio bridge.
4. Call `image_to_video(image=keyframe_path, prompt=motion_prompt, duration=8-15, resolution_name="720p")` (Grok Imagine 1.5 supports up to 15s).
5. Extract the last frame with ffmpeg for the next continuation when continuity matters.
6. Save clips under `artifacts/<project>/clips/`, update `clip_registry.csv`, update the Project Bible, and create the next handoff packet when another clip follows.

## Rules
- Never animate without an approved keyframe.
- Never continue a sequence without the previous recap and transition contract unless the cut is explicitly marked as a new scene or deliberate discontinuity.
- Use one primary action and one camera move per clip.
- With Grok Imagine 1.5 supporting up to 15 seconds: Prefer 6-8 seconds for fast action, 10-12s for most emotional/narration beats, and up to 15s for slow, dense narration or complex continuous cinematic motion. Longer clips reduce the number of cuts and allow better slow pacing.
- If the result fails, classify the failure before retrying: identity, motion, continuity, story, color, audio, text, or playback.
- Use `cinematic-sequence-extender` for 60 second or longer sequences.
