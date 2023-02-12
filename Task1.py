# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа,
# которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества.
# m - кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.
# Пример:
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12

first_length = int(input('Введите кол-во элементов первого множества: '))
first_list = []
for i in range(1, first_length + 1):
    num = int(input(f'Введите значение {i} элемента: '))
    first_list.append(num)
print(first_list)

second_length = int(input('Введите кол-во элементов второго множества: '))
second_list = []
for i in range(1, second_length + 1):
    num = int(input(f'Введите значение {i} элемента: '))
    second_list.append(num)
print(second_list)

result_list = []

for i in range(first_length):
    for n in range(second_length):
        if first_list[i] == second_list[n]:
            result_list.append(first_list[i])

result_list.sort()
temp_list = []
for num in result_list:
    if num not in temp_list:
        temp_list.append(num)
result_list = temp_list

print(result_list)
