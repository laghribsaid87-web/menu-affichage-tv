@echo off
color 0B
title Serveur Localhost - Menu TV
cd /d "%~dp0"
echo ========================================================
echo       Demarrage du serveur Localhost (Menu TV)...
echo ========================================================
echo.
echo Le serveur est accessible sur :
echo    http://localhost:8000
echo.
echo Pour arreter le serveur, fermez cette fenetre.
echo ========================================================
echo.
python server.py
pause
