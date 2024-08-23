@echo off
call venv\scripts\activate
pytest -s -v -m "sanity" --html .\reports\test_report.html --browser chrome
pause