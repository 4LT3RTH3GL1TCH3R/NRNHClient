@echo off

echo Updating package lists...
@REM This would be used for Linux; on Windows, updating isn't needed this way.

echo Installing Python...
@REM Installing Python via winget (Windows Package Manager)
winget install Python.Python.3

echo Installing pip...
@REM pip is included with Python installation on Windows

echo Installing colorama...
pip install colorama

echo Installing discord.py...
pip install discord.py

echo Verifying Python installation...
python --version
pip --version

echo Python and necessary packages have been installed successfully!
pause
