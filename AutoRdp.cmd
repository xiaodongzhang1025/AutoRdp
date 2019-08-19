@echo off
setlocal enabledelayedexpansion
echo %date% %time%
echo %~0
title %~0 

start "AutoRdp" D:\Python27\pythonw.exe AutoRdp.py

rem pause