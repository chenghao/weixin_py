#coding: utf-8

import time,re,urllib2

class History:
    
    def todayonhistory(self):
        md = getMonOrDay()
        
        baseurl = "http://www.todayonhistory.com/" + md[0] + "/" + md[1]
        resp = urllib2.urlopen(baseurl)
        html = resp.read()
        #获取<ul class="list clearfix">之间的所有内容
        content = re.findall('<ul class=\"list clearfix\">(.*?)</ul>',html)[0]
        #获取<em>之间和<i>之间的所有内容
        content = re.findall("<em>(.*?)</em> <i>(.*?)</i>", content)
        
        monOrDay = md[0]+"月"+md[1]+"日"
        result = "=历史上的"+monOrDay+"=\n"
        for c in content:
            result += "  ".join(c) + "\n"
        return result
    
    def rijiben(self):
        baseurl = "http://www.rijiben.com/"
        resp = urllib2.urlopen(baseurl)
        html = resp.read()
        # 找出所有class="listren"的div标记
        #re.S是任意匹配模式，也就是.可以匹配换行符
        content = re.findall('<div.*?class="listren".*?>(.*?)</div>', html, re.S)[0]
        content = re.findall('<a.*?href="(.*?)".*?title="(.*?)">(.*?)</a>', content, re.S)
        
        md = getMonOrDay()
        monOrDay = md[0]+"月"+md[1]+"日"
        
        result = "=历史上的"+monOrDay+"=\n"
        for c in content:
            result += "".join(c[1]).replace(monOrDay, "") + "\n"
        return result
        
def getMonOrDay():
    """获取当前的月日  如：4 23"""
    localtime = time.localtime(time.time())
    mon = time.strftime('%m',localtime)
    day = time.strftime('%d',localtime)
    if mon.startswith("0"):
        mon = re.compile("^0").sub('', mon)
    if day.startswith("0"):
        day = re.compile("^0").sub('', day)
        
    return mon,day
