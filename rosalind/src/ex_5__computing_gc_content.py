#!/usr/bin/env
# encoding: utf-8
"""
Created by John DiBaggio on 2016-11-30
"""

import sys
import fileinput
from decimal import Decimal
from decimal import ROUND_UP

DECIMAL_100 = Decimal(100)

argv = list(sys.argv)
output_file = open(argv[2], 'w+')
strand_index = -1
strand_highest_gc = None
data_set = []


def calc_gc_content(strand):
    strand = strand.strip()
    if len(strand) == 0:
        raise ValueError("Strand cannot be empty")
    gc_count = strand.count("G") + strand.count("C")
    gc_percent = DECIMAL_100 * Decimal(gc_count) / Decimal(len(strand))
    return gc_percent.quantize(Decimal('0.000001'), rounding=ROUND_UP)

for line in fileinput.input(argv[1]):
    if line.startswith('>'):
        data = dict()
        data["id"] = line.replace('>', '').replace('\n', '')
        data["strand"] = ""
        data_set.append(data)
        strand_index += 1
    else:
        data = data_set[strand_index]
        data["strand"] += line.replace('\n', '')

for data in data_set:
    try:
        data["gc"] = calc_gc_content(data["strand"])
        if strand_highest_gc is None or "gc" not in strand_highest_gc:
            strand_highest_gc = data
        elif "gc" in data and "gc" in strand_highest_gc and data["gc"] > strand_highest_gc["gc"]:
            strand_highest_gc = data
    except ValueError:
        print "Unable to calculate GC content of strand " + data["id"]


print strand_highest_gc

if strand_highest_gc is not None:
    output_file.write(strand_highest_gc["id"] + '\n')
    output_file.write(strand_highest_gc["gc"].to_eng_string())

output_file.close()
