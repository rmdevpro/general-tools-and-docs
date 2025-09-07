@echo off
cd /d "G:\projects\General Tools and Docs"
"C:\Program Files\Git\bin\git.exe" add . > git_remote_setup_result.txt 2>&1
"C:\Program Files\Git\bin\git.exe" commit -m "Add README.md and complete repository setup" >> git_remote_setup_result.txt 2>&1
"C:\Program Files\Git\bin\git.exe" remote add origin git@github.com:rmdevpro/general-tools-and-docs.git >> git_remote_setup_result.txt 2>&1
"C:\Program Files\Git\bin\git.exe" branch -M main >> git_remote_setup_result.txt 2>&1
"C:\Program Files\Git\bin\git.exe" push -u origin main >> git_remote_setup_result.txt 2>&1
echo Git repository creation exit code: %ERRORLEVEL% >> git_remote_setup_result.txt
exit /b 0