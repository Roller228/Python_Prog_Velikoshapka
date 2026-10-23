while True:
    try:
        L = int(input("Введите расстояние L в сантиметрах: "))
        break
    except ValueError:
        print("Ошибка: введите целое число.")

if L >= 0:
    meters = L // 100
    print(f"Количество полных метров: {meters}")
else:
    print("Расстояние не может быть отрицательным.")