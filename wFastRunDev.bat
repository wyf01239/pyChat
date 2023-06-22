@echo off
if "%1" == "/w" (
    %2 %3 %4 %5 %6 %7 %8 %9
    echo.
    echo Press any key to Quit.
    pause>nul
    exit %ERRORLEVEL%
) else (
    if "%COMPUTERNAME%" == "WYF9" (
        set wpy=python
    ) else (
        set wpy=d:\wyf9\python311\python.exe
        )
    set execute=Main.py
    echo Computer Name: %COMPUTERNAME%
    echo START %wpy% %execute% %1 %2 %3 %4 %5 %6
    start /WAIT %0 /w %wpy% %execute% %1 %2 %3 %4 %5 %6
    echo Process Exited.
    echo Code: %ERRORLEVEL%
    )
