import argparse
from pathlib import Path
from shutil import copyfile

parser = argparse.ArgumentParser(description='File sorter')
parser.add_argument('--source', '-s', required=True, help='source path')
parser.add_argument('--output', '-o', default='out', help='sorted files')

args = vars(parser.parse_args())

input = args.get('source')
output = args.get('output')

print(input, output)


def read_folder(path: Path) -> None:
    for elem in path.iterdir():
        if elem.is_dir():
            read_folder(elem)
        else:
            copy_file(elem)


def copy_file(file: Path):
    ext = file.suffix
    new_path = output_folder/ext
    new_path.mkdir(exist_ok=True, parents=True)
    copyfile(file, new_path/file.name)


output_folder = Path(output)
read_folder(Path(input))