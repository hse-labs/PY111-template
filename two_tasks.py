'''
4. Навигатор на сетке.
Дана плоская квадратная двумерная сетка (массив), на которой определена стоимость захода в каждую ячейку
 (все стоимости положительные). Необходимо найти путь минимальной стоимости из заданной ячейки в заданную
 ячейку и вывести этот путь.
'''
arr = [[8, 7, 22, 13],
       [22, 17, 55, 12],
       [33, 55, 52, 77],
       [71, 23, 64, 28]]


def nav(a, b):
    pr = []
    for i in range(a, b):
        for h in range(len(arr[i])):
            j = min(arr[i])
            l = arr[i].index(j)
            k = arr[i][:l + 1:]
            pr.append(k)
            break
    print(pr)


nav(0, 4)
print('Задание 4\n')

'''
5. Задача консенсуса DNA ридов
При чтении DNA последовательностей могут возникать единичные ошибки, выражающиеся в неверной букве в строке. 
Для решения данной проблемы требуемое место читается несколько раз, после чего строится консенсус-строка, 
в которой на каждом месте будет стоять тот символ, что чаще всего встречался в этом месте суммарно во всех чтениях. 
Т.е. для строк 
ATTA
ACTA
AGCA
ACAA
'''

import collections

less = [['A', 'T', 'T', 'A'],
        ['A', 'C', 'T', 'A'],
        ['A', 'G', 'C', 'A'],
        ['A', 'C', 'A', 'A']]
less2 = []
less3 = []
d = {}
l = ''


def re(BB):
    for i in range(len(less)):
        less2.append(less[i][BB])
        d = collections.Counter(less2)
    for k, v in iter(d.items()):
        if v == max(d.values()):
            l = k
    return l


if __name__ == "__main__":
    print(re(1))  # todo Укажите номер валидиоуемого символа
print('Задание 5\n')

'''
6 .Задание с ракетой.
'''


def rok():
    odna = True
    df = []
    zan = [[2, 4], [5, 7], [8, 9], [22, 23]]
    for i in zan:
        st = i[0]
        sh = i[1]
        vrem = range(st, sh)
        for j in zan:
            if i == j or j in df:
                pass
            else:
                if j[0] == st:
                    odna = False
                if j[1] in vrem:
                    odna = False
                if j[0] in vrem:
                    odna = False
                if st in range(j[0], j[1] + 1):
                    odna = False
        df.append(i)
    print('Хватит одной ракеты') if odna else print('Не хватит одной')


rok()
print('Задание 6')
