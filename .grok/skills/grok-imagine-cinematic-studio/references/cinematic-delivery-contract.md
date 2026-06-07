# Cinematic Delivery Contract

Use this contract for every multi-clip Grok Imagine production. It turns good
intentions into required artifacts, handoffs, and pass/fail gates.

## Required State Files
Create or update these files under `artifacts/<project>/` for every production:

- `project_bible.md` - locked variables, story spine, visual bible, audio bible.
- `clip_registry.csv` - clip id, duration, keyframe path, raw clip path, corrected clip path, end-frame path, status.
- `handoff_packets/clip_XX_to_YY.md` - transition contract between adjacent clips.
- `qa/clip_XX_report.md` - keyframe and clip QA results.
- `qa/rough_cut_report.md` - assembled-sequence review before final delivery.
- `final_delivery_manifest.md` - final asset list, verification, QA scores, limitations, next-cut notes.

## Gate 1 - Story Lock
Before keyframes, Studio Director, Mega Production Architect, and Narrative
Strategist must lock:

- Logline and core theme.
- Central question or dramatic promise.
- Beginning state, escalation, climax, resolution, and final emotional state.
- Clip-by-clip scene function. No clip may exist only because it looks good.
- Promise/Payoff Ledger listing every setup and where it is paid off.
- Ending Closure Check confirming the central question is answered or intentionally left open.

No generation begins while the story spine is incomplete.

## Gate 2 - Style And Continuity Lock
Before keyframes, DoP, Production Designer, Color Supervisor, Identity Lock,
Continuity Guardian, and Sonic Architect must lock:

- Visual Style Bible: aspect ratio, lens language, camera movement vocabulary, composition rules, lighting baseline, allowed evolution.
- Grade Bible: color temperature curve, contrast, saturation, grain, skin-tone or material rules, forbidden drift.
- World/Prop Bible: geography, time of day, weather, set dressing, prop states, wardrobe states.
- Character DNA: identity anchors, allowed transformation, forbidden drift.
- Audio Bible: narrator or vocal profile, ambient bed, music motif, SFX priority, silence strategy, per-clip mix notes.

Keyframe prompts must copy these locked decisions instead of reinterpreting them.

## Gate 3 - Clip Transition Contract
For every adjacent pair, Sequence Director and Continuity Guardian must create a
handoff packet before generating the next keyframe:

```markdown
# Clip XX to Clip YY Handoff Packet
- Previous clip:
- Previous corrected clip path:
- Previous end-frame path:
- Previous end state: action, pose, expression, prop state, wardrobe, environment, lighting.
- Outgoing action vector:
- Incoming start-frame target:
- Screen direction:
- Camera velocity carryover:
- Color and lighting carryover:
- Emotional level handoff: XX/10 to YY/10.
- Audio tail: final audible beat, ambience, music, silence, or SFX.
- Audio bridge into next clip:
- Cut type: match action, graphic match, hard cut, dissolve, sound bridge, insert, reaction, or deliberate rupture.
- Allowed discontinuities:
- Must-not-change items:
- Acceptance criteria:
```

If continuity would feel abrupt, add a bridge shot, reaction shot, insert, or
B-roll before approving the pair.

## Gate 4 - Stage QA Thresholds
QA Guardian must issue explicit Go, Conditional Go, or No-Go.

- Keyframe QA: pass at 85+ overall.
- Clip QA: pass at 88+ overall.
- Transition QA: pass at 90+ overall for every adjacent pair.
- Rough Cut QA: pass at 90+ overall before final polish.
- Final Master QA: pass at 92+ overall.
- Critical categories must be 8/10 or higher: identity, continuity, story function, motion naturalness, audio sync, mix clarity, visual harmony, text/subtitles, playback integrity.

Any critical category below threshold requires a targeted fix or an explicit
Director override recorded in the manifest.

## Gate 5 - Rough Cut Review
After assembly, watch or inspect the full rough cut as one film before final
delivery. The report must cover:

- Story clarity and ending closure.
- Clip-to-clip action continuity.
- Emotional carryover and pacing.
- Visual rhythm and repeated compositions.
- Color, lighting, wardrobe, prop, and world drift.
- Audio level jumps, language drift, voice drift, SFX audibility, music continuity.
- Title, credit, subtitle, and text cleanliness.
- Needed reshoots, edits, bridge shots, inserts, reaction shots, trims, or extensions.

No final delivery is allowed until the rough cut report is passed or addressed.

**SCRIPT-TO-FINAL ATOMIC RULE**: When the user supplies a full scenario or "make the drama", all gates (Story Lock, Style/Continuity Lock, every Clip Transition Contract, Normalization, Rough Cut Review, Final Master QA + ffprobe, Manifest) are non-waivable and must be executed in one continuous flow by the Studio Director + Mega Production Architect. Partial outputs or "we have some clips" are forbidden. The session only concludes with the playable master + manifest in the designated final/ location.

## Recovery Protocol
When a generation fails, classify the failure first:

- Identity drift.
- Motion artifact or frozen action.
- Continuity break.
- Story function failure.
- Color or style drift.
- Audio language, voice, sync, SFX, or distortion failure.
- Text, subtitle, or title error.
- Playback, duration, frame count, or encoding failure.

Then choose one targeted action:

- `image_edit` the keyframe when composition is close.
- Regenerate the keyframe when identity, story, or staging is wrong.
- Rerun `image_to_video` when keyframe is strong but motion/audio fails.
- Insert a bridge, reaction, or B-roll shot when the cut is abrupt.
- Strip audio and provide silent visual plus post audio spec when native audio fails repeatedly.
- Update negative prompts, locked variables, handoff packet, and QA notes before retrying.

Do not burn retries by regenerating without a failure class and changed prompt.

## Final Delivery Manifest
Every final delivery must include:

- Final video path and all source clip paths.
- Project Bible path and current locked variables.
- Story Spine and Promise/Payoff Ledger status.
- Clip registry and handoff packet list.
- QA scores by stage, rejected versions, and fixes applied.
- ffprobe verification for final duration, frame count, frame rate, and audio streams.
- Subtitle, title, credits, audio, and post-production notes.
- Known limitations and recommended next cut.
