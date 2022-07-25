import os
import sys
from pathlib import Path
from shutil import copyfile

trans_map = {
    ord('а'): 'a',
    ord('б'): 'b',
    ord('в'): 'v',
    ord('г'): 'g',
    ord('д'): 'd',
    ord('е'): 'e',
    ord('ё'): 'yo',
    ord('ж'): 'zh',
    ord('з'): 'z',
    ord('и'): 'i',
    ord('й'): 'y',
    ord('к'): 'k',
    ord('л'): 'l',
    ord('м'): 'm',
    ord('н'): 'n',
    ord('о'): 'o',
    ord('п'): 'p',
    ord('р'): 'r',
    ord('с'): 's',
    ord('т'): 't',
    ord('у'): 'u',
    ord('ф'): 'f',
    ord('х'): 'h',
    ord('ц'): 'ts',
    ord('ч'): 'ch',
    ord('ш'): 'sh',
    ord('щ'): 'shch',
    ord('ъ'): 'y',
    ord('ы'): 'y',
    ord('ь'): "'",
    ord('э'): 'e',
    ord('ю'): 'yu',
    ord('я'): 'ya',
    ord('А'): 'A',
    ord('Б'): 'B',
    ord('В'): 'V',
    ord('Г'): 'G',
    ord('Д'): 'D',
    ord('Е'): 'E',
    ord('Ё'): 'Yo',
    ord('Ж'): 'Zh',
    ord('З'): 'Z',
    ord('И'): 'I',
    ord('Й'): 'Y',
    ord('К'): 'K',
    ord('Л'): 'L',
    ord('М'): 'M',
    ord('Н'): 'N',
    ord('О'): 'O',
    ord('П'): 'P',
    ord('Р'): 'R',
    ord('С'): 'S',
    ord('Т'): 'T',
    ord('У'): 'U',
    ord('Ф'): 'F',
    ord('Х'): 'H',
    ord('Ц'): 'Ts',
    ord('Ч'): 'Ch',
    ord('Ш'): 'Sh',
    ord('Щ'): 'Shch',
    ord('Ъ'): 'Y',
    ord('Ы'): 'Y',
    ord('Ь'): "'",
    ord('Э'): 'E',
    ord('Ю'): 'Yu',
    ord('Я'): 'Ya',
    ord('і'): 'i',
}

# расширения файлов для сортровки
photo_ext = ['.jpeg', '.png', '.jpg', '.svg']
vid_ext = ['.avi', '.mp4', '.mov', '.mkv']
doc_ext = ['.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx']
mus_ext = ['.mp3', '.ogg', '.wav', '.amr']
arch_ext = ['.zip', '.gz', '.tar']

folder_path = Path(sys.argv[1])
# folder_path = Path('to_sort')


# Создаю папку для отсортированных файлов
sorted_folder_path = Path('./6_module/sorted')
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
        new_path = sorted_folder_path / 'photos'  # Создаю путь к новой папке
        new_path.mkdir(exist_ok=True)  # Создаю папку
        # Копирую файл и переношу в новую папку
        copyfile(file, new_path / file.name)
    elif ext in vid_ext:
        new_path = sorted_folder_path / 'videos'
        new_path.mkdir(exist_ok=True)
        copyfile(file, new_path / file.name)
    elif ext in doc_ext:
        new_path = sorted_folder_path / 'docs'
        new_path.mkdir(exist_ok=True)
        copyfile(file, new_path / file.name)
    elif ext in mus_ext:
        new_path = sorted_folder_path / 'music'
        new_path.mkdir(exist_ok=True)
        copyfile(file, new_path / file.name)
    elif ext in arch_ext:
        new_path = sorted_folder_path / 'archives'
        new_path.mkdir(exist_ok=True)
        copyfile(file, new_path / file.name)
    else:
        new_path = sorted_folder_path / 'else'
        new_path.mkdir(exist_ok=True)
        copyfile(file, new_path / file.name)


def normalize(file: Path) -> None:
    '''Функция изменяет имя файла на допустимое(убирает пробелы и кириллицу)'''
    parent_dir = file.parent  # корень файла
    old_name = file.name  # старое имя файла
    new_name = old_name.translate(trans_map).replace(
        ' ', '')  # новое имя файла
    # переименовую (корень  файла/имя файла -> корень файла/новое имя файла
    os.rename(parent_dir / old_name, parent_dir / new_name)


def rename_file(path: Path) -> None:
    for elem in path.iterdir():
        if elem.is_dir():
            rename_file(elem)
        else:
            normalize(elem)


read_folder(folder_path)
rename_file(sorted_folder_path)
