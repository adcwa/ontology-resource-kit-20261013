#!/bin/bash
cd "$(dirname "$0")" || exit 2
if ! command -v python3 >/dev/null 2>&1; then
  echo "Python 3.9+ is required."
  read -r -p "Press Enter to exit. " _
  exit 2
fi
echo "Includes large public candidates. Default transfer budget: 2048 MiB."
python3 download.py --all --docs --include-large --pack "$@"
result=$?
echo "Exit code: $result. Check reports/download-report.md."
read -r -p "Press Enter to close. " _
exit "$result"
