#coding:utf-8

import time

class Navigation:
    
    def baiduNavigation(self, toUserName, fromUserName, region, start, end):
        #公交、驾车和步行
        transittitle = "点击查看公交线路导航"
        transiturl = "http://api.map.baidu.com/direction?origin=%s&destination=%s&mode=transit&region=%s&output=html&src=weixin" % \
                        (start.encode("utf-8"),end.encode("utf-8"),region.encode("utf-8"))
        transitpic = ""
        
        drivingtitle = "点击查看驾车线路导航"
        drivingurl = "http://api.map.baidu.com/direction?origin=%s&destination=%s&mode=driving&region=%s&output=html&src=weixin" % \
                        (start.encode("utf-8"),end.encode("utf-8"),region.encode("utf-8"))
        drivingpic = ""
        
        walkingtitle = "点击查看步行线路导航"
        walkingurl = "http://api.map.baidu.com/direction?origin=%s&destination=%s&mode=walking&region=%s&output=html&src=weixin" % \
                        (start.encode("utf-8"),end.encode("utf-8"),region.encode("utf-8"))
        walkingpic = ""
        
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
                    <item>
                        <Title><![CDATA[%s]]></Title> 
                        <Description><![CDATA[]]></Description>
                        <PicUrl><![CDATA[%s]]></PicUrl>
                        <Url><![CDATA[%s]]></Url>
                    </item>
                    <item>
                        <Title><![CDATA[%s]]></Title> 
                        <Description><![CDATA[]]></Description>
                        <PicUrl><![CDATA[%s]]></PicUrl>
                        <Url><![CDATA[%s]]></Url>
                    </item>
                    <item>
                        <Title><![CDATA[%s]]></Title> 
                        <Description><![CDATA[]]></Description>
                        <PicUrl><![CDATA[%s]]></PicUrl>
                        <Url><![CDATA[%s]]></Url>
                    </item>
                </Articles>
                <FuncFlag>0</FuncFlag>
            </xml>
        """ % (fromUserName,toUserName,int(time.time()),4,"百度地图导航",transittitle,transitpic,transiturl, 
               drivingtitle,drivingpic,drivingurl,walkingtitle,walkingpic,walkingurl)
        
        return xml