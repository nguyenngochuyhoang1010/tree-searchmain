@echo off
REM run.bat - Execute search.py with input file and method

REM Check if the second argument is empty. Using "==" for clarity.
if "%~2" == "" (
    echo Usage: run.bat ^<filename^> ^<method^>
    echo Example: run.bat test_cases\test1.txt bfs
    exit /b 1
)

REM If arguments are provided, show what's being run and then execute it.
echo Executing: python search.py %1 %2
python search.py %1 %2
