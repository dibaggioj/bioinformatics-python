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

dna_sequence = Seq(dna, IUPAC.unambiguous_dna)

rna = dna_sequence.transcribe()

output_file.write(str(rna))
output_file.close()
input_file.close()
