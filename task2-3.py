# Реализуйте алгоритм перемешивания списка. Встроенный алгоритм SHUFFLE не использовать! Реализовать свой метод

from random import randint as rnd

def randomize(input_list, qtys):
    i = 0
    qtys = int(qtys)
    input_list = []
    while i < qtys:
        input_list.append(rnd(0, 100))
        i += 1
    return input_list

def shuffle(inlist):
    n = 0
    while n < len(inlist):
        swapindex = rnd(0, len(inlist)-1)
        inlist[n], inlist[swapindex] = inlist[swapindex], inlist[n]
        n += 1
    return inlist

qty = input('Введите количество элементов массива: ')
pure_list = []
pure_list = randomize(pure_list,qty)
print(pure_list)
pure_list = shuffle(pure_list)
print(pure_list)