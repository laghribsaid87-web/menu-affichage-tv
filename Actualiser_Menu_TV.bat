@echo off
color 0A
title Mise a jour Menu TV

echo ========================================================
echo       Mise a jour de l'affichage TV en cours...
echo ========================================================
echo.

cd /d "%~dp0"

echo 1. Enregistrement des modifications...
git add .

echo 2. Creation de la version...
git commit -m "Mise a jour du menu (Prix / Images)"

echo 3. Envoi vers la TV (Internet)...
git push

echo.
echo ========================================================
echo      SUCCES ! Le menu a ete mis a jour avec succes.
echo      La TV va s'actualiser d'ici quelques secondes.
echo ========================================================
echo.
pause
