


# Задача №1
# Дан список целых чисел numbers. Необходимо написать в императивном стиле процедуру для
# сортировки числа в списке в порядке убывания. Можно использовать любой алгоритм сортировки.# Сортировка выбором


# 1. Императивная парадигма
def sort_list_imperative(numbers):
    n = len(numbers)
    for i in range(n):
        mx_ind = n - 1 - i
        for j in range(n - i):
            if numbers[j] > numbers[mx_ind]:
                mx_ind = j
        numbers[n - 1 - i], numbers[mx_ind] = numbers[mx_ind], numbers[n - 1 - i]
    return numbers
# 2. Декларативная парадигма
def sort_list_declarative(numbers):
    return sorted(numbers)

# Проверка работы программ

not_sorted_list = [1004, 3, 13, 8, 3, 77, 0, 1, 105]

print(sort_list_imperative(not_sorted_list))
print(sort_list_declarative(not_sorted_list))