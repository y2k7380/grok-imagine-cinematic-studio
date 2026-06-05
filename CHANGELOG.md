# Changelog

## [Unreleased / TUI Supplement] - Actual Video Production
- Analyzed all cinematic skills and identified that "generation" was prompt-only.
- Supplemented **grok-imagine-cinematic-studio** + 14 supporting SKILL.md files (and created the two missing `sequence-director` + `cinematic-sequence-extender` SKILL.md) so the studio **actually produces video**.
- Integrated the built-in `imagine` skill's video protocol: keyframe image first (image_gen/edit with consistency), then `image_to_video` (or reference_to_video) with short motion prompt derived from DoP.
- Added end-frame PNG extraction via ffmpeg + LAST_FRAME_RECAP update for pixel-level + descriptive continuity across clips.
- Added final assembly via `ffmpeg -f concat ... -c copy`.
- Updated Daily Directing Loops, 6-step workflows, output templates, and integration rules across agents to drive **real tool calls** instead of prompt text for users.
- Synced key changes back to root `agents/*.txt` and `MASTER_PROMPT_v3.4.md` references for consistency.
- Now `EXECUTE FIRST CLIP`, `START FULL SEQUENCE` etc. result in real .mp4 files + stitched final film in the workspace.
- All agents now explicitly follow "reference-first, keyframe-staged, simple-motion, 6s-preferred" video rules.
- Added AUDIO LANGUAGE LOCK PROTOCOL (verified with "공무도하가" production — user confirmed "한국어 잘 나옴").

All notable changes to Grok Imagine Cinematic Studio will be documented in this file.

## [3.5.1] - 2026-06-02

### Added
- Complete **22-agent Role Card system** in `references/agents/` with full structure:
  - Core Mission
  - v3.5 / v4.0 Upgrades
  - Key Responsibilities
  - Specialized Protocols
  - Decision Frameworks
  - Output Formats
  - Activation Triggers
  - Integration Notes
- Comprehensive `AGENT_INDEX.md` in `references/agents/`
- Improved CI workflow (`cinematic-agent-workflow-ci.yml` v3.5) with:
  - Role Card structure validation
  - `references/agents/` directory checking
  - Configurable `validation_mode` (standard / strict / full)
  - Better agent detection logic
- Updated documentation:
  - Revised `README.md` (accurate 22-agent count, Role Card emphasis)
  - Updated `Quick_Start_Guide.md` v2.0 with improved workflow and specialist table
- Full `grok-imagine-cinematic-studio` skill pulled with latest `MASTER_PROMPT_v3.5.md`

### Changed
- Standardized all agent files to `*_v3.5.txt` naming
- Expanded and refined all 22 agent Role Cards to full detailed format
- Improved consistency across agent activation commands
- Better alignment between project structure and documentation

### Fixed
- Broken filename in agents directory (`Continuity_Consistency_Guardian`)
- Outdated agent counts and references in documentation
- Missing references to the new `references/agents/` Role Card system

---

## [3.5.0] - 2026-06

### Added
- Full 22-agent cinematic production system
- ErosForge NSFW Director with artistic standards
- Cinematic Sequence Extender for long-form content
- Native audio design integration
- Production Bible system
- Modular prompt template architecture
- Comprehensive agent personality versioning
- Streamlit Web UI
- Python CLI toolkit

### Changed
- Major reorganization of agent folder structure by production department
- Improved continuity and identity lock systems

## [3.4.0] - Previous

- Initial multi-agent orchestration
- Core leadership agents (Studio Director + Mega Production Architect)
- Basic Production Bible support