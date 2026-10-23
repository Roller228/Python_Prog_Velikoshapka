from ipalib.output import result
from pycparser.c_ast import While

while True:
    try:
        a = int(input("Введие a: "))
        b = int(input("Введите B: "))
        break
    except ValueError:
        print("Ошибка: нужно ввести целок число")


if a > b:
    result = a**2 + b**2
else:
    result = b - a

print("Результат:", result )