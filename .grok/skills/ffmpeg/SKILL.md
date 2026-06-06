---
name: ffmpeg
description: Trim, concatenate, transcode, normalize, subtitle, inspect, and repair video or audio files with ffmpeg.
---

# FFmpeg

Use this skill for deterministic video and audio processing.

## Workflow
1. Inspect media with `ffprobe` before editing.
2. Use `run_terminal_command` or `bash`, whichever the runtime exposes.
3. Write all outputs under `artifacts/<project>/`.
4. Preserve originals and write corrected files with clear suffixes such as `_corrected`, `_balanced`, or `_final`.
5. Verify duration, frame count, streams, and playback-sensitive metadata after processing.

## Common Commands
```bash
ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 input.mp4
ffmpeg -i input.mp4 -an -c copy video_only.mkv
ffmpeg -i input.mp4 -vn -af "loudnorm=I=-16:TP=-1.5:LRA=11,alimiter=limit=0.98" -c:a aac audio.m4a
ffmpeg -i video_only.mkv -i audio.m4a -c:v copy -c:a copy -map 0:v -map 1:a -shortest output_corrected.mp4
```
