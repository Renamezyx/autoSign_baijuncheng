import random
import time
import datetime
#原字典
import copy

def randomTime(strat,end):
    #不足两位补0
    #eg:  randomTime(0,60)
    result = random.randint(strat,end)
    if result < 10 :
        return "0" + str(result)
    else :
        return str(result) 

def createWorkDate(startDate,num):
    #生成Work时间
    #eg: createWorkDate( "2021-12-31 00:00:00",9)
    startDate = datetime.datetime.strptime(startDate, "%Y-%m-%d %H:%M:%S")
    result = []
    model = {"Date":None,"InTime":None,"OutTime":None}
    for i in range(num):
       modelDao = copy.deepcopy(model)
       date = (startDate + datetime.timedelta(days=+i)).strftime("%Y-%m-%d ")
       outsec  = randomTime(0,59)
       outhour = randomTime(19,22)
       outminu = randomTime(0,59)
       insec  = randomTime(0,59)
       inhour  = randomTime(9,9)
       inminu  = randomTime(0,29)
       modelDao["Date"] = str(date) + "00:00:00"
       modelDao["InTime"] = str(date) + str(inhour) + ":" + str(inminu) + ":" + str(insec)
       modelDao["OutTime"] = str(date) + str(outhour) + ":" + str(outminu) + ":" + str(outsec)
       result.append(modelDao)
    return result

