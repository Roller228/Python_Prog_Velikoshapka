from ipalib.output import result
from pycparser.c_ast import While
from wx.lib.pydocview import Print


#Даны два целых числа: A, B. Проверить истинность высказывания: «Хотя бы одно
#из чисел A и B четное»

#Вывод с проверкой
while True:
    try:
        a = int(input("Введие a: "))
        b = int(input("Введите B: "))
        break
    except ValueError:
        print("Ошибка: нужно ввести целок число")

#Проверка высказывания
if a % 2 == 0 or b % 2 == 0:
    print("Высказывание истинно: хотя бы одно число четное")
else:
    print("Высказывание истинно: ни одно из числе не четное")

result = a % 2 == 0 or b % 2 == 0
print("Результат:", result )