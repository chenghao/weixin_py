#coding:utf-8

def result_text(fromUser, toUser, createTime, content):
    return """
        <xml>
            <ToUserName><![CDATA[%s]]></ToUserName>
            <FromUserName><![CDATA[%s]]></FromUserName>
            <CreateTime>%s</CreateTime>
            <MsgType><![CDATA[text]]></MsgType>
            <Content><![CDATA[%s]]></Content>
        </xml>
    """ % (fromUser, toUser, createTime, content)
    
def result_music(fromUser, toUser, createTime, musicTitle, musicDes, musicURL, hqmusicURL):
    return """
        <xml>
            <ToUserName><![CDATA[%s]]></ToUserName>
            <FromUserName><![CDATA[%s]]></FromUserName>
            <CreateTime>%s</CreateTime>
            <MsgType><![CDATA[music]]></MsgType>
            <Music>
                <Title><![CDATA[%s]]></Title>
                <Description><![CDATA[%s]]></Description>
                <MusicUrl><![CDATA[%s]]></MusicUrl>
                <HQMusicUrl><![CDATA[%s]]></HQMusicUrl>
            </Music>
            <FuncFlag>0</FuncFlag>
        </xml>
    """ % (fromUser, toUser, createTime, musicTitle, musicDes, musicURL, hqmusicURL)
    
def result_one_news():    
    pass

def result_many_news():
    pass