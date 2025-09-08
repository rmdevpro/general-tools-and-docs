@echo off
cd /d "G:\projects\General Tools and Docs"
echo Starting git operations... > git_complete_result.txt

echo Adding all changes... >> git_complete_result.txt
"C:\Program Files\Git\bin\git.exe" add . >> git_complete_result.txt 2>&1
echo Git add exit code: %ERRORLEVEL% >> git_complete_result.txt

echo Committing changes... >> git_complete_result.txt
"C:\Program Files\Git\bin\git.exe" commit -m "Phase 3 Complete: Framework Integration" >> git_complete_result.txt 2>&1
echo Git commit exit code: %ERRORLEVEL% >> git_complete_result.txt

echo Creating milestone tag... >> git_complete_result.txt
"C:\Program Files\Git\bin\git.exe" tag -a "mcp-framework-v0.3.0" -m "Phase 3 Complete: MCP Framework Integration" >> git_complete_result.txt 2>&1
echo Git tag exit code: %ERRORLEVEL% >> git_complete_result.txt

echo Pushing to remote... >> git_complete_result.txt
"C:\Program Files\Git\bin\git.exe" push origin main >> git_complete_result.txt 2>&1
echo Git push exit code: %ERRORLEVEL% >> git_complete_result.txt

echo Pushing tags... >> git_complete_result.txt
"C:\Program Files\Git\bin\git.exe" push --tags >> git_complete_result.txt 2>&1
echo Git push tags exit code: %ERRORLEVEL% >> git_complete_result.txt

echo All git operations complete! >> git_complete_result.txt
exit /b 0