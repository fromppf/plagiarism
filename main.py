#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

from Levenshtein import seqratio

from parser import readfile, getkeywords, getsegments
from spider import search

def evaluate(text1, text2):
    text1 = getsegments(text1)
    text2 = getsegments(text2)

    size = 8
    threshold = 0.1

    text1s = [text1[i:i+size] for i in range(0, len(text1), size)]
    text2s = [text2[i:i+size] for i in range(0, len(text2), size)]

    blocks = []
    for s in text1s:
        for t in text2s:
            res = seqratio(s, t)
            if res > threshold:
                blocks.append({'plagiarized': res, 'input': s, 'origin': t})

    return blocks

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
