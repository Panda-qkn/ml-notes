@echo off
chcp 65001 >nul
cd /d %~dp0

echo === 一键提交推送 ===
git add -A

git diff --cached --quiet
if %errorlevel%==0 (
    echo 没有新的改动，无需提交。
    pause
    exit /b 0
)

set msg=%*
if "%msg%"=="" set msg=study: %date:~0,4%-%date:~5,2%-%date:~8,2%

git commit -m "%msg%"
git push

if %errorlevel%==0 (
    echo.
    echo === 推送成功，绿点+1 ===
) else (
    echo.
    echo === 推送失败：检查代理工具是否开启 ===
)
pause
