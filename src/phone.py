#coding: utf-8

import urllib2,re

class Phone:
    
    def tenpayPhone(self, phone):
        baseurl = "http://life.tenpay.com/cgi-bin/mobile/MobileQueryAttribution.cgi?chgmobile=%s" % (phone)
        resp = urllib2.urlopen(baseurl)
        xml = resp.read()
        
        clientIp = re.findall('<ENV_ClientIp>(.*?)</ENV_ClientIp>',xml)[0]
        retmsg = re.findall('<retmsg>(.*?)</retmsg>',xml)[0]
        province = re.findall('<province>(.*?)</province>',xml)[0]
        city = re.findall('<city>(.*?)</city>',xml)[0]
        supplier = re.findall('<supplier>(.*?)</supplier>',xml)[0]
        
        if retmsg == "OK":
            return "归属地：" + province.decode("gb2312", "utf-8") + city.decode("gb2312", "utf-8") + "  " + supplier.decode("gb2312", "utf-8") + "\n请求客户端：" + clientIp
        else:
            return "查询失败。"