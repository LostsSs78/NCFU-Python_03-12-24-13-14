#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from random import uniform


if __name__ == '__main__':
    morning = [uniform(0, 10) for i in range(7)]
    day = [uniform(4, 15) for i in range(7)]
    evening = [uniform(0, 7) for i in range(7)]

    average_temp = [round(((morning[i] + day[i] + evening[i]) / 3), 1) for i in range(len(morning))]

    print(average_temp)
