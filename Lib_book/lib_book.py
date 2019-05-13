import os
import shutil
from itertools import count

list_for_analysis = []  # todo Временное хранение списка на разбор и добавление
directory_choice = os.getcwd() + '/the_choice'  # todo  директория хранящая файлы на разбор и добавление
directory_added_books = os.getcwd() + '/the_added_books'  # todo директория хранения файлов бибилиотеки
list_added_books = []  # todo Временное хранение списка бибилиотеки


def view(directory, listt):  # todo  вывод списка библиотеки или списка на разбор
    files = os.listdir(directory)
    files = sorted(files, reverse=True)
    for i in range(len(files)):
        if files[i].endswith('.txt') or files[i].endswith('.doc'):
            listt.append(files[i])
            print(f'{i+1}. {files[i]}')
    return listt


def view_filt(list_for, a):
    for i in range(len(list_for)):
        print(f'{i+1}. {fil(list_for, a)[i]}')


def number_book():
    selected_book_number = int(input('Впишите НОМЕР книги, с которой произвести действие \n'))
    selected_book_number = selected_book_number - 1
    return selected_book_number


def transfer_file_to_lib(book, d_c, d_a_b):  # todo добавление в библиотеку
    directory_file_choice = f'{d_c}/{book}'
    directory_file_added = f'{d_a_b}/{book}'
    if os.path.isfile(directory_file_added) is True:
        print('Такая книга уже есть в биюлиотеке')
    else:
        shutil.move(directory_file_choice, directory_file_added)


def read(ft, dir):
    file = f'{dir}/{ft}'
    with open(file, "r") as myfile:
        fr = [line for line in myfile.readlines()]
        fo = iter(fr)
        try:
            for i in count():
                print(next(fo))
                print(next(fo))
                print(next(fo))
                tn = input('Читаем дальше, "Любая клавиша", заканчиваем "n')
                if tn == 'n':
                    break
        except StopIteration:
            print('Книга закончилась')
            print()


def fil(lstt, a):
    filt = list(filter(lambda x: a in x, lstt))
    return filt


if __name__ == '__main__':

    for i in count():
        list_added_books = []
        list_for_analysis = []
        num = input("Главное меню, что необходимо сделать ?\n"
                    "1 - Показать список книг в библиотеке\n"
                    "2 - Показать книги 'На добавление'\n"
                    "3 - Добавление в библиотеку'\n"
                    "4 - Почитаем'\n"
                    "5 - Удаление из библиотеки")
        print()
        if num == '1':
            view(directory_added_books, list_added_books)
            print()
            print('Нужно ли отфильтровать список, (y,n)')
            vb = input('Введите (y,n)')
            if vb == 'n':
                continue
            else:
                a = input('Введите данные для фильтрации')
                if fil(list_added_books, a) == []:
                    print('Совпадений не найдено')
                    print()
                    continue
                else:
                    view_filt(fil(list_added_books, a), a)
                    print()
        if num == '2':
            view(directory_choice, list_for_analysis)
            print()
            print('Нужно ли отфильтровать список, (y,n)')
            vb_2 = input('Введите (y,n)')
            if vb_2 == 'n':
                continue
            else:
                a = input('Введите данные для фильтрации')
                if fil(list_for_analysis, a) == []:
                    print('Совпадений не найдено')
                    print()
                    continue
                else:
                    view_filt(fil(list_for_analysis, a), a)
                    print()
        if num == '3':
            view(directory_choice, list_for_analysis)
            print()
            print('Нужно ли отфильтровать список, (y,n)')
            vb_2 = input('Введите (y,n)')
            if vb_2 == 'n':
                transfer_file_to_lib(list_for_analysis[number_book()], directory_choice,
                                     directory_added_books)
            else:
                a = input('Введите данные для фильтрации')
                view_filt(fil(list_for_analysis, a), a)
                if fil(list_for_analysis, a) == []:
                    print('Совпадений не найдено')
                    print()
                    continue
                else:
                    transfer_file_to_lib(fil(list_for_analysis, a)[number_book()], directory_choice,
                                         directory_added_books)
        if num == '4':
            view(directory_added_books, list_added_books)
            print()
            print('Нужно ли отфильтровать список, (y,n)')
            vb_2 = input('Введите (y,n)')
            if vb_2 == 'n':
                read(list_added_books[number_book()], directory_added_books)
            else:
                a = input('Введите данные для фильтрации')
                view_filt(fil(list_added_books, a), a)
                if fil(list_added_books, a) == []:
                    print('Совпадений не найдено')
                    print()
                    continue
                else:
                    read(fil(list_added_books, a)[number_book()], directory_added_books)
        if num == '5':
            view(directory_added_books, list_added_books)
            print()
            print('Нужно ли отфильтровать список, (y,n)')
            vb_2 = input('Введите (y,n)')
            if vb_2 == 'n':
                transfer_file_to_lib(list_added_books[number_book()], directory_added_books,
                                     directory_choice)
            else:
                a = input('Введите данные для фильтрации')
                view_filt(fil(list_added_books, a), a)
                if fil(list_added_books, a) == []:
                    print('Совпадений не найдено')
                    print()
                    continue
                else:
                    transfer_file_to_lib(list_added_books[number_book()], directory_added_books,
                                         directory_choice)
