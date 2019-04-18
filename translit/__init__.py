#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Transliteration Tool
#
# @author Loreto at gmail dot com
# Copyright (c) 2019 Loreto Parisi
#

import codecs
import sys  
reload(sys)  
sys.setdefaultencoding('utf-8')

import argparse
from transliterate import get_translit_function

def read_stdin():
    '''
        read standard input
        yeld next line
    '''
    try:
        readline = sys.stdin.readline()
        while readline:
            yield readline
            readline = sys.stdin.readline()
    except:
        # LP: avoid to exit(1) at stdin end
        pass

def parse_args(args):
    return args

def process_args(args):
    # TODO

    if sys.version_info[0] >= 3:
        ofp = codecs.getwriter('utf8')(sys.stdout.buffer)
    else:
        ofp = codecs.getwriter('utf8')(sys.stdout)
    
    for line in read_stdin():
        translit_ru = get_translit_function('ru')
        res =  translit_ru(u"привет я симона", reversed=True)
        
        ofp.write( res )

    # close files
    ofp.close()

def main():
    args = parse_args(sys.argv[1:])
    process_args(args)
