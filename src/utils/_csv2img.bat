set csv_path=%1
set json_path=%2
python ./src/utils/csv2json.py %csv_path% json_in/%json_path%
python ./src/main.py %json_path%