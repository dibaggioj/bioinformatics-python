#!/usr/bin/env
# encoding: utf-8
"""
Created by John DiBaggio on 2017-05-27
"""
__author__ = 'johndibaggio'

import sys
import fileinput

from lib.bio_util import BioUtil


MAX_K = 100

argv = list(sys.argv)
strands_collection = []


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


def strands_contain_a_kmer(k):
    for index in range(0, 4 ** k - 1):
        if strands_contain_substring(BioUtil.number_to_pattern(index, k)):
            return True
    return False


def get_lexicographically_first_kmer(k):
    for index in range(0, 4 ** k - 1):
        pattern = BioUtil.number_to_pattern(index, k)
        # print("Checking pattern: " + pattern)
        if strands_contain_substring(pattern):
            return pattern
    return None


def get_longest_common_substring():
    substring = ""
    found = True
    k = 2
    while found and k < MAX_K:
        next_substring = get_lexicographically_first_kmer(k)
        k += 1
        if next_substring is not None:
            substring = next_substring
            print("Current longest motif: " + substring)
        else:
            found = False

    return substring


init_strands_set()

longest_common_substring = get_longest_common_substring()

print(longest_common_substring)

output_file = open(argv[2], 'w+')
output_file.write(longest_common_substring)
output_file.close()
