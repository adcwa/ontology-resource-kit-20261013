#!/bin/sh
cd "$(dirname "$0")" || exit 2
exec python3 download.py --all --docs --pack "$@"
