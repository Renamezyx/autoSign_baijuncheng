from SQLDao import *
import time
from urllib import parse
import requests

playIng = []
while True:
    if(len(playIng) == 0):
        playIng.append((findPlanToday()))
        print(playIng[0][0])
    #执行签到
    else :
        if(playIng[0][0]["State"] == 0  and time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) > str(playIng[0][0]["InTime"])):
            #签入
            url = "http://wechat-pro.bill-jc.com/wechatCloud/attendanceController/signSava?wxuId=B-80732&isgonggancheck=0&iswangluocheck=0"
            headers = {
                "Host": "wechat-pro.bill-jc.com",
                "Connection": "keep-alive",
                "Content-Length": "600",
                "Accept": "application/json, text/javascript, */*; q=0.01",
                "X-Requested-With": "XMLHttpRequest",
                "User-Agent": "Mozilla/5.0 (Linux; Android 11; Redmi Note 8 Pro Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.72 MQQBrowser/6.2 TBS/045811 Mobile Safari/537.36 MMWEBID/2782 MicroMessenger/8.0.15.2020(0x28000F31) Process/tools WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64",
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                "Origin": "http://wechat-pro.bill-jc.com",
                "Referer": "http://wechat-pro.bill-jc.com/wechatCloud/attendanceController/goSignView?workId=Xv0GSGRKhxy%2BOz%2FLIRCeLEDx2wYdYGpKibfGJWq5F%2BM%3D&wxuid=Xv0GSGRKhxy%2BOz%2FLIRCeLEDx2wYdYGpKibfGJWq5F%2BM%3D",
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
            }
            inData = 'gongganRemarks=&workId=B-80732&departmentName=ISBG-BU3-DU1&signDate=' + parse.quote(str(playIng[0][0]["InTime"])[0:10]) + '&signAddress=aQU9ucLsyxhPP%252B1HeM25e1MgwEuKvJbXWTLqLHPsaDVoW7CAkOur8drqla%252BIma9oOl9A9nrEd1Qx%250ANungHgDTNmEVX%252B3KVX8KtMXLHGSxdHhhHtptMjdE%252B7dtUDa0UU8%252F&signTime=' + parse.quote(str(playIng[0][0]["InTime"])) + '&signlnglat=113.94032569897%2C22.54645007723&employeeName=%E6%9B%BE%E8%82%B2%E8%BE%89&flag=&precise=450&juli=87.23&addressId=566&workAddress=%E6%B7%B1%E5%9C%B3%E5%B8%82%E5%8D%97%E5%B1%B1%E5%8C%BA%E7%A7%91%E7%A0%94%E8%B7%AF%E6%9D%BE%E6%97%A5%E9%BC%8E%E7%9B%9B%E5%A4%A7%E5%8E%A6&isSite=onsite&teste=09%3A30&wxVersion=8.0152020028000f3d)'
            inresponse = requests.post(url, headers=headers, data=inData)
            print("执行签入")
            if(inresponse.status_code == 200):
                changeState(playIng[0][0]["Date"],1)
                playIng[0][0]["State"] = 1
        if(playIng[0][0]["State"] == 1 and time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) > str(playIng[0][0]["OutTime"])):
            url = "http://wechat-pro.bill-jc.com/wechatCloud/attendanceController/signOutSava?ischeck=no&wxuId=B-80732&isgonggancheck=0&iswangluocheck=0"
            headers = {
                "Host": "wechat-pro.bill-jc.com",
                "Connection": "keep-alive",
                "Content-Length": "597",
                "Accept": "application/json, text/javascript, */*; q=0.01",
                "X-Requested-With": "XMLHttpRequest",
                "User-Agent": "Mozilla/5.0 (Linux; Android 11; Redmi Note 8 Pro Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.72 MQQBrowser/6.2 TBS/045811 Mobile Safari/537.36 MMWEBID/2782 MicroMessenger/8.0.15.2020(0x28000F31) Process/tools WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64",
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                "Origin": "http://wechat-pro.bill-jc.com",
                "Referer": "http://wechat-pro.bill-jc.com/wechatCloud/attendanceController/goSignOutView?workId=auUw3rMQR%2Fn7JmKPKyC0Czy2r4wZpS4wtpGAvkTPwBQ%3D&wxuid=auUw3rMQR%2Fn7JmKPKyC0Czy2r4wZpS4wtpGAvkTPwBQ%3D",
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
            }
            outData = "gongganRemarks=&workId=B-80732&departmentName=ISBG-BU3-DU1&signOutDate=" + parse.quote(str(playIng[0][0]["Date"])[0:10]) + "&signOutAddress=aQU9ucLsyxhPP%252B1HeM25e1MgwEuKvJbXWTLqLHPsaDVoW7CAkOur8drqla%252BIma9oOl9A9nrEd1Qx%250ANungHgDTNsrhhzmw9mDUMrvmM6mW7dthHtptMjdE%252B7dtUDa0UU8%252F&signOutTime=" + parse.quote(str(playIng[0][0]["OutTime"])) + "&signOutlnglat=113.94030574168%2C22.546208194393&employeeName=%E6%9B%BE%E8%82%B2%E8%BE%89&attId=6945466&hours=&addressId=566&workAddress=%E6%B7%B1%E5%9C%B3%E5%B8%82%E5%8D%97%E5%B1%B1%E5%8C%BA%E7%A7%91%E7%A0%94%E8%B7%AF%E6%9D%BE%E6%97%A5%E9%BC%8E%E7%9B%9B%E5%A4%A7%E5%8E%A6&isSite=onsite&precise=450&juli=89.83&xiabTime=" + parse.quote(str(playIng[0][0]["InTime"])[0:5])
            outresponse = requests.post(url, headers=headers,data=outData)
            print("执行签出")
            changeState(playIng[0][0]["Date"],2)
            if(outresponse.status_code == 200) :
                playIng[0][0]["State"] = 2
                playIng.clear()
                print(playIng)
       