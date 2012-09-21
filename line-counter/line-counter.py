#!/usr/bin/env python
# -*- coding: utf-8 *-*

"""
    Line-Counter compare the lines number of two files
"""

from sys import argv
from sys import exit


def line_counter(file_):
    line_file = open(file_, 'r')
    line_number = 0

    for line in line_file.readlines():
        line_number += 1

    line_file.close()
    return line_number


def show_results(total, rest):
    print '\nRESULTS'
    print '=' * 50
    print '\tTotal number of lines: %i' % (total)
    print '\tLines terminated: %i' % (total - rest)
    print '\tNumber of lines rest: %i' % (rest)


def helper():
    print 'Instructions for use: python line_counter.py [total_line_file]\
    [rest_line_file]'


def start():
    if argv[1] == '--help':
        helper()
        exit()

    if len(argv) >= 3:
        try:
            if argv[1] is not None and argv[2] is not None:
                show_results(line_counter(argv[1]), line_counter(argv[2]))
        except IndexError:
            print 'Incorrect arguments! see the help \'--help\''
    else:
        print 'Missing an argument, see the help \'--help\''


if __name__ == '__main__':
    start()
