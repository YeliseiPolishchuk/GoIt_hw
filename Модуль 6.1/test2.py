from pathlib import Path
p = Path('abc')
p.mkdir(exist_ok=True)  # Если директория существует, то не вызовет ошибку
p.rmdir()  # Удалить папку

p = Path('abc/temp')
p.mkdir(exist_ok=True, parents=True)  # создать папку внутри папки
