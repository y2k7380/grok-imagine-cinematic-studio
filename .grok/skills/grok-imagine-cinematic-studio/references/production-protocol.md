# Video Production Protocol (Detailed)

This reference contains the full detailed rules, flows, and helpers that were previously in the main SKILL.md. The core SKILL.md now points here for depth while remaining lean.

**This environment has real Imagine tools.** The studio no longer just writes prompts — it **produces actual video files** (.mp4) by calling tools.

## Tool Naming Contract
- Preferred Grok Build tool names: `image_gen`, `image_edit`, `image_to_video`, `reference_to_video`, and `run_terminal_command`.
- If a runtime exposes `generate_image` instead of `image_gen`, use it as the image generation alias.
- If a runtime exposes `edit_image` instead of `image_edit`, use it as the image editing alias.
- If a runtime exposes `bash` instead of `run_terminal_command`, use `bash` for ffmpeg and file operations.

## MANDATORY RULES (all agents)
- Follow Imagine Prompt Master and this protocol for every image/video call (reference-first for people, keyframe staging, short motion prompts, 6s preference, consistency via base reuse + end-frames, no pure text-to-video). If a global `imagine` skill exists in the runtime, load it as an additional source.
- When generating, the video rules in this protocol are the law for shot planning and prompt craft.
- **Keyframe-first**: Never call `image_to_video` or `reference_to_video` without a prior approved keyframe image from `image_gen`/`image_edit`.
- QA Guardian issues Go/No-Go before every keyframe AND before every video animation.
- Use locked [VARIABLES], character DNA, and continuity recaps verbatim in all prompts.
- Record every generated asset path in Project Bible + studio state under `artifacts/<project>/` (e.g. `artifacts/<project>/clips/clip_01.mp4`, `artifacts/<project>/clips/clip_01_keyframe.png`).
- **Keyframe Image Saving Rule**: After every keyframe generation (`image_gen`/`generate_image` or `image_edit`/`edit_image`), save a copy of the keyframe image to the project's `clips/` directory in addition to `refs/`. This makes stills easily accessible alongside the video clips for editing, review, or re-use.

## AUDIO LANGUAGE LOCK PROTOCOL (Critical for mixed-language projects)
- AI video tools often bake in unwanted vocals/singing that default to English, Japanese, or multilingual mix even when the prompt is in English.
- For any motion_prompt that mentions voice, singing, lament, dialogue, or "sings":
  - **Explicitly lock language**: "SINGING / VOCALS IN [TARGET LANGUAGE] ONLY (e.g. KOREAN LANGUAGE ONLY). Exact lyrics/phonemes: [quote the full text in original script]. No English words, no Japanese, no other languages, no code-switching, no narration in wrong language."
  - Safer default for reliability: "NO HUMAN SINGING OR SPEECH WHATSOEVER. Pure ambient sound design only — wind, river, fabric, footsteps, no voices, no lyrics, no English, no Japanese, no singing."
- Repeat the ban 2–3 times in the prompt. Put it near the front.
- In the Production Bible, always have a separate "Target Audio Language" field and "Vocal Spec" section.
- If the tool still mixes languages: immediately strip audio with ffmpeg (`-an`) and deliver clean visual tracks. Provide the correct-language singing as a separate asset or user post-production task.
- Sonic Architect must specify exact language + lyrics in every audio direction handed to Imagine Prompt Master.
- Never assume the model will "just do Korean" — always over-specify and ban alternatives. Mixing = failure. Single consistent language (or silence) = acceptable.

## Narration Pacing Control (Critical for Educational Lectures & Long-form Content)
- Short-form (shorts/reels) bias in the model often produces unnaturally fast narration. For lecture, course, or educational content, ALWAYS override this.
- In every narration motion prompt, explicitly include: "slow, natural, comfortable educational lecture narration pace. Deliver at relaxed speaking speed (~120-140 words per minute) with clear natural pauses, breathing, and sentence separation. Do NOT rush, accelerate, or compress the speech to fit the clip duration — use calm, articulate, unhurried delivery even if it results in a measured, professional pace with slight pauses."
- Prefer 10-second duration for narration-dense clips. Split dense scripts across multiple clips if needed rather than forcing fast delivery.
- In the Production Bible, mark narration-heavy sections and note target pace.

## Narration (Voiceover) vs Character Dialogue/Performance Separation
- Narration is off-screen voiceover and must remain separate from any on-screen character performance or dialogue.
- In all prompts involving narration: "This is off-screen voiceover narration. The voice is completely separate from the visuals. NO on-screen character is speaking the narration text. No lip movement, mouth animation, talking head delivering lines, or character appearing to voice the narration. Use B-roll, diagrams, abstract visuals, code interfaces, non-speaking elements (hands, back view, silhouette), or pure visual storytelling only. If a human element appears, they are not the source of the narration voice."
- Dialogue (if any character speaks on-screen) must be explicitly labeled as separate "character dialogue" with its own script and visual sync rules. Never conflate lecture narration with character speech.
- For pure educational lectures, default to no visible speaker for the main narration track.

