@echo off
echo FastRunDev %1 %2 %3 %4 %5 %6 %7 %8 %9
if "%1" == "/w" (
    %2 %3 %4 %5 %6 %7 %8 %9
    echo.
    echo Program Exited.
    echo Press any key x2 to Quit.
    pause>nul
    echo Press any key x1 to Quit.
    pause>nul
    exit
) else (
    if "%COMPUTERNAME%" == "WYF9" (
        set wpy=python
    ) else (
        set wpy=d:\wyf9\python311\python.exe
        )
    echo ComputerName ^= %COMPUTERNAME%
    start %0 /w %wpy% Main.py %1 %2 %3 %4 %5 %6 %7 %8 %9
    )
