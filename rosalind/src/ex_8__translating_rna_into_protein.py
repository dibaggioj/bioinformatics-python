#!/usr/bin/env
# encoding: utf-8
"""
Created by John DiBaggio on 2016-12-07
"""
__author__ = 'johndibaggio'

import sys
from decimal import Decimal

CODON_LENGTH = 3
STOP = "Stop"
RNA_CODON_TABLE = dict({"UUU": "F", "CUU": "L", "AUU": "I", "GUU": "V", "UUC": "F", "CUC": "L", "AUC": "I", "GUC": "V",
                        "UUA": "L", "CUA": "L", "AUA": "I", "GUA": "V", "UUG": "L", "CUG": "L", "AUG": "M", "GUG": "V",
                        "UCU": "S", "CCU": "P", "ACU": "T", "GCU": "A", "UCC": "S", "CCC": "P", "ACC": "T", "GCC": "A",
                        "UCA": "S", "CCA": "P", "ACA": "T", "GCA": "A", "UCG": "S", "CCG": "P", "ACG": "T", "GCG": "A",
                        "UAU": "Y", "CAU": "H", "AAU": "N", "GAU": "D", "UAC": "Y", "CAC": "H", "AAC": "N", "GAC": "D",
                        "UAA": "Stop", "CAA": "Q", "AAA": "K", "GAA": "E", "UAG": "Stop", "CAG": "Q", "AAG": "K",
                        "GAG": "E", "UGU": "C", "CGU": "R", "AGU": "S", "GGU": "G", "UGC": "C", "CGC": "R", "AGC": "S",
                        "GGC": "G", "UGA": "Stop", "CGA": "R", "AGA": "R", "GGA": "G", "UGG": "W", "CGG": "R",
                        "AGG": "R", "GGG": "G"})

argv = list(sys.argv)
input_file = open(argv[1], 'r+')
output_file = open(argv[2], 'w+')

rna = input_file.read()
codons = [rna[i:i+CODON_LENGTH] for i in xrange(0, len(rna), CODON_LENGTH)]
protein = ""

for codon in codons:
    if codon in RNA_CODON_TABLE:
        amino_acid = RNA_CODON_TABLE.get(codon)
        if STOP != amino_acid:
            protein += amino_acid

output_file.write(protein)

output_file.close()
input_file.close()
