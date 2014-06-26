#coding: utf-8

import urllib2,json
import models

def face(path):
    baseurl = "http://apicn.faceplusplus.com/v2/detection/detect?url=%s&api_secret=%s&api_key=%s" % \
               (path.encode("utf-8"), "haugjGwsaQ8e9eMH2KLS_zzJnlLWjK6C", "6275292f9b91559205b45e6e98de3546")
               
    resp = urllib2.urlopen(baseurl)
    jsons = json.loads(resp.read())

    #排序， 从左到右
    jsonFaces = sorted(jsons['face'], key = centerX)
    
    faces = []
    for face in jsonFaces:
        attributes = face["attribute"]
        positions = face["position"]
        
        race = raceConvert(attributes["race"]["value"])
        gender = genderConvert(attributes["gender"]["value"])
        
        faces.append(models.Face(face["face_id"],attributes["age"]["value"],
                                 gender,race,attributes["smiling"]["value"],
                                 positions["center"]["x"],positions["center"]["y"]))

    return makeMessage(faces)


def centerX(s):
    '''返回水平线的值'''
    return s["position"]["center"]["x"]
        
def raceConvert(race):   
    result = "黄种人"
    if race == "Asian":
        result = "黄种人"
    elif race == "White":    
        result = "白种人"
    elif race == "Black":
        result = "黑种人"
    
    return result    
        
def genderConvert(gender):
    result = "男性"      
    if gender == "Male":
        result = "男性"
    elif gender == "Female":
        result = "女性"
    
    return result
    
    
def makeMessage(faces):    
    facesLen = len(faces)
    msg_list = []
    msg_list.append("共检测到")
    msg_list.append(str(facesLen))
    msg_list.append("张人脸：\n")
    
    if facesLen == 1:
        jointMsg(faces, msg_list)
    
    elif facesLen > 1:
        msg_list.append("按脸部中心位置从左至右依次为：\n")
        jointMsg(faces, msg_list)
        
    return "".join(msg_list)
    
    
def jointMsg(faces, msg_list):    
    for face in faces:
        msg_list.append(face.raceValue)
        msg_list.append(",")
        msg_list.append(face.genderValue)
        msg_list.append(",")
        msg_list.append(str(face.ageValue))
        msg_list.append("岁左右\n")
            
            
#face("http://www.damiwan.com/damiwanimg/face/bigFace/3174c3e3d0e44a3c849770ef6b814285.jpg")    
#print face("http://cn.faceplusplus.com/static/resources/python_demo/2.jpg")
#face("http://pic11.nipic.com/20101111/6153002_002722872554_2.jpg")

