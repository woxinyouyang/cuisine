@echo off
chcp 65001 >nul
cd /d "%~dp0"
echo.
echo  中华古典菜肴百科
echo.
echo  Starting local server at http://localhost:8080
echo  Press Ctrl+C to stop.
echo.
python -m http.server 8080
pause
