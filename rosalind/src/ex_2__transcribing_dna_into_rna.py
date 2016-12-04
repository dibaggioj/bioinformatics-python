#!/usr/bin/env
# encoding: utf-8
"""
Created by John DiBaggio on 2016-11-30
"""
__author__ = 'johndibaggio'

import sys
import os

argv = list(sys.argv)
input_file = open(argv[1])
output_file = open(argv[2], 'w+')

dna = input_file.read()
rna = ""

for nucleobase in dna:
    if nucleobase == 'T':
        rna += "U"
    else:
        rna += nucleobase

# rna = dna.replace("T", "U")

output_file.write(rna)
output_file.close()
input_file.close()
