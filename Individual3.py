#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from functools import reduce
from random import uniform


if __name__ == '__main__':
    january = tuple([round(uniform(0, 110), 2) for _ in range(31)])
    march = tuple([round(uniform(0, 110), 2) for _ in range(31)])
    variants = ["в январе", "в марте"]

    rain_for_january = reduce(lambda x, y: x + y, january)
    rain_for_march = reduce(lambda x, y: x + y, march)

    print(f"Осадков выпало в январе: {rain_for_january}")
    print(f"Осадков выпало в марте: {rain_for_march}")
    print(f"Осадков выпало больше {variants[rain_for_january < rain_for_march]}")
