__author__ = 'johndibaggio'

from abc import ABCMeta


class BioUtil:
    __metaclass__ = ABCMeta

    def __init__(self):
        """
        Empty __init__
        """

    @staticmethod
    def symbol_to_number(symbol):
        if symbol == 'A':
            return 0
        elif symbol == 'C':
            return 1
        elif symbol == 'G':
            return 2
        elif symbol == 'T':
            return 3
        return 0

    @staticmethod
    def number_to_symbol(index):
        if index == 0:
            return 'A'
        elif index == 1:
            return 'C'
        elif index == 2:
            return 'G'
        elif index == 3:
            return 'T'
        return ''

    @staticmethod
    def pattern_to_number(pattern):
        if pattern is None or len(pattern) == 0:
            return 0
        last_symbol = pattern[-1:]
        prefix = pattern[:-1]
        return 4 * BioUtil.pattern_to_number(prefix) + BioUtil.symbol_to_number(last_symbol)

    @staticmethod
    def number_to_pattern(index, k):
        if k == 1:
            return BioUtil.number_to_symbol(index)
        prefix_index = index // 4
        r = index % 4
        symbol = BioUtil.number_to_symbol(r)
        prefix_pattern = BioUtil.number_to_pattern(prefix_index, k - 1)
        return prefix_pattern + symbol

BioUtil.register(tuple)

assert issubclass(tuple, BioUtil)
assert isinstance((), BioUtil)
