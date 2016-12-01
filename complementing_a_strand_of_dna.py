#!/usr/bin/env
# encoding: utf-8
"""
Created by John DiBaggio on 2016-11-30
Copyright (c) 2016 Inworks. All rights reserved.
"""

import sys
import os

dna = "AAAACCCGGT"
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

print "DNA: " + dna
print "Reverse Complement: " + reverse_complement
