# ● Контекст
# Корреляция - статистическая мера, используемая для оценки связи между двумя случайными величинами.
# ● Ваша задача
# Написать скрипт для расчета корреляции Пирсона между двумя случайными величинами (двумя массивами). 
# Можете использовать любую парадигму, но рекомендую использовать функциональную, т.к. в этом примере она значительно упростит вам жизнь.


from functools import reduce
import math

def pearson_correlation(x, y):
    n = len(x)

    # Среднее значение
    mean_x = reduce(lambda a, b: a + b, x) / n
    mean_y = reduce(lambda a, b: a + b, y) / n

    # Ковариация
    covariance = sum((xi - mean_x) * (yi - mean_y) for xi, yi in zip(x, y)) / n

    # Стандартное отклонение
    std_dev_x = math.sqrt(sum((xi - mean_x) ** 2 for xi in x) / n)
    std_dev_y = math.sqrt(sum((yi - mean_y) ** 2 for yi in y) / n)

    # Корреляция
    correlation = covariance / (std_dev_x * std_dev_y)
    return correlation

# Пример использования
array1 = [7, 6, 5, 4, 4]
array2 = [12, 11, 7, 5, 1]

correlation = pearson_correlation(array1, array2)
print(f"Корреляция: {correlation}")


# Функция pearson_correlation использует функции reduce, zip и math.sqrt, чтобы вычислить корреляцию Пирсона между двумя массивами.