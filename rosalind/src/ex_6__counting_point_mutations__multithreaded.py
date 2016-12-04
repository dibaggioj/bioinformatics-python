#!/usr/bin/env
# encoding: utf-8
"""
Created by John DiBaggio on 2016-12-03
"""
__author__ = 'johndibaggio'

import sys
import thread
import threading
import time

STRAND_LENGTH = 500

argv = list(sys.argv)
output_file = open(argv[2], 'w+')

exit_flag = 0
strand_1 = None
strand_2 = None

with open(argv[1], 'r') as f:
    strands = f.readlines()

if len(strands) >= 2:
    strand_1 = strands[0].replace('\n', '')
    strand_2 = strands[1].replace('\n', '')


class HammingThread(threading.Thread):
    def __init__(self, id, s1, s2):
        threading.Thread.__init__(self)
        self.id = id
        self.s1 = s1
        self.s2 = s2
        self.name = "Thread-" + str(id)
        self.h_dist = 0

    def run(self):
        print "Starting " + self.name
        self.h_dist = calc_hamming_distance_threaded(self.name, self.s1, self.s2)
        print "%s Hamming distance: %d" % (self.name, self.h_dist)
        print "Exiting " + self.name

    def get_h_dist(self):
        return self.h_dist


def calc_hamming_distance_threaded(thread_name, s1, s2):
    if exit_flag:
        thread_name.exit()
    print "%s: %s" % (thread_name, time.ctime(time.time()))

    if s1 is None or s2 is None or len(s1) != len(s2):
        raise ValueError("Both strands must not be empty and must be of equal length.")

    h_dist = 0
    for index, n_base in enumerate(s1):
        if n_base != s2[index]:
            h_dist += 1
    return h_dist


def calc_hamming_distance(s1, s2):
    if s1 is None or s2 is None or len(s1) != len(s2):
        raise ValueError("Both strands must not be empty and must be of equal length.")

    s1_segments = [s1[i:i+STRAND_LENGTH] for i in xrange(0, len(s1), STRAND_LENGTH)]
    s2_segments = [s2[i:i+STRAND_LENGTH] for i in xrange(0, len(s2), STRAND_LENGTH)]
    h_threads = []

    for index, s1_segment in enumerate(s1_segments):
        try:
            h_threads.append(HammingThread(index, s1_segment, s2_segments[index]))
        except:
            print "Error: unable to start thread"

    for h_thread in h_threads:
        h_thread.start()

    # TODO: synchronize threads

    h_dist = 0
    for h_thread in h_threads:
        h_dist += h_thread.get_h_dist()

    return h_dist

try:
    time_start = time.time()

    hamming_distance = calc_hamming_distance(strand_1, strand_2)

    time_end = time.time()
    time_elapsed = time_end - time_start
    print "Hamming distance is {}. Calculated in {} seconds".format(str(hamming_distance), time_elapsed)
    output_file.write(str(hamming_distance))
except ValueError:
    print "ValueError thrown while calculating Hamming distance for strands:\n{}\n{}".format(strand_1, strand_2)
    output_file.write("ValueError thrown while calculating Hamming distance for strands:\n{}\n{}".format(strand_1,
                                                                                                         strand_2))
finally:
    output_file.close()
