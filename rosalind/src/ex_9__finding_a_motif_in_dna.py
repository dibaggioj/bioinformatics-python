#!/usr/bin/env
# encoding: utf-8
"""
Created by John DiBaggio on 2017-05-25
"""
__author__ = 'johndibaggio'

import sys

argv = list(sys.argv)
output_file = open(argv[2], 'w+')
dna_strand_s = ""
dna_strand_t = ""

with open(argv[1]) as f:
    lines = f.readlines()
    if len(lines) >= 2:
        dna_strand_s = lines[0].replace('\n', '')
        dna_strand_t = lines[1].replace('\n', '')
    else:
        print("There was an error with the data file")


def get_next_index(indices, strand_s, strand_t, start):
    index = dna_strand_s.find(dna_strand_t, start)
    if index > -1:
        indices.append(index + 1)
        get_next_index(indices, strand_s, strand_t, index + 1)


def get_indices(strand_s, strand_t):
    indices = []
    get_next_index(indices, strand_s, strand_t, 0)
    return indices


def indices_as_string(indices):
    indices_str = ""
    for i in indices:
        indices_str += str(i) + " "
    if len(indices_str) > 1:
        indices_str = indices_str[:-1]
    return indices_str


locations = indices_as_string(get_indices(dna_strand_s, dna_strand_t))
print("All locations of t as a substring of s:\n" + locations)

output_file.write(locations)
output_file.close()
