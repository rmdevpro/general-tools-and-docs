@echo off
cd /d "G:\projects\General Tools and Docs"
"C:\Program Files\Git\bin\git.exe" status > git_status_result.txt 2>&1
"C:\Program Files\Git\bin\git.exe" log --oneline -3 >> git_status_result.txt 2>&1
echo Git status exit code: %ERRORLEVEL% >> git_status_result.txt
exit /b 0