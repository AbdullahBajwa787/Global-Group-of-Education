@echo off
title Global Group of Education - Local Server
echo ============================================================
echo   Global Group of Education Localhost Server
echo   Opening in your browser: http://localhost:8080
echo ============================================================
start http://localhost:8080
python -u server.py
pause
