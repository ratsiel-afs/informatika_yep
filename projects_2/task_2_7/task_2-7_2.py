seq = [ "ATATACGCGTA", "CTTCGGNGGA" ]
for string in seq:
    print(f"Данная последовательность: {string}")
    print("Построчно: ")
    for letter in string:
        print(letter)
print("Цикл выполнен")