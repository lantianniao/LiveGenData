
import random
import datetime
import struct
import time
from socket import socket


def genDate(datestart=None,dateend=None):
    if datestart!=None:
        datestart = datestart
    else:
        datestart = "1970-06-28"
    if dateend!=None:
        dateend = dateend
    else:
        dateend = "2002-06-28"
    # bir_add = random.randint(0,max_day)
    datestart = datetime.datetime.strptime(datestart, '%Y-%m-%d')
    datestart += datetime.timedelta()
    date_str = datestart.strftime('%Y-%m-%d')
    return date_str

def timeStrToTimeStamp(time_str):
    if len(time_str)<12:
        time_str = time_str+" 00:00:00"
    timeArray = time.strptime(time_str, "%Y-%m-%d %H:%M:%S")
    timeStamp = int(time.mktime(timeArray))
    return timeStamp


def genArea():
    area_list = ["A_US","B_US",
                 "A_CN","B_CN",
                 "A_JAP","B_JAP",
                 "A_KOR","B_KOR"
                 ]
    return random.choice(area_list)

def genRating():
    return random.choice(["S","A","B","C","D"])


def genNickName():
    name_list = ["patton","nicole","anthony",
                 "zane","venus","twinkle",
                 "esther","danika","clement",
                 "edgar",
                 ]
    num = str(random.randint(10,50))
    return random.choice(name_list)+num


def genVer():
    ver_list = ["3.5.12","3.6.15","3.7.19"]
    return random.choice(ver_list)

def genCountryCode():
    code_list = ["VN","PV","IFN","ION","CI","CN"]
    return random.choice(code_list)



def genIP():
    ip1 = random.randint(0,255)
    ip2 = random.randint(0,255)
    ip3 = random.randint(0,255)
    ip4 = random.randint(0,255)
    return '.'.join([str(ip1),str(ip2),str(ip3),str(ip4)])




if __name__ == '__main__':
    # date = genDate("2026-02-01")
    stamp = timeStrToTimeStamp('2026-02-01 00:00:00')
    print(genIP())