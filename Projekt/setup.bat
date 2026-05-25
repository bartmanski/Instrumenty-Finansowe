@echo off
REM Setup script for Windows - creates venv and configures Jupyter kernel
cd /d "%~dp0"
echo ======================================
echo Setting up Jupyter environment...
echo ======================================
python setup.py %*
pause
