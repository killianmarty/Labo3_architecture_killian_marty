CALL java -jar swagger-codegen-cli.jar generate -i api.yaml -l python-flask
CALL java -jar swagger-codegen-cli.jar generate -i api.yaml -l python

setlocal enabledelayedexpansion

set "old_value=8080"
set "new_value=5555"
set "input_file=swagger_server\__main__.py"
set "output_file=swagger_server\__main__.py"

for /f "usebackq delims=" %%a in ("%input_file%") do (
    set "line=%%a"
    set "line=!line:%old_value%=%new_value%!"
    echo !line! >> "tmp.py"
)

move /y "tmp.py" "%output_file%"

if exist "tmp.py" del "tmp.py"
endlocal