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


def write(file):
    with open(file, "r") as myfile2:
        lines = myfile2.readlines()
        inn = input('Введите НОВЫЕ данные или ENTER, если не хотите заменять строку.')
        if inn != '':
            lines[0] = inn + '\n'
            if inn != '':
                lines[1] = inn + '\n'
                if inn != '':
                    lines[2] = inn + '\n'

    with open(file, "w") as myfile2:
        myfile2.write(lines[0])
        myfile2.write(lines[1])
        myfile2.write(lines[2])


def read(ft, dir, num):
    file = f'{dir}/{ft}'
    with open(file, "r") as myfile:
        li = myfile.readlines()
        if int(num) > 2:
            fr = [li[line] for line in range(len(li)) if line >= 3]
        else:
            fr = [li[line] for line in range(len(li))]
        fo = iter(fr)
        try:
            for i in count():
                print(next(fo))
                print(next(fo))
                print(next(fo))
                print('Заменить аннотацию')
                write(file)
                if int(num) <= 2:
                    break
                tn = input('Читаем дальше, "Любая клавиша", ВЫХОД в МЕНЮ " n "')
                if tn == 'n':
                    break
                if tn == 'r':
                    pass
        except StopIteration:
            print('Книга закончилась')
            print()





        # li = myfile.readlines()
        # if int(num) > 2:
        #     fr = [li[line] for line in range(len(li)) if line >= 3]



def fil(lstt, a):
    filt = list(filter(lambda x: a in x, lstt))
    return filt
4

def view_filt(list_for, a):
    for i in range(len(list_for)):
        print(f'{i+1}. {fil(list_for, a)[i]}')


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
                ann = input('Хотите прочитать аннотацию? Нет " n " , Да , любая ')
                print()
                if ann == 'n':
                    continue
                else:
                    try:
                        read(list_added_books[number_book()], directory_added_books, num)
                        # name = [list_added_books[number_book()]]
                        # write(name, directory_added_books)
                    except IndexError:
                        print('Нет такой позиции')
            else:
                a = input('Введите данные для фильтрации')
                if fil(list_added_books, a) == []:
                    print('Совпадений не найдено')
                    print()
                    continue
                else:
                    view_filt(fil(list_added_books, a), a)
                    print()
                    ann = input('Хотите прочитать аннотаци? Нет " n " , Да , любая ')
                    if ann == 'n':
                        continue
                    else:
                        try:
                            read(list_added_books[number_book()], directory_added_books, num)
                        except IndexError:
                            print('Нет такой позиции')
        if num == '2':
            view(directory_choice, list_for_analysis)
            print()
            print('Нужно ли отфильтровать список, (y,n)')
            vb_2 = input('Введите (y,n)')
            if vb_2 == 'n':
                ann = input('Хотите прочитать аннотацию? Нет " n " , Да , любая ')
                print()
                if ann == 'n':
                    continue
                else:
                    try:
                        read(list_for_analysis[number_book()], directory_choice, num)
                    except IndexError:
                        print('Нет такой позиции')
            else:
                a = input('Введите данные для фильтрации')
                if fil(list_for_analysis, a) == []:
                    print('Совпадений не найдено')
                    print()
                    continue
                else:
                    view_filt(fil(list_for_analysis, a), a)
                    print()
                    ann = input('Хотите прочитать аннотаци? Нет " n " , Да , любая ')
                    if ann == 'n':
                        continue
                    else:
                        try:
                            read(list_for_analysis[number_book()], directory_choice, num)
                        except IndexError:
                            print('Нет такой позиции')
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
                try:
                    read(list_added_books[number_book()], directory_added_books, num)
                except IndexError:
                    print('Нет такой позиции')
            else:
                a = input('Введите данные для фильтрации')
                view_filt(fil(list_added_books, a), a)
                if fil(list_added_books, a) == []:
                    print('Совпадений не найдено')
                    print()
                    continue
                else:
                    try:
                        read(list_added_books[number_book()], directory_added_books, num)
                    except IndexError:
                        print('Нет такой позиции')
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
