#!/usr/bin/env
# encoding: utf-8
"""
Created by John DiBaggio on 2017-05-27
"""
__author__ = 'johndibaggio'

import sys
import fileinput


argv = list(sys.argv)
dna_strands_set = []
profile_matrix = [[], [], [], []]
shortest_strand_length = 0
consensus_string = ""


def init_dna_strands_set():
    """
    Builds an array of hashmaps of strand IDs and DNA strings, e.g.
    [
        {'id': 'Rosalind_1', 'strand': 'ATCCAGCT'},
        {'id': 'Rosalind_2', 'strand': 'GGGCAACT'},
        {'id': 'Rosalind_3', 'strand': 'ATGGATCT'},
        {'id': 'Rosalind_4', 'strand': 'AAGCAACC'},
        {'id': 'Rosalind_5', 'strand': 'TTGGAACT'},
        {'id': 'Rosalind_6', 'strand': 'ATGCCATT'},
        {'id': 'Rosalind_7', 'strand': 'ATGGCACT'}
    ]
    Sets `shortest_strand_length` to the length of the shortest DNA strand from the data
    """
    strand_index = -1
    for line in fileinput.input(argv[1]):
        if line.startswith('>'):
            data = dict()
            data["id"] = line.replace('>', '').replace('\n', '')
            data["strand"] = ""
            dna_strands_set.append(data)
            strand_index += 1
        elif len(dna_strands_set) == strand_index + 1:
            data = dna_strands_set[strand_index]
            data["strand"] += line.replace('\n', '')
            length = len(data["strand"])

    global shortest_strand_length
    shortest_strand_length
    for strand in dna_strands_set:
        length = len(strand["strand"])
        if 0 < length < shortest_strand_length:
            shortest_strand_length = length
        elif shortest_strand_length == 0:
            shortest_strand_length = length


def build_profile_matrix():
    """
    Builds a profile matrix of counts of base pairs from each DNA strand in `dna_strands_set` at each position, e.g.
    [
        [5, 1, 0, 0, 5, 5, 0, 0],
        [0, 0, 1, 4, 2, 0, 6, 1],
        [1, 1, 6, 3, 0, 1, 0, 0],
        [1, 5, 0, 0, 0, 1, 1, 6]
    ]
    """
    for strand in dna_strands_set:
        dna_string = strand.get("strand")
        for position in range(shortest_strand_length):
            base_pair = dna_string[position]
            if len(profile_matrix[0]) < position + 1:
                profile_matrix[0].append(0)
                profile_matrix[1].append(0)
                profile_matrix[2].append(0)
                profile_matrix[3].append(0)

            if base_pair == 'A':
                profile_matrix[0][position] += 1
            elif base_pair == 'C':
                profile_matrix[1][position] += 1
            elif base_pair == 'G':
                profile_matrix[2][position] += 1
            elif base_pair == 'T':
                profile_matrix[3][position] += 1

            position += 1


def build_first_consensus_string():
    """
    Builds consensus string from profile (alphabetically first in the case that there are multiple base pairs have the
    maximum frequency at a position
    :rtype: basestring
    :return: consensus string
    """
    for position in range(shortest_strand_length):
        base_pairs_at_position = [profile_matrix[0][position], profile_matrix[1][position], profile_matrix[2][position],
                                  profile_matrix[3][position]]
        most_freq_index = base_pairs_at_position.index(max(base_pairs_at_position))
        global consensus_string
        if most_freq_index == 0:
            consensus_string += 'A'
        elif most_freq_index == 1:
            consensus_string += 'C'
        elif most_freq_index == 2:
            consensus_string += 'G'
        elif most_freq_index == 3:
            consensus_string += 'T'


def profile_matrix_to_string(p_matrix):
    """
    :param p_matrix profile matrix
    :rtype: basestring
    :return: string representation of profile matrix, e.g.,
    A: 5 1 0 0 5 5 0 0
    C: 0 0 1 4 2 0 6 1
    G: 1 1 6 3 0 1 0 0
    T: 1 5 0 0 0 1 1 6
    """
    p_matrix_str = ""
    base_pair_index = 0
    for base_pair_positions in p_matrix:
        print(base_pair_positions)
        if base_pair_index == 0:
            p_matrix_str += 'A:'
        elif base_pair_index == 1:
            p_matrix_str += 'C:'
        elif base_pair_index == 2:
            p_matrix_str += 'G:'
        elif base_pair_index == 3:
            p_matrix_str += 'T:'

        for pos_freq in base_pair_positions:
            p_matrix_str += ' ' + str(pos_freq)

        p_matrix_str += '\n'
        base_pair_index += 1

    return p_matrix_str


def write_output():
    output_file = open(argv[2], 'w+')
    output_file.write(consensus_string + '\n')
    output_file.write(profile_matrix_to_string(profile_matrix))
    output_file.close()


init_dna_strands_set()
build_profile_matrix()
build_first_consensus_string()
write_output()
