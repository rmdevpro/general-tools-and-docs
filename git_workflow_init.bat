@echo off
cd /d "G:\projects\General Tools and Docs"
"C:\Program Files\Git\bin\git.exe" init > git_init_result.txt 2>&1
echo Git init exit code: %ERRORLEVEL% >> git_init_result.txt
exit /b 0