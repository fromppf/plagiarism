#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from io import StringIO, BytesIO
from docx import Document
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFResourceManager, process_pdf
import html2text

import jieba
import jieba.analyse

from spider import download

def _parse_docx_table(table, text=''):
    for row in table.rows:
        for cell in row.cells:
            text += '\n\n'.join([
                paragraph.text for paragraph in cell.paragraphs
            ])

            for table in cell.tables:
                text += _parse_docx_table(table, text)

    return text

def readfile(file):
    try:
        if file.startswith('https://') or file.startswith('http://') or file.startswith('ftp://'):
            data = BytesIO(download(file))
        else:
            data = open(file, 'rb')

        if file.endswith('.caj'):
            raise Exception('.caj files are not supported')
        elif file.endswith('.doc'):
            raise Exception('.doc files are not supported')
        elif file.endswith('.docx'):
            text = ''
            document = Document(data)

            text += '\n\n'.join([
                paragraph.text for paragraph in document.paragraphs
            ])

            for table in document.tables:
                text += _parse_docx_table(table, text)

            return text
        elif file.endswith('.htm') or file.endswith('.html'):
            html = html2text.HTML2Text()
            html.ignore_links = True
            return html.handle(data)
        elif file.endswith('.pdf'):
            with StringIO() as outfp:
                rsrcmgr = PDFResourceManager()
                device = TextConverter(rsrcmgr, outfp)
                process_pdf(rsrcmgr, device, data)
                return outfp.getvalue()
        elif file.endswith('.rtf'):
            raise Exception('.rtf files are not supported')
        elif file.endswith('.txt'):
            return data.read()
        else:
            raise Exception('Unknown file extension')
    except:
        pass

def getkeywords(text):
    try:
        # TF-IDF
        return jieba.analyse.extract_tags(text, topK=10)
        # TextRank
        #return jieba.analyse.textrank(text, topK=10)
    except:
        pass

def getsegments(text):
    try:
        return jieba.lcut(text, cut_all=False, HMM=False)
    except:
        pass
