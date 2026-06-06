---
name: github-repo-manager
description: Manage GitHub repositories, branches, commits, pull requests, issues, and release files for this workspace.
---

# GitHub Repo Manager

Use this skill for repository operations.

## Workflow
1. Check repository state with `git status`.
2. Use connected GitHub tools when available.
3. If connected tools are unavailable, use `git` and `gh` from the shell if authenticated.
4. Do not rewrite history or delete branches unless the user explicitly asks.
5. Keep generated assets out of commits unless the user wants them versioned.
6. Summarize changed files and commands after completing the operation.

## Safety
- Never expose tokens or secrets.
- Confirm remote and branch before pushing.
- For pull requests, include a concise summary and validation notes.
