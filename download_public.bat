@echo off
cd /d "%~dp0"
where py >nul 2>nul
if %errorlevel% equ 0 (
  py -3 download.py --all --docs --pack %*
) else (
  python download.py --all --docs --pack %*
)
echo Check reports\download-report.md for saved, failed, partial and skipped items.
pause
