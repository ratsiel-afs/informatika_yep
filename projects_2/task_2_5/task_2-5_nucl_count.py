print(f"=== Анализ последовательности ДНК ===")
dna = input(f"\nВведите последовательность ДНК: ").upper()
print(f"\nПоследовательность в верхнем регистре: {dna}")

count_A = dna.count("A")
count_T = dna.count("T")
count_G = dna.count("G")
count_C = dna.count("C")
length = len(dna)
percent_A = 100 * count_A / length
percent_T = 100 * count_T / length
percent_G = 100 * count_G / length
percent_C = 100 * count_C / length

print(f"\nПодсчёт нуклеотидов:")
print(f"A: {count_A}\nT: {count_T}\nG: {count_G}\nC: {count_C}")
print(f"\nОбщая длина: {length} нуклеотидов")
print(f"\nПроцентное содержание нуклеотидов в цепи:\nA: {percent_A:.1f}\nT: {percent_T:.1f}\nG: {percent_G:.1f}\nC: {percent_C:.1f}")