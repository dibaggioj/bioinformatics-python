#!/usr/bin/env
# encoding: utf-8
"""
Created by John DiBaggio on 2016-11-30
Copyright (c) 2016 Inworks. All rights reserved.
"""

import sys
import os

argv = list(sys.argv)
input_file = open(argv[1])
output_file = open(argv[2], 'w+')

dna = input_file.read()
reverse_complement = ""

for basepair in dna[::-1]:
    if basepair == 'A':
        reverse_complement += 'T'
    elif basepair == 'T':
        reverse_complement += 'A'
    elif basepair == 'G':
        reverse_complement += 'C'
    elif basepair == 'C':
        reverse_complement += 'G'

output_file.write(reverse_complement)
output_file.close()
input_file.close()
