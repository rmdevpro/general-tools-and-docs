@echo off
echo ============================================ > dependency_install_log.txt
echo Python Dependencies Installation - Started at %DATE% %TIME% >> dependency_install_log.txt
echo ============================================ >> dependency_install_log.txt

cd /d "G:\projects\General Tools and Docs\claude-dev-context-server"
echo Current directory: %CD% >> dependency_install_log.txt
echo. >> dependency_install_log.txt

echo [STEP 1] Check Python Version >> dependency_install_log.txt
echo ---------------------------------------- >> dependency_install_log.txt
"C:\Users\j\AppData\Local\Programs\Python\Python312\python.exe" --version >> dependency_install_log.txt 2>&1
echo Python version check exit code: %ERRORLEVEL% >> dependency_install_log.txt
echo. >> dependency_install_log.txt

echo [STEP 2] Check Pip Version >> dependency_install_log.txt
echo ---------------------------------------- >> dependency_install_log.txt
"C:\Users\j\AppData\Local\Programs\Python\Python312\python.exe" -m pip --version >> dependency_install_log.txt 2>&1
echo Pip version check exit code: %ERRORLEVEL% >> dependency_install_log.txt
echo. >> dependency_install_log.txt

echo [STEP 3] Upgrade Pip >> dependency_install_log.txt
echo ---------------------------------------- >> dependency_install_log.txt
"C:\Users\j\AppData\Local\Programs\Python\Python312\python.exe" -m pip install --upgrade pip >> dependency_install_log.txt 2>&1
echo Pip upgrade exit code: %ERRORLEVEL% >> dependency_install_log.txt
echo. >> dependency_install_log.txt

echo [STEP 4] Install FastMCP >> dependency_install_log.txt
echo ---------------------------------------- >> dependency_install_log.txt
"C:\Users\j\AppData\Local\Programs\Python\Python312\python.exe" -m pip install fastmcp >> dependency_install_log.txt 2>&1
echo FastMCP install exit code: %ERRORLEVEL% >> dependency_install_log.txt
echo. >> dependency_install_log.txt

echo [STEP 5] Install Watchdog >> dependency_install_log.txt
echo ---------------------------------------- >> dependency_install_log.txt
"C:\Users\j\AppData\Local\Programs\Python\Python312\python.exe" -m pip install watchdog >> dependency_install_log.txt 2>&1
echo Watchdog install exit code: %ERRORLEVEL% >> dependency_install_log.txt
echo. >> dependency_install_log.txt

echo [STEP 6] Verify Installation >> dependency_install_log.txt
echo ---------------------------------------- >> dependency_install_log.txt
"C:\Users\j\AppData\Local\Programs\Python\Python312\python.exe" -c "import fastmcp; import watchdog; print('Dependencies successfully installed!')" >> dependency_install_log.txt 2>&1
echo Verification exit code: %ERRORLEVEL% >> dependency_install_log.txt
echo. >> dependency_install_log.txt

echo [STEP 7] List Installed Packages >> dependency_install_log.txt
echo ---------------------------------------- >> dependency_install_log.txt
"C:\Users\j\AppData\Local\Programs\Python\Python312\python.exe" -m pip list | findstr -i "fastmcp watchdog" >> dependency_install_log.txt 2>&1
echo Package list exit code: %ERRORLEVEL% >> dependency_install_log.txt

echo ============================================ >> dependency_install_log.txt
echo Python Dependencies Installation - Completed at %DATE% %TIME% >> dependency_install_log.txt
echo ============================================ >> dependency_install_log.txt
exit /b 0