#!/usr/bin/env
# encoding: utf-8
"""
Created by John DiBaggio on 2017-05-27
"""
__author__ = 'johndibaggio'

import sys
import fileinput


BASE_PAIR_SET = ['A', 'C', 'G', 'T']

argv = list(sys.argv)
strands_collection = []
contained_kmers = ['']
longest_kmer_found = False


def init_strands_set():
    """
    From a FASTA-formatted file argv[1] builds an array of hashmaps of DNA strand IDs and strings, e.g.
    [
        {'id': 'Rosalind_1', 'string': 'ATCCAGCT'},
        {'id': 'Rosalind_2', 'string': 'GGGCAACT'},
        {'id': 'Rosalind_3', 'string': 'ATGGATCT'},
        {'id': 'Rosalind_4', 'string': 'AAGCAACC'},
        {'id': 'Rosalind_5', 'string': 'TTGGAACT'},
        {'id': 'Rosalind_6', 'string': 'ATGCCATT'},
        {'id': 'Rosalind_7', 'string': 'ATGGCACT'}
    ]
    Sets `shortest_strand_length` to the length of the shortest DNA strand from the data
    """
    strand_index = -1
    for line in fileinput.input(argv[1]):
        if line.startswith('>'):
            data = dict()
            data["id"] = line.replace('>', '').replace('\n', '')
            data["string"] = ""
            strands_collection.append(data)
            strand_index += 1
        elif len(strands_collection) == strand_index + 1:
            data = strands_collection[strand_index]
            data["string"] += line.replace('\n', '')
            length = len(data["string"])


def strands_contain_substring(substring):
    for strand in strands_collection:
        if strand["string"].find(substring) < 0:
            return False
    return True


def get_longest_common_substring():
    global contained_kmers
    global longest_kmer_found

    contained_longer_kmers = []

    for kmer in contained_kmers:
        for base_pair in BASE_PAIR_SET:
            longer_kmer = kmer + base_pair
            # print("Checking kmer: " + longer_kmer)
            if strands_contain_substring(longer_kmer):
                contained_longer_kmers.append(longer_kmer)

    if len(contained_longer_kmers) > 0:     # Try to motif of larger k
        contained_kmers = contained_longer_kmers
        return get_longest_common_substring()
    else:                                   # No motif of larger k found, so return the previous longest
        longest_kmer_found = True
        if len(contained_kmers) > 0:
            return contained_kmers[0]
        print("No shared motif found!")
        return None


init_strands_set()

longest_common_substring = get_longest_common_substring()

print(longest_common_substring)

output_file = open(argv[2], 'w+')
output_file.write(longest_common_substring)
output_file.close()
