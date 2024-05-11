set csv_path=%1
set json_path=%2

call "src/utils/_csv2img.bat" json_in/%csv_path% %json_path%