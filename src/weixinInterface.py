#coding: utf-8
import hashlib
import web
import time
import os
import music,translate,face,weather,ip,phone,todayonhistory,navigation,imei
import re
from xml.etree import ElementTree as etree

import sys 
reload(sys) 
sys.setdefaultencoding('utf-8')

import promptMsg


class WeixinInterface:
    def __init__(self):
        self.app_root = os.path.dirname(__file__)
        self.templates_root = os.path.join(self.app_root, 'templates')
        self.render = web.template.render(self.templates_root)
        
    def GET(self):
        #获取输入参数
        data = web.input()
        signature=data.signature
        timestamp=data.timestamp
        nonce=data.nonce
        echostr=data.echostr
        #自己的token
        token="juanzi" #这里改写你在微信公众平台里输入的token
        #字典序排序
        list=[token,timestamp,nonce]
        list.sort()
        sha1=hashlib.sha1()
        map(sha1.update,list)
        hashcode=sha1.hexdigest()
        #sha1加密算法        
 
        #如果是来自微信的请求，则回复echostr
        if hashcode == signature:
            return echostr
            
    def POST(self):        
        str_xml = web.data() #获得post来的数据
        xml = etree.fromstring(str_xml)#进行XML解析
        msgType=xml.find("MsgType").text
        fromUser=xml.find("FromUserName").text
        toUser=xml.find("ToUserName").text
        
        respContent = ""
        
        if msgType == "text":
            content=xml.find("Content").text#获得用户所输入的内容
            
            if content.startswith("翻译"):
                #拆分以翻译开头
                reinfo = re.compile("^翻译")
                #首先content值类型是unicode，所以要先转换为str在拆分,strip去除左右空格
                args = reinfo.sub('', content.encode("utf-8")).strip()
                if not args:
                    respContent = promptMsg.getFanYiMsg()
                else:    
                    respContent = translate.Translate().baiduFanYi(args)
                
            elif content.startswith("歌曲"):
                reinfo = re.compile("^歌曲")
                args = reinfo.sub('', content.encode("utf-8")).strip()
                argslist = args.split("@")
                des = "来自百度音乐"
                if not argslist[0]:
                    respContent = promptMsg.getMusicMsg()
                elif len(argslist) == 1:
                    respContent = music.Music().baiduMusic(argslist[0],"")
                else:
                    des = argslist[1]
                    respContent = music.Music().baiduMusic(argslist[0],argslist[1])
                
                if argslist[0]:
                    return self.render.reply_music(fromUser,toUser,int(time.time()),argslist[0],des,respContent[0],respContent[1])
        
            elif content.startswith("天气"):
                reinfo = re.compile("^天气")
                args = reinfo.sub('', content.encode("utf-8")).strip()
                if not args:
                    respContent = promptMsg.getWeather()
                else:
                    newsMsg = weather.Weather().baiduWeather(args, fromUser, toUser)
                    return newsMsg
        
            elif content.startswith("ip"):
                reinfo = re.compile("^ip")
                args = reinfo.sub('', content.encode("utf-8")).strip()
                if not args:
                    respContent = promptMsg.getIp()
                else:    
                    respContent = ip.IP().taobaoIP(args)
            
            elif content.startswith("手机"):
                reinfo = re.compile("^手机")
                args = reinfo.sub('', content.encode("utf-8")).strip()
                if not args:
                    respContent = promptMsg.getPhone()
                else:
                    respContent = phone.Phone().tenpayPhone(args).encode("utf-8")
            
            elif content.startswith("苹果"):
                reinfo = re.compile("^苹果")
                args = reinfo.sub('', content.encode("utf-8")).strip()
                if not args:
                    respContent = promptMsg.getApple()
                else:
                    result, code = imei.IMEI().appleIMEI(args, toUser, fromUser)
                    if code == 0:
                        return result
                    elif code == -1:
                        respContent = result
                    
            elif content.encode("utf-8").strip() == "历史上的今天" or content.encode("utf-8").strip() == "lssdjt":
                respContent = todayonhistory.History().rijiben()
            
            elif len(content.replace("—","-").replace("-","-").split("-")) == 3:
                s = content.replace("—","-").replace("-","-").split("-")
                region = s[0]
                start = s[1]
                end = s[2]
            
                newsMsg = navigation.Navigation().baiduNavigation(toUser, fromUser, region, start, end)
                return newsMsg
                
            else:
                respContent = promptMsg.getTextMsg()
        
        elif msgType == "image":
            #取得图片地址  
            picUrl = xml.find("PicUrl").text  
            respContent = face.face(picUrl)
        
        elif msgType == "location":
            respContent = xml.find("Location_X").text
        
        elif msgType == "event":
            #事件类型
            eventType = xml.find("Event").text
            #订阅
            if eventType == "subscribe":
                respContent = "谢谢您关注娟子服装。"
            #取消订阅    
            #elif eventType == "unsubscribe":
                #取消订阅后用户再收不到公众号发送的消息，因此不需要回复消息
            #自定义菜单点击事件    
            elif eventType == "CLICK":
                #事件KEY值，与创建自定义菜单时指定的KEY值对应
                eventKey = xml.find("EventKey").text
                #TODO
        
        return self.render.reply_text(fromUser,toUser,int(time.time()),respContent)