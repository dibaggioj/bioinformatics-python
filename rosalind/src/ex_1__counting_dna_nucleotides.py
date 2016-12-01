#!/usr/bin/env
# encoding: utf-8
"""
Created by John DiBaggio on 2016-11-30
Copyright (c) 2016 Inworks. All rights reserved.
"""

import sys
import os
# from collections import defaultdict

# groups = defaultdict(int)
argv = list(sys.argv)
input_file = open(argv[1])
output_file = open(argv[2], 'w+')
dna = input_file.read()

a_count = 0
c_count = 0
g_count = 0
t_count = 0

for basepair in dna:
    if basepair == 'A':
        a_count += 1
    elif basepair == 'C':
        c_count += 1
    elif basepair == 'G':
        g_count += 1
    elif basepair == 'T':
        t_count += 1

output_file.write("DNA: " + dna + "\nA: " + str(a_count) + "\nC: " + str(c_count) + "\nG: " + str(g_count) + "\nT: " + str(t_count))
