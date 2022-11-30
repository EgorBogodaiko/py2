# Задайте список из n чисел последовательности (1 + 1/n)^n. Вывестив консоль сам список и сумму его элементов.
qty = int(input('Введите количество чисел последовательности:  '))
list_fun = []
sum = 0
i=1
while i<=qty:
    list_fun.append(round((1 + 1/i)**i,2))
    sum+=list_fun[i-1]
    i+=1
print(list_fun)
print(sum)