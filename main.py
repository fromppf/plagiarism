#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

from parser import readfile, getkeywords, evaluate
from spider import search

def checkfile(file):
    res = {'input': file, 'keywords': [], 'results': []}

    # read file fulltext
    text = readfile(file)
    if text is None:
        print('This file appears to be invalid')
        return res

    # get keywords
    keywords = getkeywords(text)
    print('Keywords: ', ', '.join(keywords))
    res['keywords'] = keywords

    # search by keywords
    results = search(keywords).results()

    if not results:
        print('No result.')
        return res

    # processing files
    for i, result in enumerate(results):
        try:
            print('\nProcessing file {0}: {1} ({2})'.format(str(i + 1), result['name'], result['url']))
            text2 = readfile(result['url'])
            if text2 is None:
                print('This file appears to be invalid')
                continue
            # get keywords
            keywords2 = getkeywords(text2)
            print('Keywords: ', ', '.join(keywords2))
            # compare segments to detect plagiarism blocks
            blocks = evaluate(text, text2)
            print('Search ended, found {0} plagiated blocks'.format(len(blocks)))
        except:
            continue

        if not blocks:
            continue

        res['results'].append({
            'origin': result['url'],
            'title': result['name'],
            'keywords': keywords,
            'blocks': blocks,
            'plagiarized': sum(block['plagiarized'] for block in blocks) / len(blocks)
            })

    return res

if __name__ == '__main__':
    if len(sys.argv) >= 2:
        print(checkfile(sys.argv[1]))
    else:
        raise Exception('No input file specified')
