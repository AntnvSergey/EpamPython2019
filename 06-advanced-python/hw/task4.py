"""
Реализовать метод __str__, позволяющий выводить все папки и файлы из данной, например так:
> print(folder1)
V folder1
|-> V folder2
|   |-> V folder3
|   |   |-> file3
|   |-> file2
|-> file1
А так же возможность проверить, находится ли файл или папка в другой папке:
> print(file3 in folder2)
True
"""


class PrintableFolder:
    def __init__(self, name, info):
        self.name = name
        self.info = info

    def __str__(self):
        return self.content(-1)

    def __contains__(self, item):
        check = False
        for i in self.info:
            if item.name == i.name:
                return True
            elif hasattr(i, 'info'):
                check = i.__contains__(item)
            if check:
                return True

    def content(self, layer):
        layer += 1
        message = 'V ' + self.name
        for i in self.info:
            if hasattr(i, 'content'):
                message += '\n' + layer*'|   ' + '|-> ' + i.content(layer)
            else:
                message += '\n' + layer*'|   ' + '|-> ' + i.name
        return message


class PrintableFile:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


file1 = PrintableFile('file1')
file2 = PrintableFile('file2')
file3 = PrintableFile('file3')
file4 = PrintableFile('file4')
folder4 = PrintableFolder('folder4', [file3])
folder3 = PrintableFolder('folder3', [file3])
folder2 = PrintableFolder('folder2', [folder3, file2])
folder1 = PrintableFolder('folder1', [folder2, file1])
print(folder1)
print(file1 in folder1)

