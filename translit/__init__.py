#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Transliteration Tool
#
# @author Loreto at gmail dot com
# Copyright (c) 2019 Loreto Parisi
#

import sys  
reload(sys)  
sys.setdefaultencoding('utf-8')

import json
import codecs
from transliterate import get_translit_function, get_available_language_codes

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

def process_args(args):
    
    if sys.version_info[0] >= 3:
        ofp = codecs.getwriter('utf8')(sys.stdout.buffer)
    else:
        ofp = codecs.getwriter('utf8')(sys.stdout)

    # last language used
    lang = None
    # last language pack used
    translit = None

    for line in read_stdin():
        try:
            
            obj = json.loads(line)
            text = obj['text']
            source =  obj['source']
            target = obj['target']

            # { "source" : "ru", "target" : "en", "text": "до свидания" }
            # { "source" : "en", "target": "ru", "text": "do svidanija" }
            reversed = True if target == 'en' else False
            lang = source if reversed is True else target

            translit = get_translit_function(lang) # ru
            tline =  translit(text, reversed = reversed) # True

            # result json
            obj['lang'] = lang
            obj['reversed'] = reversed
            obj['trans'] = tline
            res = json.dumps(obj, ensure_ascii=False).encode('utf8')

        except Exception as ex:
            obj = {}
            obj['error'] = str(ex)
            obj['description'] = get_available_language_codes()
            res = json.dumps(obj, ensure_ascii=False).encode('utf8')  

        # write to stdout
        try:
            # {"source": "ru", "trans": "Lorem ipsum dolor sit amet", "target": "en", "text": "Лорем ипсум долор сит амет"}
            ofp.writelines([res, '\n'])
            sys.stdout.flush()
        except Exception:
            pass
        except KeyboardInterrupt:
            # close files when process ends
            ifp.close()
            ofp.close()
            # gracefully exit
            sys.exit(0) 

    # close files
    ofp.close()

def main():
    args = sys.argv[1:]
    process_args(args)
