#coding: utf-8
import urllib2,json,time

class Weather:
    
    def baiduWeather(self, city, toUserName, fromUserName):
        baseurl = "http://api.map.baidu.com/telematics/v3/weather?location=%s&output=json&ak=%s" % \
                    (city.encode("utf-8"), "Kva4gmB4sRQKZHypQFG211wV")
        resp = urllib2.urlopen(baseurl)
        jsons = json.loads(resp.read())
        weather_datas = jsons["results"][0]["weather_data"]
        
        xml = """
            <xml>
                <ToUserName><![CDATA[%s]]></ToUserName>
                <FromUserName><![CDATA[%s]]></FromUserName>
                <CreateTime>%s</CreateTime>
                <MsgType><![CDATA[news]]></MsgType>
                <ArticleCount>%s</ArticleCount>
                <Articles>
                    <item>
                        <Title><![CDATA[%s]]></Title> 
                        <Description><![CDATA[]]></Description>
                        <PicUrl><![CDATA[]]></PicUrl>
                        <Url><![CDATA[]]></Url>
                    </item>
        """ % (toUserName, fromUserName, int(time.time()), len(weather_datas), city+"的天气预报") 
        
        for weather in weather_datas:
            xml += """
                <item>
                    <Title><![CDATA[%s]]></Title>
                    <Description><![CDATA[%s]]></Description>
                    <PicUrl><![CDATA[%s]]></PicUrl>
                    <Url><![CDATA[%s]]></Url>
                </item>
            """ % (weather["date"].encode('utf-8')+"\n"+weather["weather"].encode('utf-8')+"  "+weather["temperature"].encode('utf-8')+"\n"+weather["wind"].encode('utf-8'), \
                    "", weather["dayPictureUrl"].encode('utf-8'), "")
            
        xml += """
                </Articles>
                <FuncFlag>0</FuncFlag>
            </xml>
        """    
        
        return xml
        