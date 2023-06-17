# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума

min = int(input())
max = int(input())

array = list(input().split())
array_int = [int(x) for x in array]
index = []
for i in range(len(array)):
    if array_int[i] <= max and array_int[i] >= min:
        index.append(i)
print(index)
