#!/usr/bin/env bash
set -euo pipefail

show_help() {
  cat <<EOF
Usage: $0 [OPTIONS]

Take one still with rpicam-still and rename the produced file to ISO8601.

Options (all optional):
  --width N
  --height N
  --rotation N
  --hflip 0|1
  --vflip 0|1
  --brightness N
  --contrast N
  --saturation N
  --sharpness N
  --gain N
  --quality N         JPEG quality (0-100)
  --annotate TEXT
  --outdir PATH
  --utc
  --help

Example:
  $0 --width 1920 --height 1080 --quality 95 --annotate "Front cam" --utc
EOF
}

OUTDIR="."
USE_UTC=0

declare -A OPTS

while [[ $# -gt 0 ]]; do
  case "$1" in
    --width) OPTS[width]="$2"; shift 2 ;;
    --height) OPTS[height]="$2"; shift 2 ;;
    --rotation) OPTS[rotation]="$2"; shift 2 ;;
    --hflip) OPTS[hflip]="$2"; shift 2 ;;
    --vflip) OPTS[vflip]="$2"; shift 2 ;;
    --brightness) OPTS[brightness]="$2"; shift 2 ;;
    --contrast) OPTS[contrast]="$2"; shift 2 ;;
    --saturation) OPTS[saturation]="$2"; shift 2 ;;
    --sharpness) OPTS[sharpness]="$2"; shift 2 ;;
    --gain) OPTS[gain]="$2"; shift 2 ;;
    --quality) OPTS[quality]="$2"; shift 2 ;;
    --annotate) OPTS[annotate]="$2"; shift 2 ;;
    --outdir) OUTDIR="$2"; shift 2 ;;
    --utc) USE_UTC=1; shift ;;
    --help|-h) show_help; exit 0 ;;
    *) echo "Unknown option: $1"; show_help; exit 1 ;;
  esac
done

if ! command -v rpicam-still >/dev/null 2>&1; then
  echo "Error: rpicam-still not found in PATH." >&2
  exit 2
fi

mkdir -p -- "$OUTDIR"

args=()

for k in "${!OPTS[@]}"; do
  v="${OPTS[$k]}"
  case "$k" in
    width) args+=( --width "$v" ) ;;
    height) args+=( --height "$v" ) ;;
    rotation) args+=( --rotation "$v" ) ;;
    hflip) args+=( --hflip "$v" ) ;;
    vflip) args+=( --vflip "$v" ) ;;
    brightness) args+=( --brightness "$v" ) ;;
    contrast) args+=( --contrast "$v" ) ;;
    saturation) args+=( --saturation "$v" ) ;;
    sharpness) args+=( --sharpness "$v" ) ;;
    gain) args+=( --gain "$v" ) ;;
    quality) args+=( --quality "$v" ) ;;
    annotate) args+=( --annotate "$v" ) ;;
  esac
done

tmpfile="$(mktemp --suffix=.jpg)"
trap 'rm -f -- "$tmpfile"' EXIT

echo "Running: rpicam-still ${args[*]} -o $tmpfile"
rpicam-still --immediate "${args[@]}" -o "$tmpfile"

if [[ "$USE_UTC" -eq 1 ]]; then
  timestamp="$(date -u +"%Y-%m-%dT%H-%M-%SZ")"
else
  timestamp="$(date +"%Y-%m-%dT%H-%M-%S")"
fi

outfile="$OUTDIR/${timestamp}.jpg"
mv -- "$tmpfile" "$outfile"
trap - EXIT

echo "Saved: $outfile"
