@echo off
if "%1" == "/w" (
    echo Starting Progress "%2"...
    echo.
    %4 %2
    echo.
    echo Progress Exited.
    echo Press any key x2 to Quit.
    pause>nul
    echo Press any key x1 to Quit.
    pause>nul
    exit
) else (
    start %0 /w Main.py /p d:\wyf9\python311\python.exe
)
