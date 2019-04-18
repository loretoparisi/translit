#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Musixmatch API API
#
# @author Loreto Parisi at musixmatch dot com
# Copyright (c) 2019 Musixmatch spa
#

import sys  
reload(sys)  
sys.setdefaultencoding('utf-8')

import argparse
from transliterate import get_translit_function

def parse_args(args):
    return args

def process_args(args):
    # TODO
    
    translit_ru = get_translit_function('ru')
    print(translit_ru(u"привет я симона", reversed=True))


def main():
    args = parse_args(sys.argv[1:])
    process_args(args)
