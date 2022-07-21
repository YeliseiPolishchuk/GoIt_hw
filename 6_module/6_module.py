import sys
from pathlib import Path
from shutil import copyfile

# расширения файлов для сортровки
photo_ext = ['.jpeg', '.png', '.jpg', '.svg']
vid_ext = ['.avi', '.mp4', '.mov', '.mkv']
doc_ext = ['.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx']
mus_ext = ['.mp3', '.ogg', '.wav', '.amr']
arch_ext = ['.zip', '.gz', '.tar']

folder_path = Path(sys.argv[1])

sorted_folder_path = Path('./6_module/sorted')  # Создаю папку для отсортированных файлов
sorted_folder_path.mkdir(exist_ok=True, parents=True)


def read_folder(path: Path) -> None:
    '''Функция прохода по файлам в папке'''
    for elem in path.iterdir():
        if elem.is_dir():
            read_folder(elem)
        else:
            copy_file(elem)


def copy_file(file: Path) -> None:
    '''Функция, которая копирует файл, изменяет имя и отправляет в отсортированную папку'''
    ext = file.suffix  # расширение файла
    if ext in photo_ext:
        new_path = sorted_folder_path/'photos'
        new_path.mkdir(exist_ok=True)
        copyfile(file, new_path/file.name)
    elif ext in vid_ext:
        new_path = sorted_folder_path/'videos'
        new_path.mkdir(exist_ok=True)
        copyfile(file, new_path/file.name)
    elif ext in doc_ext:
        new_path = sorted_folder_path/'docs'
        new_path.mkdir(exist_ok=True)
        copyfile(file, new_path/file.name)
    elif ext in mus_ext:
        new_path = sorted_folder_path/'music'
        new_path.mkdir(exist_ok=True)
        copyfile(file, new_path/file.name)
    elif ext in arch_ext:
        new_path = sorted_folder_path/'archives'
        new_path.mkdir(exist_ok=True)
        copyfile(file, new_path/file.name)
    else:
        new_path = sorted_folder_path/'else'
        new_path.mkdir(exist_ok=True)
        copyfile(file, new_path/file.name)


read_folder(folder_path)
