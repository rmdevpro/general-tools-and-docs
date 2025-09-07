@echo off
cd /d "G:\projects\General Tools and Docs"
"C:\Program Files\Git\bin\git.exe" config user.email "claude@anthropic.com" > git_config_result.txt 2>&1
"C:\Program Files\Git\bin\git.exe" config user.name "Claude Assistant" >> git_config_result.txt 2>&1
"C:\Program Files\Git\bin\git.exe" commit -m "General Tools and Docs: Initial repository setup - Complete framework with 25 files" >> git_config_result.txt 2>&1
echo Git config and commit exit code: %ERRORLEVEL% >> git_config_result.txt
exit /b 0