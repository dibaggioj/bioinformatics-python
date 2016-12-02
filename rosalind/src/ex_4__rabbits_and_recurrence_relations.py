#!/usr/bin/env
# encoding: utf-8
"""
Created by John DiBaggio on 2016-11-30
Copyright (c) 2016 Inworks. All rights reserved.
"""

import sys
import time
from math import sqrt
from decimal import Decimal

argv = list(sys.argv)
input_file = open(argv[1], 'r+')
output_file = open(argv[2], 'w+')

conditions = input_file.read().split(" ")

n = int(conditions[0])
k = int(conditions[1])


def calc_rabbit_pairs_linear_recurrence(month_n, multiplier):
    """
    Calculate number of rabbit pairs after month `month_n` with `multiplier` pairs produced per litter, using the linear
    -recurrence expression (slower)

    :type month_n: int
    :param month_n: nth month_n after which point we want to know the number of rabbit pairs

    :type multiplier: int
    :param multiplier: number of rabbit pairs produced per litter

    :rtype: int
    :return: number of rabbit pairs after
    """
    if month_n == 0:
        return 0
    elif month_n == 1:
        return 1
    else:
        return calc_rabbit_pairs_linear_recurrence(month_n - 1, multiplier) + multiplier * calc_rabbit_pairs_linear_recurrence(month_n - 2, multiplier)


def calc_rabbit_pairs_closed_form(month_n, multiplier):
    """
    Calculate number of rabbit pairs after month `month_n` with `multiplier` pairs produced per litter, using the closed
    -form expression (faster)

    :type month_n: int
    :param month_n: nth month_n after which point we want to know the number of rabbit pairs

    :type multiplier: int
    :param multiplier: number of rabbit pairs produced per litter

    :rtype: int
    :return: number of rabbit pairs after
    """
    alpha = Decimal(calc_quad_root(1, multiplier, True))
    beta = Decimal(calc_quad_root(1, multiplier, False))
    answer = (alpha ** month_n - beta ** month_n) / (alpha - beta)
    return answer.to_integral_value()


def calc_quad_root(a, b, plus):
    quad_a = 1
    quad_b = - a
    quad_c = - b
    if plus:
        return (-quad_b + sqrt(quad_b ** 2 - 4 * quad_a * quad_c)) / (2 * quad_a)
    return (-quad_b - sqrt(quad_b ** 2 - 4 * quad_a * quad_c)) / (2 * quad_a)


time_start = time.time()

rabbit_pair_count = calc_rabbit_pairs_closed_form(n, k)

time_end = time.time()
time_elapsed = time_end - time_start

print "{} rabbit pairs after {} months with {} pairs per litter. Calculated in {} seconds".format(
    rabbit_pair_count, n, k, time_elapsed)

output_file.write(str(rabbit_pair_count))
