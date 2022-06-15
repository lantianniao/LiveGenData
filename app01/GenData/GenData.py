import random
import time
import pymysql



# 人为设定：
# 用户id四位数
# 用户： 1000-1010、2000-2010 20个人
# 2开头的为日常主播，大概率被关注（70%）,level: 1-7
# ，1开头的为日常用户，小概率被关注（30%）,level:4-9
#

from app01.utils.GenDataUtils import *

user_uid_range = [1000,1010]
zhubo_uid_range = [2000,2010]

def InitUser():

    db = pymysql.connect(host='127.0.0.1', user='root', password='tk54123', port=3306, db='video')
    cursor = db.cursor()
    table = 'cl_level_user'
    user = {}
    i = 1

    # 初始化 1开头
    for id in range(user_uid_range):
        user["id"] = i
        user["uid"] = id
        user["anchor_exp"] = random.randint(50,400)
        user["anchor_level"] = random.randint(5,15)
        user["create_time"] = genDate("2016-07-05","2023-10-10")
        user["update_time"] = genDate("2024-10-11","2026-10-10")
        user["exp"] = 10
        user["level"] = 2
        keys = ','.join(user.keys())
        value = ','.join(['%s'] * len(user))
        sql = 'REPLACE INTO {table}({keys}) VALUES ({values})'.format(table=table, keys=keys, values=value)
        try:
            cursor.execute(sql, tuple(user.values()))
            print("Successful")
            db.commit()
        except Exception as e:
            print('插入失败，原因：', e, '数据：', user)
            print("Failed")
            db.rollback()
        i+=1

    for id in range(zhubo_uid_range):
        user["id"] = i
        user["uid"] = id
        user["anchor_exp"] = random.randint(5,400)
        user["anchor_level"] = random.randint(10,35)
        user["create_time"] = genDate("2016-07-05","2023-10-10")
        user["update_time"] = genDate("2024-10-11","2026-10-10")
        user["exp"] = 10
        user["level"] = 2
        keys = ','.join(user.keys())
        value = ','.join(['%s'] * len(user))
        sql = 'REPLACE INTO {table}({keys}) VALUES ({values})'.format(table=table, keys=keys, values=value)
        try:
            cursor.execute(sql, tuple(user.values()))
            print("Successful")
            db.commit()
        except Exception as e:
            print('插入失败，原因：', e, '数据：', user)
            print("Failed")
            db.rollback()
        i += 1
    cursor.close()
    db.close()


def GenHistoryFollowData(num):
    db = pymysql.connect(host='127.0.0.1', user='root', password='tk54123', port=3306, db='video')
    cursor = db.cursor()
    table = 'follower_00'
    data = {}
    for i in range(num):
        if random.randint(1,10)<8:
            fuid = random.randint(zhubo_uid_range[0],zhubo_uid_range[1]-1)
        else:
            fuid = random.randint(user_uid_range[0], user_uid_range[1] - 1)
        uid = random.choice(
            list(range(user_uid_range[0], user_uid_range[1])) + list(range(zhubo_uid_range[0], zhubo_uid_range[1])))
        timestamp= genDate(datestart='2026-01-30', dateend='2026-01-30')
        data["fuid"] = fuid
        data["uid"] = uid
        data["timestamp"] = timestamp
        keys = ','.join(data.keys())
        value = ','.join(['%s'] * len(data))
        sql = 'REPLACE INTO {table}({keys}) VALUES ({values})'.format(table=table, keys=keys, values=value)
        try:
            cursor.execute(sql, tuple(data.values()))
            print("Successful")
            db.commit()
        except Exception as e:
            print('插入失败，原因：', e, '数据：', data)
            print("Failed")
            db.rollback()
        i += 1
    cursor.close()
    db.close()



def GenRealTimeFollowData():
    if random.randint(1,10)<8:
        followuid = random.randint(zhubo_uid_range[0],zhubo_uid_range[1]-1)
    else:
        followuid = random.randint(user_uid_range[0], user_uid_range[1] - 1)

    ret = {}
    ret["followuid"] = followuid
    ret["followeruid"] = random.choice(list(range(user_uid_range[0],user_uid_range[1]))+list(range(zhubo_uid_range[0],zhubo_uid_range[1])))
    ret["type"] = "user_follow"
    ret["timestamp"] = timeStrToTimeStamp(genDate(datestart='2020-01-01',dateend='2026-12-12'))
    if random.randint(0,9) < 7:
        ret["desc"] = "follow"
    else:
        ret["desc"] = "unfollow"
    return ret

def GenVideoData(date):
    ret = {}
    ret["area"] = genArea()
    ret["watchnumpv"] = random.randint(1,500)
    ret["follower"] = random.randint(50,700)
    ret["hosts"] = random.randint(50,500)
    ret["watchnumuv"] = random.randint(1,500)
    ret["gifter"] = random.randint(1,500)
    ret["nofollower"] = random.randint(1,500)
    ret["length"] = random.randint(1,500)
    ret["rating"] = genRating()
    ret["smlook"] = random.randint(1,500)
    ret["type"] = "video_info"
    ret["gold"] = random.randint(1,500)
    ret["uid"] = random.randint(zhubo_uid_range[0],zhubo_uid_range[1]-1)
    ret["nickname"] = genNickName()
    ret["looktime"] = random.randint(100,500)
    ret["id"] = "1751215421512"
    ret["exp"] = random.randint(1,500)
    ret["timestamp"] = timeStrToTimeStamp(genDate(datestart=date,dateend=date))
    return ret

def GenUserActiveData(date):
    ret = {}
    ret["uid"] = random.choice(list(range(user_uid_range[0],user_uid_range[1]))+list(range(zhubo_uid_range[0],zhubo_uid_range[1])))
    ret["ver"] = genVer()
    ret["countryCode"] = genCountryCode()
    ret["ip"] = genIP()
    ret["UnixtimeStamp"] = str(timeStrToTimeStamp(date))
    ret["mcc"] = 452
    ret["type"] = "user_active"
    return ret



if __name__ == '__main__':
    # print(len(GenVideoData()))
    GenHistoryFollowData(20)
