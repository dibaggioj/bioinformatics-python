#!/usr/bin/env
# encoding: utf-8
"""
Created by John DiBaggio on 2016-12-07
"""
__author__ = 'johndibaggio'

import sys
import time

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


# ~0.54 seconds / 500 times
def translate_rna_into_protein_1(rna_seq):
    codons = [rna_seq[i:i+CODON_LENGTH] for i in xrange(0, len(rna_seq), CODON_LENGTH)]
    protein_seq = ""

    for codon in codons:
        if codon in RNA_CODON_TABLE:
            amino_acid = RNA_CODON_TABLE.get(codon)
            if STOP != amino_acid:
                protein_seq += amino_acid
    return protein_seq


# ~0.79 seconds / 500 times
def translate_rna_into_protein_2(rna_seq):
    protein_seq = ""
    codon = ""
    counter = 0

    for nucleobase in rna_seq:
        counter += 1
        codon += nucleobase
        if counter == CODON_LENGTH:
            if codon in RNA_CODON_TABLE:
                amino_acid = RNA_CODON_TABLE.get(codon)
                if STOP != amino_acid:
                    protein_seq += amino_acid
            codon = ""
            counter = 0

    return protein_seq


protein = ""

time_start = time.time()
# for j in range(500):
#     protein = translate_rna_into_protein_1(rna)

protein = translate_rna_into_protein_1(rna)

time_end = time.time()
time_elapsed = time_end - time_start

print "RNA successfully translated in {} seconds".format(time_elapsed)

output_file.write(protein)

output_file.close()
input_file.close()
