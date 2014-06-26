#coding: utf-8

import urllib2,re

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class Music:
    
    def baiduMusic(self, musicTitle, musicAuthor):
        baseurl = r"http://box.zhangmen.baidu.com/x?op=12&count=1&title=%s$$%s$$$$" % \
        (urllib2.quote(musicTitle.encode("utf-8")),urllib2.quote(musicAuthor.encode("utf-8")))
        
        resp = urllib2.urlopen(baseurl)
        xml = resp.read()
        
        #.*?是只获取<url>之间的数据 普通url
        url = re.findall('<url>.*?</url>',xml)
        #.*?是只获取<durl>之间的数据 高品质url
        durl = re.findall('<durl>.*?</durl>',xml)

        #获取第一个url中encode标签的数据
        url1 = re.findall('<encode>.*?CDATA\[(.*?)\]].*?</encode>',url[0])
        url2 = re.findall('<decode>.*?CDATA\[(.*?)\]].*?</decode>',url[0])
        
        #取出url1最后一个 /(包含) 之前的数据加上url2最后一个 &(不包含) 之前的数据
        urlpath = url1[0][:url1[0].rindex('/')+1] + url2[0][:url2[0].rindex('&')]
        durlpath = ""
        if durl:
            durl1 = re.findall('<encode>.*?CDATA\[(.*?)\]].*?</encode>',durl[0])
            durl2 = re.findall('<decode>.*?CDATA\[(.*?)\]].*?</decode>',durl[0])
            durlpath = durl1[0][:durl1[0].rindex('/')+1] + durl2[0][:durl2[0].rindex('&')]

        return urlpath, durlpath
    
