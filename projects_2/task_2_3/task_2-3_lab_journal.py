researcher_fio = input('Введите ФИО исследователя: ')
date = input('Введите дату: ')
experiment_name = input('Введите название эксперимента: ')
conclusion = input('Введите вывод: ')

with open("journal.txt", "w", encoding="utf-8") as journal:
    journal.write(f"+" + "-" * 50 + "+\n")
    journal.write(f"| Электронный лабораторный журнал |\n")
    journal.write(f"+" + "-" * 50 + "+\n")
    journal.write(f"| ФИО исследователя : {researcher_fio}  |\n")
    journal.write(f"| Дата              : {date}            |\n")
    journal.write(f"| Эксперимент       : {experiment_name} |\n")
    journal.write(f"+" + "-" * 50 + "+\n")
    journal.write(f"| Вывод:{' ' * 40}|\n")
    journal.write(f"| {conclusion} |\n")
    journal.write(f"+" + "-" * 50 + "+\n")

print("\nФайл 'journal.txt' успешно создан!")