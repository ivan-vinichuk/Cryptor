import pyAesCrypt
import os
import sys
from colorama import init, Fore, Back, Style

# функция шифрования файла
def encryption(file, password):

    # задаём размер буфера
    buffer_size = 512 * 1024

    # вызываем метод шифрования
    pyAesCrypt.encryptFile(
        str(file),
        str(file) + ".crp",
        password,
        buffer_size
    )

    # чтобы видеть результат выводим на печать имя зашифрованного файла
    print("[Файл '" + str(os.path.splitext(file)[0]) + "' зашифрований]")

    # удаляем исходный файл
    os.remove(file)

# функция сканирования директорий
def walking_by_dirs(dir, password):

    # перебираем все поддиректории в указанной директории
    for name in os.listdir(dir):
        path = os.path.join(dir, name)

        # если находим файл, то шифруем его
        if os.path.isfile(path):
            try:
                encryption(path, password)
            except Exception as ex:
                print(ex)
        # если находим директорию, то повторяем цикл в поисках файлов
        else:
            walking_by_dirs(path, password)
init()



while True:
    security_key = input("Введiть персональний ключ доступу: ")
    if security_key == 'QJNXR-7D97Q-K7WH4-RYWQ8-6MT6Y':
        break
    else:
        print('\nКлюч невірний, у доступі відмовленно\n')
def console_picture():
    print(Style.BRIGHT + Fore.GREEN)
    print("   ***************************  ")
    print("   ***************************  ")
    print("   *** Шифрувальщик файлів ***   ")
    print("   ***                     ***  ")
    print("   ***         BETA        ***   ")
    print("   ***                     ***   ")
    print("   ***        Версiя       ***   ")
    print("   ***************************  ")
    print("   ***************************  ")

console_picture()    

            
#security_key = input("Введiть клюк доступу: ")
directories = input("\nВведiть шлях для шифрування: ")
password = input("Введiть пароль для шифрування: ")
walking_by_dirs(directories, password)
input('\nНажміть ENTER щоб вийти') 
# os.remove(str(sys.argv[0]))

