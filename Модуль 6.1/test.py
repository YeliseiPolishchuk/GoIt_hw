file = open('text.txt', 'w', encoding='utf-8')
file.write('Hello, my name is Yelisei!\n')
file.write('Hello, i\'m Python\n')
lst = ['Kyiv\n', 'Lviv\n', 'Kharkiv\n']
file.writelines(lst)
file.close()

with open('text.txt', 'r', encoding='utf-8') as file:
    # for line in file.readlines():
    # print(line)
    print(file.read())
