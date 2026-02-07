from PyInstaller.utils.hooks import collect_data_files

# Collect templates and other required files from python-docx
datas = collect_data_files("docx")
