#!/bin/bash

echo "Сумма оценок: "
awk '{sum += $2} END {print sum}' students.txt
echo "Среднее значение: "
awk '{sum += $2; n++} END {print sum/n}' students.txt
echo "Максимальное значение: "
awk 'NR==1{max=$2} $2>max{max=$2} END {print max}' students.txt

