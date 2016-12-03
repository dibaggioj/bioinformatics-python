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

memo = {}


def calc_rabbit_pairs_linear_recurrence(month_n, multiplier):
    """
    Calculate number of rabbit pairs after month `month_n` with `multiplier` pairs produced per litter, using the linear
    -recurrence expression (slow)

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
        return calc_rabbit_pairs_linear_recurrence(month_n - 1, multiplier) \
            + multiplier * calc_rabbit_pairs_linear_recurrence(month_n - 2, multiplier)


def calc_rabbit_pairs_linear_recurrence_dynamic(month_n, multiplier=1):
    """
    Calculate number of rabbit pairs after month `month_n` with `multiplier` pairs produced per litter, using dynamic
    programming (faster) - memorization, by storing answers computed for conditions and then reusing those answers for
    the same conditions rather than recomputed them

    :type month_n: int
    :param month_n: nth month_n after which point we want to know the number of rabbit pairs

    :type multiplier: int
    :param multiplier: number of rabbit pairs produced per litter

    :rtype: int
    :return: number of rabbit pairs after
    """
    args = (month_n, multiplier)
    if args in memo:
        return memo[args]  # Use previously computed value for conditions

    # Compute value for new conditions
    if month_n == 1:
        ans = 1
    elif month_n == 2:
        ans = 1
    else:
        ans = calc_rabbit_pairs_linear_recurrence_dynamic(month_n-1, multiplier) \
            + multiplier * calc_rabbit_pairs_linear_recurrence_dynamic(month_n-2, multiplier)
    memo[args] = ans  # Store the computed value for new conditions
    return ans


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
    answer = (pow(alpha, month_n) - pow(beta,  month_n)) / (alpha - beta)
    return answer.to_integral_value()


def calc_rabbit_pairs_loop(month_n, multiplier):
    """
    Calculate number of rabbit pairs after month `month_n` with `multiplier` pairs produced per litter, using an
    loop/enumeration (fastest)

    :type month_n: int
    :param month_n: nth month_n after which point we want to know the number of rabbit pairs

    :type multiplier: int
    :param multiplier: number of rabbit pairs produced per litter

    :rtype: int
    :return: number of rabbit pairs after
    """
    previous1, previous2 = 1, 1
    current = 0
    for i in range(2, month_n):
        current = previous1 + multiplier * previous2
        previous2 = previous1
        previous1 = current
    return current


def calc_quad_root(a, b, plus):
    quad_a = 1
    quad_b = - a
    quad_c = - b
    if plus:
        return (-quad_b + sqrt(pow(quad_b, 2) - 4 * quad_a * quad_c)) / (2 * quad_a)
    return (-quad_b - sqrt(pow(quad_b, 2) - 4 * quad_a * quad_c)) / (2 * quad_a)


time_start = time.time()

rabbit_pair_count = calc_rabbit_pairs_linear_recurrence_dynamic(n, k)

time_end = time.time()
time_elapsed = time_end - time_start

print "{} rabbit pairs after {} months with {} pairs per litter. Calculated in {} seconds".format(
    rabbit_pair_count, n, k, time_elapsed)

output_file.write(str(rabbit_pair_count))
output_file.close()
input_file.close()