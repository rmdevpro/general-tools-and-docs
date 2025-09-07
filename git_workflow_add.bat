@echo off
cd /d "G:\projects\General Tools and Docs"
"C:\Program Files\Git\bin\git.exe" add . > git_add_result.txt 2>&1
echo Git add exit code: %ERRORLEVEL% >> git_add_result.txt
exit /b 0