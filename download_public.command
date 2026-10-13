#!/bin/bash
cd "$(dirname "$0")" || exit 2
if ! command -v python3 >/dev/null 2>&1; then
  echo "Python 3.9+ is required. Install Python first; this script does not install software."
  read -r -p "Press Enter to exit. " _
  exit 2
fi
python3 download.py --all --docs --pack "$@"
result=$?
echo "Exit code: $result. Check reports/download-report.md; skipped/licensed items are not completed."
read -r -p "Press Enter to close. " _
exit "$result"
