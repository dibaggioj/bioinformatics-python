#!/usr/bin/env
# encoding: utf-8
"""
Created by John DiBaggio on 2017-06-22

Prints a message like the following:
417929742755482295 rabbit pairs after 86 months with 1 pairs produced per litter from rabbits of age 2+ months and
rabbits dying after 18 months. Calculated in 0.000448942184448 seconds

"""
__author__ = 'johndibaggio'

import sys
import time

argv = list(sys.argv)
input_file = open(argv[1], 'r+')
output_file = open(argv[2], 'w+')

conditions = input_file.read().split(" ")

n = int(conditions[0])
k = 1
m = int(conditions[1])

memo = {}


def calc_rabbit_pairs(month_n, months_death, multiplier=1):
    rabbits_next = calc_rabbit_pairs_linear_recurrence_dynamic(month_n, months_death, multiplier)
    total_rabbits = 0
    for rabbits_month_i in rabbits_next:
        total_rabbits += rabbits_month_i
    return total_rabbits


def calc_rabbit_pairs_linear_recurrence_dynamic(month_n, months_death, multiplier=1):
    """
    Calculate number of rabbit pairs after month `month_n` with `multiplier` pairs produced per litter, using dynamic
    programming (faster) - memorization, by storing answers computed for conditions and then reusing those answers for
    the same conditions rather than recomputed them

    :type month_n: int
    :param month_n: nth month_n after which point we want to know the number of rabbit pairs

    :type multiplier: int
    :param multiplier: number of rabbit pairs produced per litter

    :rtype: array
    :return: array, numbers of pairs of rabbits of age 0 months, 1 month, ... n-1 months
    """

    args = (month_n, multiplier)
    if args in memo:
        print('using data store')
        return memo[args]  # Use previously computed value for conditions

    rabbits_current = [0] * months_death

    # Compute value for new conditions
    if month_n == 1:    # new baby rabbit pair
        rabbits_current[0] = 1
        # print('current:')
        # print(rabbits_current)
        ans = rabbits_current
    # elif month_n == 2:  # new mature rabbit pair (will produce offspring in subsequent months)
    #     rabbits_current[1] = 1
    #     ans = rabbits_current
    else:
        rabbits_prev = calc_rabbit_pairs_linear_recurrence_dynamic(month_n-1, months_death, multiplier)
        # print('\nprevious:')
        # print(rabbits_prev)
        rabbits_current[1] = rabbits_prev[0]
        rabbits_current[0] += multiplier * rabbits_prev[months_death - 1]   # produce offspring from oldest rabbits
        for i in range(1, months_death - 1):                                   # kill off oldest rabbits
            rabbits_current[i + 1] = rabbits_prev[i]                           # age the mature rabbits by 1 month
            rabbits_current[0] += multiplier * rabbits_current[i + 1]          # produce offspring from mature rabbits
        # print('current:')
        # print(rabbits_current)
        ans = rabbits_current

    memo[args] = ans  # Store the computed value for new conditions

    return ans


time_start = time.time()

rabbit_pair_count = calc_rabbit_pairs(n, m, k)

time_end = time.time()
time_elapsed = time_end - time_start

print "{} rabbit pairs after {} months with {} pairs produced per litter from rabbits of age 2+ months and rabbits " \
      "dying after {} months. Calculated in {} seconds".format(rabbit_pair_count, n, k, m, time_elapsed)

output_file.write(str(rabbit_pair_count))
output_file.close()
input_file.close()