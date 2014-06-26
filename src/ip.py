#coding: utf-8
import urllib2,json

class IP:
    
    def taobaoIP(self,ip):
        baseurl = "http://ip.taobao.com/service/getIpInfo.php?ip=%s" % (ip)
                    
        resp = urllib2.urlopen(baseurl)
        jsons = json.loads(resp.read())
        
        code = jsons["code"]
        
        result = ""
        if code == 0:
            country = jsons["data"]["country"]
            region = jsons["data"]["region"]
            city = jsons["data"]["city"]
            isp = jsons["data"]["isp"]
        
            if country:
                result += country
            if region:
                result += "\n"+region
            if city:
                result += city
            if isp:
                result += "\n"+isp    
        else:
            result = "查询失败。"
        
        return result