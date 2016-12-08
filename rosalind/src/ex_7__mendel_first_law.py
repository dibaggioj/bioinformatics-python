#!/usr/bin/env
# encoding: utf-8
"""
Created by John DiBaggio on 2016-12-07
"""
__author__ = 'johndibaggio'

import sys
from decimal import Decimal
from decimal import ROUND_UP

DECIMAL_ONE_HALF = Decimal(1) / Decimal(2)
DECIMAL_THREE_FOURTHS = Decimal(3) / Decimal(4)

argv = list(sys.argv)
input_file = open(argv[1], 'r+')
output_file = open(argv[2], 'w+')

conditions = input_file.read().split(" ")

"""
k individuals are homozygous dominant for a factor,
m are heterozygous, and
n are homozygous recessive.
"""

k = int(conditions[0])
m = int(conditions[1])
n = int(conditions[2])

total = k + m + n

prob_dominant_allele = (Decimal(k) / total) * (Decimal(k - 1) / (total - 1))\
    + (Decimal(k) / total) * (Decimal(m) / (total - 1))\
    + (Decimal(k) / total) * (Decimal(n) / (total - 1))\
    + (Decimal(m) / total) * (Decimal(m - 1) / (total - 1)) * DECIMAL_THREE_FOURTHS\
    + (Decimal(m) / total) * (Decimal(n) / (total - 1)) * DECIMAL_ONE_HALF\
    + (Decimal(m) / total) * (Decimal(k) / (total - 1))\
    + (Decimal(n) / total) * (Decimal(k) / (total - 1))\
    + (Decimal(n) / total) * (Decimal(m) / (total - 1)) * DECIMAL_ONE_HALF\
    + (Decimal(n) / total) * (Decimal(n - 1) / (total - 1)) * 0

answer = prob_dominant_allele.quantize(Decimal('0.00001'), rounding=ROUND_UP).to_eng_string()

output_file.write(answer)

output_file.close()
input_file.close()
