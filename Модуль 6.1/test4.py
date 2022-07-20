import shutil

print(shutil.get_archive_formats())

archive_file = shutil.make_archive('archive_one', 'zip', 'Temp')  # Создать архив

archive_file =shutil.unpack_archive(archive_file, 'Temp/abc')   # разархивировать архив