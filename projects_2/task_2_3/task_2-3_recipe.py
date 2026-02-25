nutrient_medium_name = input("Введите название питательной среды: ")
agar_concentration = input("Введите концентрацию агара (в процентах): ")
temperature = input("Введите температуру стерилизации: ")

with open("recipe.txt", "w", encoding="utf-8") as recipe_file:
    recipe_file.write(f"\t{nutrient_medium_name}\nКонцентрация агара: {agar_concentration}\nТемпература стерилизации: {temperature}")

print("Файл 'recipe.txt' успешно сформирован!")