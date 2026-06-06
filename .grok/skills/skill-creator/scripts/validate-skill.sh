#!/usr/bin/env bash
set -euo pipefail

skill_dir="${1:-}"
if [ -z "$skill_dir" ]; then
  echo "usage: validate-skill.sh /path/to/skill-dir" >&2
  exit 2
fi

if [ ! -d "$skill_dir" ]; then
  echo "error: skill directory not found: $skill_dir" >&2
  exit 1
fi

skill_file="$skill_dir/SKILL.md"
if [ ! -f "$skill_file" ]; then
  echo "error: missing SKILL.md" >&2
  exit 1
fi

base="$(basename "$skill_dir")"
name="$(awk '/^name: /{sub(/^name: /,""); print; exit}' "$skill_file")"
desc="$(awk '/^description: /{sub(/^description: /,""); print; exit}' "$skill_file")"

if [ "$name" != "$base" ]; then
  echo "error: name does not match directory: name=$name dir=$base" >&2
  exit 1
fi

if ! printf '%s\n' "$name" | grep -Eq '^[a-z0-9]+(-[a-z0-9]+)*$'; then
  echo "error: name must be kebab-case lowercase letters digits and hyphens" >&2
  exit 1
fi

if [ -z "$desc" ]; then
  echo "error: missing description" >&2
  exit 1
fi

if printf '%s' "$desc" | grep -q ':'; then
  echo "error: description must not contain colons" >&2
  exit 1
fi

if printf '%s' "$desc" | grep -Eq '[<>]'; then
  echo "error: description must not contain angle brackets" >&2
  exit 1
fi

desc_len="$(printf '%s' "$desc" | wc -c | tr -d ' ')"
if [ "$desc_len" -gt 1024 ]; then
  echo "error: description exceeds 1024 characters" >&2
  exit 1
fi

line_count="$(wc -l < "$skill_file" | tr -d ' ')"
if [ "$line_count" -gt 500 ]; then
  echo "error: SKILL.md exceeds 500 lines" >&2
  exit 1
fi

if find "$skill_dir" \( -iname 'README.md' -o -iname 'CHANGELOG.md' \) | grep -q .; then
  echo "error: README.md and CHANGELOG.md are not allowed inside skill directories" >&2
  exit 1
fi

echo "ok: $base"
