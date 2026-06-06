# PRODUCTION BIBLE — 지록위마 (指鹿爲馬)

**A Grok Imagine Cinematic Studio v3.5 Production**

**Version:** 1.0  
**Date:** 2026-06  
**Idiom:** 지록위마 (指鹿爲馬) - Pointing to a deer and calling it a horse  
**Target Runtime:** Exactly 2:00 (Title 10s + 8 scenes × 10s = 80s + Credits 10s + living motion extension as needed). All 고사성어 videos must have professional title + ending credits.

**Style:** Hyper-realistic 8K cinematic, film grain, anamorphic lens, grand Qin dynasty imperial palace (massive red pillars, silk banners, misty light, stone floors). Pure ancient East Asian Qin dynasty Chinese historical court setting. Traditional East Asian silk official robes, luxurious but sinister for Zhao Gao. Dramatic lighting, high tension, fear, and moral corruption. No Western, modern military, European, or post-apocalyptic elements whatsoever.

**Locked Variables:**

- [IDIOM:지록위마] = The infamous incident in which the powerful eunuch Zhao Gao (조고) brought a live deer to the Qin court and deliberately called it a horse to test the loyalty and obedience of the officials. Those who truthfully said "deer" were later persecuted or killed. Those who lied and said "horse" were rewarded. This created the idiom meaning the deliberate confusion of truth and lies by those in power.

- [CHARACTER:조고 (Zhao Gao)] = Middle-aged cunning eunuch, sharp and sinister eyes, luxurious dark silk robes with gold accents, authoritative presence. Expression progression: sly smile → cold command → triumphant calm. Body: slender, intimidating.

- [CHARACTER:진2세황제 (Qin Er Shi)] = Young, weak, indecisive emperor in his early 20s, ornate imperial robes. Body: slight build, lacking authority. Expression: confusion and fear.

- [CHARACTER:충성스러운 대신 (Loyal Official)] = Elderly dignified minister, honest face, simple yet noble robes. Body: sturdy. Expression: righteous courage turning to despair.

- [CHARACTER:아첨하는 대신들] = Multiple sycophantic officials in fine robes, fearful and calculating expressions, bowing postures.

- [STYLE] = Hyper-realistic 8K cinematic, photorealistic historical detail (palace architecture, silk, deer, official hats, dramatic side lighting, morning mist in grand halls). Emotional close-ups on faces showing fear, calculation, and moral collapse. Wide shots of the imposing Qin court. Consistent character designs and palace layout across all clips. No drift. Pure ancient East Asian Qin dynasty court setting — traditional robes only.

- [NARRATION] = Consistent calm, professional Korean male narrator voice. Extremely slow, natural, dramatic pace with very long generous pauses. Off-screen voiceover only. Identical timbre, pitch, accent, warmth, and delivery style throughout (reference title and credits clips). Never lip-synced.

- [AUDIO] = Tense traditional Chinese court music (qin, drums, low strings) building dread. Subtle palace atmosphere (footsteps, silk rustling, deer sounds, heavy breathing, fearful whispers). Clear, slow narration. Powerful emotional SFX at the climax (the moment truth is spoken).

**Scene Structure (Title + 8 main scenes + concise credits for exact 2:00):**

The production dramatizes the specific historical incident of Zhao Gao's loyalty test with the deer — the moment power forced an entire court to deny reality.

1. Zhao Gao's scheme in the misty palace (setup)
2. Bringing the deer into court
3. Declaring the deer a horse before the officials
4. The officials' fearful reactions (some lie, some hesitate)
5. The loyal official speaks the truth (climax)
6. Zhao Gao marks the truth-teller for elimination
7. Rewards for liars, removal of the honest (consequence)
8. The idiom is born — power that makes people call a deer a horse (lesson)

All prompts include full style lock, verbatim character DNA, consistency references, historical purity, extreme slow pacing, mandatory subtitles, and off-screen VO rules.

**Title & Credits Rules (Enforced):**
- Title: Elegant single prominent main title "지록위마 (指鹿爲馬)" (one clean line). Hook as one supporting clean line or delivered purely by voice + subtitles. No branding.
- Credits: Extremely concise — idiom name + one powerful thematic line only.