## Sound Design Reality in This Environment
The primary (and often only) way to get sound effects, ambient, and music (including narration) is through the generative audio baked into `image_to_video` / `reference_to_video`. This is guided entirely by the richness of the "embedded sound description" in the motion prompt. There is no separate high-quality music or foley generation tool available here.

## Important note on Narration / Voice
- Narration voices are synthesized by the video model's native audio engine on a per-clip basis.
- Each `image_to_video` call generates its own audio independently.
- This means there can be natural variation in voice timbre, tone, and characteristics between different clips, even with identical instructions.
- **Voice Consistency Protocol for Multi-Clip Narrated Content (e.g. lectures):**
  - Always use an extremely detailed and identical voice descriptor in **every** narration prompt.
  - Include reference to previous clips: "use the exact same calm professional Korean educational narrator voice as in the title and credits clips of this series — identical timbre, pitch, accent, warmth, and delivery style throughout the entire lecture."
  - Add "maintain perfect voice consistency across all clips in this production".
  - For best results, generate title/credits first (or a "voice reference clip"), then reference them explicitly in subsequent clips.
  - If variation is still too high for the project, fall back to silent video + external consistent TTS (studio can produce silent version + full script list).
- The studio can easily produce clean silent versions + complete script lists on request.

Therefore:
- Sonic Architect + Imagine Prompt Master must collaborate to create highly specific, cinematic sound descriptions for every single clip, with **SFX Volume Priority** (user feedback: effects too quiet or inaudible, but "EXTREMELY LOUD" in prompt or high post-boost can cause distortion "직직"): Use "prominent loud clear [SFX], punchy and easily audible foreground sound effects that stand out strongly". Avoid "extremely loud" in prompt.
- The Production Bible must contain a full "Audio Bible" with multi-layer breakdown + volume targets for every clip, marking SFX as highest priority.
- **Mandatory Audio Post-Processing Pass (after every clip generation — users report raw SFX too quiet, but volume=4.0+ causes "직직" distortion):**
  - Use `run_terminal_command` or `bash` with ffmpeg for safe balancing:
    - `ffmpeg -i clip.mp4 -af "loudnorm=I=-16:TP=-1.5:LRA=11,volume=2.2,alimiter=limit=0.95" -c:v copy clip_balanced.mp4` (moderate boost + limiter to prevent clipping/distortion. "boosted 버전이 나은 듯" per feedback, use volume=2.0~2.5).
  - If SFX still too quiet, re-generate with stronger "prominent loud clear foreground SFX" language, then re-balance with the same safe command. Avoid "EXTREMELY LOUD" unless the user explicitly prefers distortion risk.
- After generation, evaluate the baked audio quality. If it doesn't meet the vision, deliver silent visuals + complete post-production audio spec, or re-generate the clip with refined sound prompt.

## Per-Shot Production Flow (executed via real tool calls)
1. **Plan & Craft (DoP + Imagine Prompt Master + Performance + Continuity + Sonic Architect):**
   - Detailed `keyframe_prompt` using Ultimate Template + quality stack + all refs + locked vars (for beautiful frame 1).
   - **Sound Design Pass** (Sonic Architect): Create detailed "embedded audio description" — specific SFX, ambient layers, music cues, spatial audio notes that match the action and emotion.
   - Short `motion_prompt` (1-2 sentences, present tense): subject + action + exact `[CAMERA_MOVE]` from DoP + lighting/mood **+ rich sound design description from Sonic**. 
     Example: "Slow anamorphic push-in on the rain-soaked detective as he lights a cigarette, subtle eye shift to camera, neon reflections, god rays through blinds, with layered sound design: distant thunder rumble, wet footsteps on pavement, subtle melancholic string drone swelling, wind gusts."
2. **Produce Keyframe:**
   - Select consistency base(s) via Identity Lock + last extracted end-frame if continuing.
   - `image_gen(prompt=keyframe_prompt, aspect_ratio="16:9")` for new or `image_edit(prompt=..., image=base_path)` for continuity. Use `generate_image` / `edit_image` aliases only when those are the tool names exposed by the runtime.
   - May loop edits 1-2x based on visual QA.
