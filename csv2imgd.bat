set name=%1

call "src/utils/_csv2json.bat" %name%
python src/main.py %name%.json d 