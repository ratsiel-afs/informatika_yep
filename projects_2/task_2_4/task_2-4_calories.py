protein_g = int(input("Введите массу белков в продукте (г): "))
fats_g = int(input("Введите массу жиров в продукте (г): "))
carbohydrates_g = int(input("Введите массу углеводов в продукте (г): "))

calories = (protein_g * 4) + (fats_g * 9) + (carbohydrates_g * 4)
print(f"Общая калорийность продукта: {calories} ккал")