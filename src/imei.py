#coding:utf-8

import urllib2, json, time

class IMEI:
    
    def appleIMEI(self, sn, toUserName, fromUserName):
        baseurl = "http://www.25pp.com/xuliehao/index.php?action=search&sn=%s" % (sn)
        
        resp = urllib2.urlopen(baseurl)
        jsons = json.loads(resp.read())
        
        code = jsons["resultcode"]

        if code == "200":
            description = "序列号：%s\nIMEI号码：%s\n设备名称：%s\n激活状态：%s\n电话支持：%s\n硬件保修：%s\n生产工厂：%s" % \
                          (jsons["result"]["serial_number"], jsons["result"]["imei_number"], \
                           jsons["result"]["phone_model"], jsons["result"]["active"], \
                           jsons["result"]["tele_support_status"], jsons["result"]["warranty_status"], \
                           jsons["result"]["made_area"])
            
            xml = """
                  <xml>
                      <ToUserName><![CDATA[%s]]></ToUserName>
                      <FromUserName><![CDATA[%s]]></FromUserName>
                      <CreateTime>%s</CreateTime>
                      <MsgType><![CDATA[news]]></MsgType>
                      <ArticleCount>1</ArticleCount>
                      <Articles>
                          <item>
                              <Title><![CDATA[%s]]></Title> 
                              <Description><![CDATA[%s]]></Description>
                              <PicUrl><![CDATA[]]></PicUrl>
                              <Url><![CDATA[]]></Url>
                          </item>
                      </Articles>
                      <FuncFlag>0</FuncFlag>
                  </xml>
                  """ % (fromUserName, toUserName, int(time.time()), "苹果产品信息查询", description)
        
            return xml, 0
        else:
            return "查询失败", -1