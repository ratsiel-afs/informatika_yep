weight = float(input("Введите вес (кг): "))
height = float(input("Введите рост (см): "))

bmi = weight / ((height / 100) ** 2)
print(f"\n--- Отчет о состоянии здоровья ---\nРост:\t{height}\nВес:\t{weight}\nИндекс массы тела:\t{bmi:.2f}")