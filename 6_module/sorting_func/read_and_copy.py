from pathlib import Path
from shutil import copyfile

sorted_folder_path = Path('./sorted')
sorted_folder_path.mkdir(exist_ok=True, parents=True)


dict_ext = {
    'photos': ['.jpeg', '.png', '.jpg', '.svg'],
    'videos': ['.avi', '.mp4', '.mov', '.mkv'],
    'documents': ['.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx'],
    'music': ['.mp3', '.ogg', '.wav', '.amr'],
    'archives': ['.zip', '.gz', '.tar'],
    'else': []
}


def read_folder(path: Path) -> None:
    '''Функция прохода по файлам в папке'''
    for elem in path.iterdir():
        if elem.is_dir():
            read_folder(elem)
        else:
            copy_file(elem)


def copy_file(file: Path):
    file_ext = file.suffix
    for category, category_ext in dict_ext.items():
        if file_ext in category_ext:
            new_path = sorted_folder_path/category
            new_path.mkdir(exist_ok=True)
            copyfile(file, new_path/file.name)
            return
        dict_ext['else'].append(file_ext)
        new_path = sorted_folder_path/'else'
        new_path.mkdir(exist_ok=True)
        copyfile(file, new_path/file.name)
