import pyAesCrypt
import os
import sys
from colorama import init, Fore, Back, Style

# функция дешифровки файла
def decryption(file, password):

    # задаём размер буфера
    buffer_size = 512 * 1024

    # вызываем метод расшифровки
    pyAesCrypt.decryptFile(
        str(file),
        str(os.path.splitext(file)[0]),
        password,
        buffer_size
    )

    # чтобы видеть результат выводим на печать имя зашифрованного файла
    print("[Файл '" + str(os.path.splitext(file)[0]) + "' розшифрований]")

    # удаляем исходный файл
    os.remove(file)

# функция сканирования директорий
def walking_by_dirs(dir, password):

    # перебираем все поддиректории в указанной директории
    for name in os.listdir(dir):
        path = os.path.join(dir, name)

        # если находим файл, то дешифруем его
        if os.path.isfile(path):
            try:
                decryption(path, password)
            except Exception as ex:
                print(ex)
        # если находим директорию, то повторяем цикл в поисках файлов
        else:
            walking_by_dirs(path, password)
            
           
while True:
    security_key = input("Введiть персональний ключ доступу: ")
    if security_key == 'QJNXR-7D97Q-K7WH4-RYWQ8-6MT6Y':
        break
    else:
        print('\nКлюч невірний, у доступі відмовленно')
    
init()
            
def console_picture():
    print(Style.BRIGHT + Fore.BLUE)
    print("   *****************************  ")
    print("   *****************************  ")
    print("   *** Дешифрувальщик файлів ***   ")
    print("   ***                       ***  ")
    print("   ***         BETA          ***   ")
    print("   ***                       ***   ")
    print("   ***        Версiя         ***   ")
    print("   *****************************  ")
    print("   *****************************  ")

console_picture()
            
#security_key = input("Введiть клюк доступу: ")
directories = input("\nВведiть шлях для розшифрування: ")
password = input("Введiть пароль для розшифрування: ")
walking_by_dirs(directories, password)
input('\nНажміть ENTER щоб вийти') 
# os.remove(str(sys.argv[0]))
