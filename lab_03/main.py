from dataclasses import dataclass
from os.path import isfile, exists

from message import Message
from encryption.file_encryption import des_encipher_file


@dataclass
class Settings:
    msg = '''
Шифрование алгоритмом DES

Выберите пункт меню:
1 - Зашифровать файл
2 - Расшифровать файл
0 - Выход

Выбор: '''

    red = '\033[0;31m'
    end = '\033[0;0m'

    encipher_file = 1
    decipher_file = 2
    exit = 0


def encipher_file():
    file = input('\nВведите имя файла: ')
    
    message = Message()

    if not exists(file) or \
       not isfile(file):
        message.danger('Файл не найден!')
        return

    des_encipher_file(file)

    return

def decipher_file():
    file = input('\nВведите имя файла: ')
    
    message = Message()

    if not exists(file) or \
       not isfile(file):
        message.danger('Файл не найден!')
        return

    des_encipher_file(file, deciphering = True)

    return


if __name__ == '__main__':
    run = True
    message = Message()

    while run:
        command =  int(input(Settings.msg))

        if command == Settings.encipher_file:
            encipher_file()
        elif command == Settings.decipher_file:
            decipher_file()
        elif command == Settings.exit:
            run = False
        else:
            message.danger('Выбран неверный пункт меню!')
