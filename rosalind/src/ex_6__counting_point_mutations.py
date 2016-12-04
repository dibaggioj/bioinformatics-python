#!/usr/bin/env
# encoding: utf-8
"""
Created by John DiBaggio on 2016-12-03
"""
__author__ = 'johndibaggio'

import sys
import time

argv = list(sys.argv)
output_file = open(argv[2], 'w+')

strand_1 = None
strand_2 = None

with open(argv[1], 'r') as f:
    strands = f.readlines()

if len(strands) >= 2:
    strand_1 = strands[0].replace('\n', '')
    strand_2 = strands[1].replace('\n', '')


def calc_hamming_distance(s1, s2):
    if s1 is None or s2 is None or len(s1) != len(s2):
        raise ValueError("Both strands must not be empty and must be of equal length.")
    h_dist = 0
    for index, n_base in enumerate(s1):
        if n_base != s2[index]:
            h_dist += 1
    return h_dist

try:
    time_start = time.time()

    hamming_distance = calc_hamming_distance(strand_1, strand_2)

    time_end = time.time()
    time_elapsed = time_end - time_start
    print "Hamming distance is {}. Calculated in {} seconds".format(str(hamming_distance), time_elapsed)
    output_file.write(str(hamming_distance))
except ValueError:
    print "ValueError thrown while calculating Hamming distance for strands:\n{}\n{}".format(strand_1, strand_2)
    output_file.write("ValueError thrown while calculating Hamming distance for strands:\n{}\n{}".format(strand_1,
                                                                                                         strand_2))
finally:
    output_file.close()
