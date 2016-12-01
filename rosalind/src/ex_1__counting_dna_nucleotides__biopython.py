#!/usr/bin/env
# encoding: utf-8
"""
Created by John DiBaggio on 2016-11-30
Copyright (c) 2016 Inworks. All rights reserved.
"""

import sys
import os
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

argv = list(sys.argv)
input_file = open(argv[1])
output_file = open(argv[2], 'w+')

dna = input_file.read()

dna_sequence = Seq(dna, IUPAC.unambiguous_rna)

a_count = dna_sequence.count("A")
c_count = dna_sequence.count("C")
g_count = dna_sequence.count("G")
t_count = dna_sequence.count("T")

output_file.write("DNA: " + dna + "\nA: " + str(a_count) + "\nC: " + str(c_count) + "\nG: " + str(g_count) + "\nT: " + str(t_count))
