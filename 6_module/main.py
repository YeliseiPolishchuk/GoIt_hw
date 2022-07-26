import sys
from pathlib import Path
from sorting_func import read_folder, rename_file


folder_path = Path(sys.argv[1])
# folder_path = Path('to_sort')


# Создаю папку для отсортированных файлов
sorted_folder_path = Path('./sorted')
sorted_folder_path.mkdir(exist_ok=True, parents=True)


read_folder(folder_path)
rename_file(sorted_folder_path)
