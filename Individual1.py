#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from random import uniform


if __name__ == '__main__':
    morning = [uniform(0, 10) for _ in range(7)]
    day = [uniform(4, 15) for _ in range(7)]
    evening = [uniform(0, 7) for _ in range(7)]

    average_temp = [round(((m + d + e) / 3), 1) for m, d, e in zip(morning, day, evening)]

    print(average_temp)
