#coding: utf-8
import urllib2,json

class Translate:

    def baiduFanYi(self,p):
        qword = urllib2.quote(p)
        baseurl = r"http://openapi.baidu.com/public/2.0/bmt/translate?client_id=Kva4gmB4sRQKZHypQFG211wV&from=auto&to=auto&q="
        url = baseurl + qword
        resp = urllib2.urlopen(url)
        fanyi = json.loads(resp.read())
        
        #将列表转换为字符串
        trans_result = str(fanyi['trans_result'])
        #获取字符串第二个字符开始到最后一个字符-1
        jsonstr = trans_result[1:len(trans_result)-1]
        
        #eval是将字符串转换为字典
        return eval(jsonstr)['dst']