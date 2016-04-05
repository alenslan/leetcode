#coding:utf-8
'''
目的：百度相关搜索的相关词抓取
时间：2016-03-26
'''
import requests
import re

class Spider(object):
    def __init__(self):
        self.badui_url = 'https://www.baidu.com/s?wd='
        # 输入词列表
        self.words = ''
        # 内部循环列表
        self.loop_list = []
        # 输出列表
        self.result_list = []
        self._html = ''
        self.count = 0
        self.f = open('baidu_relation.txt', 'w')

    def __crawl(self, url):
        headers = {
            'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36'
        }
        
        respone = requests.get(url, headers = headers)
        if respone.status_code == 200:
            print '抓取完成%s%s' % (self.count, '*' * 20)
            self._html = respone.text
        else:
            self._html = ''
            
    def __paser(self):
        self._html = self._html.encode('utf-8')
        regx1 = re.compile('</div>\s*<table cellpadding="0">(.*?)</table>', re.M|re.S)
        regx2 = re.compile('<a[^>]+>(.*?)</a>', re.M|re.S)

        if not self._html:
            return
        res1 = re.findall(regx1, self._html)
        if not res1: return

        data1 = res1[0]
        res2 = re.findall(regx2, data1)
        for res in res2:
            if res not in self.result_list and self.word in res:
                self.result_list.append(res)
                self.loop_list.append(res)
                print >> self.f, res
        print '解析完成%s%s' % (self.count, '*' * 20)

    def loop(self):
        while 1:
            if not self.loop_list:
                break
            word = self.loop_list[0]
            url = self.badui_url + word
            self.__crawl(url)
            self.__paser()
            self.loop_list.remove(word)
            self.count += 1
            if self.count > 500:
                break
        
    def baidu(self, word):
        url = self.badui_url + word
        self.word = word
        self.__crawl(url)
        print self._html
        self.__paser()
    
    def result(self):
        return self.result_list
          
S = Spider()
S.baidu('蒂芙尼')
S.loop()