#!/usr/bin/env bash
set -euo pipefail

# rpicam_shot.bash
# Usage example:
# ./rpicam_shot.bash --width 1920 --height 1080 --rotation 180 --hflip 1 --annotate "Camera 1" --outdir /home/pi/pics --utc

show_help() {
  cat <<EOF
Usage: $0 [OPTIONS]

Take one still with rpicam-still and rename the produced file to ISO8601.

Options (all optional):
  --width N            image width (px)
  --height N           image height (px)
  --rotation N         rotation (0,90,180,270)
  --hflip 0|1          horizontal flip
  --vflip 0|1          vertical flip
  --brightness N       brightness (0-100)
  --contrast N         contrast (-100..100)
  --saturation N       saturation (-100..100)
  --sharpness N        sharpness (-100..100)
  --gain N             analog gain (if supported)
  --annotate TEXT      annotation text (quoted if contains spaces)
  --outdir PATH        output directory (default: ./)
  --utc                use UTC and suffix 'Z' (default: local time)
  --safe               replace ':' with '-' (default: enabled)
  --help               show this help and exit

Example:
  $0 --width 1920 --height 1080 --annotate "Front cam" --outdir ~/timelapse --utc
EOF
}

# defaults
OUTDIR="."
USE_UTC=0
SAFE=1

# parse args (long options)
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
    --annotate) OPTS[annotate]="$2"; shift 2 ;;
    --outdir) OUTDIR="$2"; shift 2 ;;
    --utc) USE_UTC=1; shift ;;
    --safe) SAFE=1; shift ;;
    --no-safe) SAFE=0; shift ;;
    --help|-h) show_help; exit 0 ;;
    *) echo "Unknown option: $1"; show_help; exit 1 ;;
  esac
done

# check rpicam-still exists
if ! command -v rpicam-still >/dev/null 2>&1; then
  echo "Error: rpicam-still not found in PATH." >&2
  exit 2
fi

mkdir -p -- "$OUTDIR"

# build rpicam-still args array
args=()

# map provided options to rpicam-still CLI names (long names)
# NOTE: depends on rpicam-still supporting these long options (common on recent builds).
# If your version uses short flags, edit accordingly.
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
    annotate) args+=( --annotate "$v" ) ;;
  esac
done

# create temp file for rpicam output
tmpfile="$(mktemp --suffix=.jpg)"
cleanup() {
  rm -f -- "$tmpfile" || true
}
trap cleanup EXIT

# run rpicam-still (use --immediate to avoid delays if supported)
# If your rpicam-still variant doesn't support --immediate or some long options,
# remove or adapt the flags above.
echo "Running: rpicam-still ${args[*]} -o $tmpfile"
# Note: do not set -e for rpicam-still failure? we keep set -e so script exits on failure.
rpicam-still --immediate "${args[@]}" -o "$tmpfile"

# build ISO8601 filename (file-safe: colons replaced by hyphens)
if [[ "$USE_UTC" -eq 1 ]]; then
  # UTC with trailing Z
  timestamp="$(date -u +"%Y-%m-%d_%H-%M-%SZ")"
else
  timestamp="$(date +"%Y-%m-%d_%H-%M-%S")"
fi

outfile="$OUTDIR/${timestamp}.jpg"

# move temp -> final atomically
mv -- "$tmpfile" "$outfile"
# cancel trap cleanup (file moved)
trap - EXIT

echo "Saved: $outfile"
