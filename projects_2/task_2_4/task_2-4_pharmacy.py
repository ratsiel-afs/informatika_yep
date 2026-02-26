capsules_total_number = int(input("Введите общее количество произведенных капсул: "))
packing_capacity = int(input("Введите количество капсул в одной упаковке: "))

complete_packages_number = capsules_total_number // packing_capacity
remains = capsules_total_number % packing_capacity

print(f"\n--- Отчет фасовочного цеха ---\nПолных упаковок:\t{complete_packages_number}\nОстаток капсул:  \t{remains}")