@echo off
if "%1"=="/gcback" goto goto2
:go
cls
set wdir=%~dp0
title cmdChat v0.1 for wyf9 2023.3.18
echo cmdChat Main Menu: 
echo a / 1. This is a Server
echo b / 2. This is a Console
echo q / 0. Quit

:goto
call %wdir%modules\getChar\wapi.bat
:goto2
echo %wapi%
if "%wapi%"=="a" goto Server
if "%wapi%"=="b" goto Console
if "%wapi%"=="q" goto end
if "%wapi%"=="1" goto Server
if "%wapi%"=="2" goto Console
if "%wapi%"=="0" goto end
goto goto

:Server
echo.
echo Be a Server.
goto goto

:Console
echo.
echo Be a Console.
goto goto

:end