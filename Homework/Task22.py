# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа,
# которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества.
# m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

n = int(input("Введите число n: "))
m = int(input("Введите число m: "))
print("Вводите элементы первого множества")
numbers1 = []
for i in range(n):
    numbers1.append(int(input()))
print("Вводите элементы второго множества")
numbers2 = []
for i in range(m):
    numbers2.append(int(input()))
numbers1 = set(numbers1)
numbers2 = set(numbers2)
result = numbers1.intersection(numbers2)
print(*sorted(result))