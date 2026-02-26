volume = int(input("Введите необходимый объём раствра (мл): "))
salt_mass = volume * 0.009

with open("C:/Users/ninel/OneDrive/Документы/gurieva_ne/projects_2/task_2_4/recipe.txt", "w", encoding="utf-8") as file:
    file.write("ОТЧЁТ ПО ПРИГОТОВЛЕНИЮ:\n")
    file.write("-" * 21)
    file.write(f"\nОбщий объем:\t{volume} мл\nМасса соли:\t{salt_mass:.2f} г\nОбъем воды:\t{volume} мл")