@echo off
echo ========================================================
echo   AMINA'S 23RD BIRTHDAY GIFT - ONLINE SYNC TO GITHUB
echo ========================================================
echo.
echo [1/3] Copying latest HTML to index.html...
copy /Y Instagram_Chat_Analysis_Amina_Hamid.html index.html >nul

echo [2/3] Adding changes to Git...
git add index.html Instagram_Chat_Analysis_Amina_Hamid.html images sync_to_github.bat

echo [3/3] Committing and Pushing to GitHub (hamidgazi/amina)...
git commit -m "Update Amina birthday memories, photos, and love letter"
git push origin main

echo.
echo ========================================================
echo   SUCCESS! Website is live and updated at:
echo   https://hamidgazi.github.io/amina/
echo ========================================================
echo.
pause