**Production Rules (Enforced from updated gosa-seong-eo-cinematic-script skill):**
- Title first (clean single-line text).
- 10s clips for slow, clear narration.
- Every prompt contains full Character DNA + "exact same ... as in all previous clips of this production. No drift."
- Full historical purity boilerplate in every prompt: "pure ancient East Asian Qin dynasty Chinese historical court setting. Traditional East Asian clothing only. No Western, modern military, European, or post-apocalyptic elements whatsoever."
- EXTREMELY SLOW narration + full off-screen VO paragraph in every video prompt.
- Mandatory clean on-screen Korean subtitles in every video prompt.
- Exact 2:00 without frozen stills: continuous subtle motion in final scenes/credits/pad. No tpad or static cloning.
- Story Origin Focus: The 8 scenes vividly dramatize the exact incident (Zhao Gao's deer test) so viewers remember *why* the saying exists.
- Pre-video keyframe audit for drift and text quality.
- Safe ffmpeg balancing + global normalization.
- All artifacts in artifacts/지록위마_영화/

**Assets Record:**
- Keyframes in refs/ and clips/
- Balanced clips in clips/
- Final assembled 2:00 video in artifacts/지록위마_영화/ and root copy.

**Director's Vision:** A chilling, morally devastating 2-minute historical drama that shows how power can make an entire court deny reality. The viewer must feel the suffocating fear and the terrible cost of speaking truth. Every frame screams "지록위마" — when those in power point at a deer and demand you call it a horse, what will you say?

**End of Initial Bible v1.0**
**Production Started: 지록위마 (指鹿爲馬)**
- Script created following gosa-seong-eo-cinematic-script v0.2+ rules (exact output format, 8 scenes, full boilerplate for purity, slow pacing, subtitles, no-drift, story origin focus).
- Title keyframe generated with strict "SINGLE CLEAN ELEGANT MAIN TITLE ONLY" rule.
- Title video generated and balanced (~10s).
- Scene 1 keyframe (Zhao Gao preparing scheme with deer) generated and video balanced.
- All artifacts saved to artifacts/지록위마_영화/.
- Will continue scene-by-scene with strict consistency anchoring to title + previous clips.
- Final will use living motion pad if needed for exact 2:00 without frozen image.


**Production Update:**
- Title: keyframe + balanced video complete (strict single clean title).
- Scene 1: keyframe + balanced video complete.
- Scene 2 & 3 keyframes generated (bringing deer into court, declaring it a horse).
- Continuing full 8-scene production with strict consistency and all gosa rules.


**image_to_video 에러 원인 분석 (user: "에러나는 이유는 뭘까?")**
- 반복된 에러: "image reference not readable: ... (No such file or directory (os error 2))"
- 관찰: ls, cp, file 명령으로는 파일이 명확히 존재하고 읽을 수 있음. ffmpeg zoompan으로는 동일 jpg에서 정상 mp4 생성 성공.
- 성공 패턴: image_gen 직후 session 내부 images/xx.jpg 경로를 바로 사용하거나, artifacts에 최초 cp한 직후에만 가끔 성공.
- 실패 패턴: 복사/rename 반복, 긴 세션 동안 여러 프로덕션(양두구육 ↔ 지록위마) 파일 작업 후, 특히 artifacts/ 하위 경로를 참조할 때 backend가 reference를 잃음.
- 추정 원인: image_to_video 도구의 이미지 reference resolver (Grok Imagine video backend)가 파일 시스템 경로를 내부적으로 resolve할 때, 세션 캐시/ generation provenance / 메타데이터가 없으면 os error 2로 거부. tool 호출 간 파일 상태가 tool sandbox에 완전히 보이지 않거나, path normalization 문제.
- 우회: ffmpeg으로 keyframe에서 직접 living B-roll 생성 (성공). concat 시에는 명시적 리스트 + pure 지록위마 파일만 사용.
- 양두구육 혼입: 이전에 같은 세션에서 두 프로덕션 동시 작업하면서 /tmp 리스트나 broad cp/concat이 잘못된 balanced 클립을 끌어온 결과. clips dir 자체는 grep으로 깨끗하게 유지됐으나 final이 partial/ mixed로 덮어써짐.

