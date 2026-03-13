read -r -p "Введите массу (кг): " MASS
read -r -p "Введите рост (м): " HEIGHT
BMI=$((MASS / ($HEIGHT * $HEIGHT)))

echo "Индекс массы тела равен $BMI"
