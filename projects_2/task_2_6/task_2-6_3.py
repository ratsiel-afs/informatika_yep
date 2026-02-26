donor_phenotype = input("Введите фенотип группы крови донора (I, II, III, IV): ").strip().upper()
patient_phenotype = input("Введите фенотип группы крови пациента (I, II, III, IV): ").strip().upper()

if patient_phenotype == donor_phenotype or patient_phenotype == "IV" or donor_phenotype == "I":
    print("Переливание возможно")
else:
    print("Переливание НЕВОЗМОЖНО!")