3. **Animate to Video (only on GO):**
   - `image_to_video(image=keyframe_path, prompt=motion_prompt, duration=6, resolution_name="720p")`
     (The detailed sound description in the prompt guides the model's native audio synthesis for SFX, ambient, and musical elements.)
   - Use `reference_to_video` (with 2+ refs + prompt) only for complex multi-element shots; prefer compositing refs into one keyframe first.
4. **Post-Clip Update:**
   - Update Continuity: `last_frame_recap` (precise description of final frame's action/expression/props/lighting/pose for next prompt).
   - **Audio Review & Safe Boost (mandatory, speed-safe version):** Use the video-lock extract + remux flow (see FFmpeg Helpers) to create *_corrected.mp4 with boost. Never use plain -c:v copy after -af on a clip destined for assembly (causes the "휘리릭" bug where mains speed up but titles/credits don't). Verify each corrected has identical nb_frames to its raw base. Deliver the corrected as primary.
   - Advanced continuity (recommended): run `ffmpeg` via `run_terminal_command` or `bash` to extract exact last frame as PNG for pixel-accurate next keyframe ref.
   - Update Bible shot_list with asset paths, momentum vector, emotional carry-over, and generated audio notes (raw vs balanced).
   - All involved agents output 7-metric self-eval + Director's Notes.
5. **Full Sequence Delivery:**
   - After clips: build concat list, `ffmpeg -f concat -safe 0 -i list.txt -c copy final_cinematic.mp4`
   - Deliver playable final video + individual clips + Production Bible + audio spec.
   - **Audio Note**: Because this environment's primary audio comes from the video model's generative sound baked into image_to_video (guided by rich prompts), complex original music or precise foley often requires post-production. The skill provides full layered audio direction for that purpose.

## FFmpeg Helpers (use via `run_terminal_command` or `bash` when needed)
- Extract last frame of a clip for continuity ref:  
  `ffprobe -v error -select_streams v:0 -count_packets -show_entries stream=nb_read_packets -of csv=p=0 clip.mp4` → then `ffmpeg -i clip.mp4 -vf "select=eq(n\,LAST-1)" -vframes 1 clip_end.png`
- Final assembly (reliable timing, mandatory for complex productions with multiple iterations / any audio post-processing):  
  When all per-clip durs are accurate and no AF was applied: simple `ffmpeg -f concat -safe 0 -i clips/concat.txt -c copy -fflags +genpts ...` is fine.  
  **Preferred robust method (avoids "휘리릭" speed issues from AF-stretched audio duration metadata + heterogeneous clips, as reported "플레이하면 영화 무지 빨리 진행되듯이 휘리릭 가버리네, 타이틀 크레딧 빼고"):**  
  Use frame-accurate filter_complex (respects actual decoded frames, ignores lying format durations):  
  `ffmpeg -i title.mp4 -i clip01_corrected.mp4 ... -i credits.mp4 -filter_complex "[0:v][1:v]...concat=n=8:v=1:a=0[v];[0:a][1:a]...concat=n=8:v=0:a=1[a]" -map "[v]" -map "[a]" -c:v libx264 -preset medium -crf 18 -r 24 -pix_fmt yuv420p -c:a aac ... final.mp4`  
  Then (or instead) the demuxer re-encode with explicit `-r 24` also helps bake clean CFR.  
  **CRITICAL VERIFICATION (always run after AF or assembly):**  
  `ffprobe -v error -select_streams v:0 -show_entries stream=nb_frames,duration,r_frame_rate,avg_frame_rate -of default=noprint_wrappers=1 final.mp4`  
  Compare nb_frames and video stream duration to expected (e.g. 1352 frames / 56.333s for the 7-clip + titles project). If wrong frame count, playback speed will be off even if format duration looks plausible. Title/credits are usually immune because single-gen accurate.
- **Mandatory Audio Balancing (after every clip — "효과음이 잘 들리지 않아" + "boosted 버전이 나은 듯" but "여전히 지직" + "휘리릭 speed bug" lessons applied):**  
  NEVER just `-af ... -c:v copy` on a clip and then feed to concat (causes audio dur skew → container lies → players speed/slow video = "휘리릭" or wrong total time).  
  **Correct safe flow (preserves exact video frames/PTS while adding boost):**  
  ```bash
  ffmpeg -i raw_clip.mp4 -an -c copy video_only.mkv
  ffmpeg -i raw_clip.mp4 -vn -af "loudnorm=I=-16:TP=-1.5:LRA=11,volume=1.3,alimiter=limit=0.98" -c:a aac -b:a 128k -ar 48000 aud.m4a
  ffmpeg -i video_only.mkv -i aud.m4a -c:v copy -c:a copy -map 0:v -map 1:a -shortest -copyts -avoid_negative_ts make_zero clipXX_corrected.mp4
  ```
  (volume=1.3 gentle is the sweet spot that gave "boosted" presence without distortion in this project. Always ffprobe the corrected: video stream nb_frames and duration must match the raw's exactly.)
- Verify: `ls -l *.mp4` and play the final.

## Standard Title Sequence & End Credits (see main SKILL.md for current concise guideline)
The current concise rules (no branding in titles, extremely minimal summary-only credits) are maintained in the main SKILL.md "Standard Title Sequence & End Credits" section. This reference focuses on the production mechanics; always follow the latest concise text rules when generating titles/credits.

---

This file captures the detailed, battle-tested production knowledge so the main SKILL.md can stay focused on activation, high-level flow, agent coordination, and pointers to references.
