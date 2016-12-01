#!/usr/bin/env
# encoding: utf-8
"""
Created by John DiBaggio on 2016-11-30
Copyright (c) 2016 Inworks. All rights reserved.
"""

import sys
import os

dna = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"

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

print "DNA: " + dna
print "A: " + str(a_count)
print "C: " + str(c_count)
print "G: " + str(g_count)
print "T: " + str(t_count)