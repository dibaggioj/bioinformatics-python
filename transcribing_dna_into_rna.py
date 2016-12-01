#!/usr/bin/env
# encoding: utf-8
"""
Created by John DiBaggio on 2016-11-30
Copyright (c) 2016 Inworks. All rights reserved.
"""

import sys
import os

dna = "GATGGAACTTGACTACGTAAATT"
rna = ""

# for basepair in dna:
#     if basepair == 'T':
#     	rna += "U"
#     else:
#     	rna += basepair

rna = dna.replace("T", "U")

print "DNA: " + dna
print "RNA: " + rna
