#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from functools import reduce
from random import uniform


if __name__ == '__main__':
    my_list = [round(uniform(-10, 10), 2) for _ in range(7)]

    # Отфильтровываем все значения, которые больше нуля, а затем функцией reduce складываем полученные значения
    Sum = reduce(lambda x, y: x + y, filter(lambda x: x <= 0, my_list))

    # Определить индексы минимального и максимального элементов.
    a_min = a_max = my_list[0]
    i_min = i_max = 0
    for i, item in enumerate(my_list):
        if item < a_min:
            i_min, a_min = i, item
        
        if item >= a_max:
            i_max, a_max = i, item

    # Проверить индексы и обменять их местами.
    if i_min > i_max:
        i_min, i_max = i_max, i_min

    Mult = reduce(lambda x, y: x * y, my_list[i_min:i_max+1])

    print("Исходный список: " + " ".join(map(lambda x: str(x), my_list)))
    print(f"Сумма всех отрицательных элементов списка: {Sum}")
    print(f"Произведение элементов списка между максимальным и минимальным элементами: {Mult}")
