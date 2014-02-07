#!/usr/bin/env python

__author__ = 'Ed Epstein'

import re
import os
import argparse

expression = re.compile('^log_file_paths')


def pair_exists(pair, configfile):
    fh = open(configfile, 'r')
    lines = fh.readlines()
    fh.close()
    line = filter(lambda l: expression.search(l), lines)
    if len(line) == 1:
        return re.search(pair, line[0])


def insert_pair(pair, configfile):
    fh = open(configfile, 'r+')
    lines = fh.readlines()

    def sub_line(line):
        if expression.search(line):
            if line.rstrip().endswith('='):
                return line.rstrip() + " " + pair + ','
            else:
                return line.rstrip() + pair + ','
        else:
            return line

    updated_lines = map(sub_line, lines)
    fh.seek(0)
    fh.writelines(updated_lines)
    fh.close()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('collectorconfigfile', help="A path to the file that contains the collector config.")
    parser.add_argument('logpair', help="A string of the form name:path to specify the log name and path to be added.")
    args = parser.parse_args()
    if os.path.exists(args.collectorconfigfile):
        if not pair_exists(args.logpair, args.collectorconfigfile):
            insert_pair(args.logpair, args.collectorconfigfile)


if __name__ == '__main__':
    main()