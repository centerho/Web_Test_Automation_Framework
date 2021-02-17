pytest -s -v -m "sanity" --html=./reports/report.html testCases/ --browser chrome
pytest -s -v -m "sanity" --html=./reports/report.html testCases/ --browser firefox


rem chrome
rem pytest -s -v -m "sanity" --html=./reports/report.html testCases/ --browser chrome
rem pytest -s -v -m "sanity or regression" --html=./reports/report.html testCases/ --browser chrome
rem pytest -s -v -m "sanity and regression" --html=./reports/report.html testCases/ --browser chrome
rem pytest -s -v -m "regression" --html=./reports/report.html testCases/ --browser chrome

rem firefox
rem pytest -s -v -m "sanity" --html=./reports/report.html testCases/ --browser firefox
rem pytest -s -v -m "sanity or regression" --html=./reports/report.html testCases/ --browser firefox
rem pytest -s -v -m "sanity and regression" --html=./reports/report.html testCases/ --browser firefox
rem pytest -s -v -m "regression" --html=./reports/report.html testCases/ --browser firefox