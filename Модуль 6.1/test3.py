from pathlib import Path

message = 'Привіт світ!'
'''Изменить кодировку строки'''
print(message.encode())
print(message.encode('utf-16'))
print(message.encode('cp1251'))

s = b'\xcf\xf0\xe8\xe2\xb3\xf2 \xf1\xe2\xb3\xf2!'
print(s.decode('cp1251'))

p = Path()
with open(p / 'utf-8.txt', 'wb') as file:
    file.write(message.encode())

with open(p / 'utf-16.txt', 'wb') as file:
    file.write(message.encode('utf-16'))

with open(p / 'cp1251.txt', 'wb') as file:
    file.write(message.encode('cp1251'))
