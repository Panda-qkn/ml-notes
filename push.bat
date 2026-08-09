@echo off
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

rem 推送，失败自动重试3次，间隔5秒
set tries=0
:push_retry
set /a tries+=1
if %tries% gtr 1 echo 第 %tries% 次尝试推送...
git push
if %errorlevel%==0 (
    echo.
    echo === 推送成功，绿点+1 ===
    pause
    exit /b 0
)
if %tries% lss 3 (
    echo 推送失败，5秒后重试...
    timeout /t 5 /nobreak >nul
    goto push_retry
)

echo.
echo === 重试3次仍失败：检查代理工具是否开启，稍后再双击本脚本 ===
pause
