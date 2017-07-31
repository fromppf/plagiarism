#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from time import strftime
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import re

def download(url, data = None):
    try:
        response = urllib.request.urlopen(url=url, data=data, timeout=5)
        return response.read()
    except:
        return None

class search:
    SEARCH_URL = u"http://kns.cnki.net/kns/request/SearchHandler.ashx"
    RESULT_URL = u"http://kns.cnki.net/kns/brief/brief.aspx?pagename=%(pagename)s&t=%(timestamp)s&recordsperpage=50"

    def __init__(self, keywords):
        self.keywords = keywords

    def __fetch(self):
        query = u' AND '.join(u'FT=\'{0}\''.format(keyword) for keyword in self.keywords)

        data = urllib.parse.urlencode({
            'NaviCode': u'*',
            'PageName': u'ASP.brief_result_aspx',
            'DbPrefix': u'SCDB',
            'DbCatalog': u'中国学术文献网络出版总库',
            'ConfigFile': u'SCDB.xml',
            #'db_opt': u'CJFQ,CJFN,CDFD,CMFD,CPFD,IPFD,CCND,CYFD,SCOD,CISD,SNAD,CCJD',
            #'db_value': u'中国期刊全文数据库,中国博士学位论文全文数据库,中国优秀硕士学位论文全文数据库,中国重要会议论文全文数据库,国际会议论文全文数据库,中国重要报纸全文数据库',
            'expertvalue': query
        }).encode('utf-8')

        pagename = download(search.SEARCH_URL, data=data).decode('utf-8')

        url = search.RESULT_URL % {
            'pagename': pagename,
            'timestamp': strftime('%s')
        }

        return download(url)

    def results(self):
        res = []

        try:
            text = self.__fetch().decode('utf-8')

            soup = BeautifulSoup(text, 'html.parser')

            table = soup.find('table', {'class': 'GridTableContent'})

            if table is None:
                return res

            results = table.select('tr[bgcolor]')

            for result in results:
                try:
                    d = result.find(href=re.compile('download\.aspx'))
                    n = result.find(href=re.compile('detail\.aspx'))
                    res.append({'name': n.text.replace("document.write(ReplaceChar1(ReplaceChar(ReplaceJiankuohao('", '').replace("'))));", ''), 'url': d.get('href')})
                except:
                    continue
        except:
            raise

        return res
