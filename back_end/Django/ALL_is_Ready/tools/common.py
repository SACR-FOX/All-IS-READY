from models.models import User,ToDoList
from django.db.models import F

HOST_PREFIX="http://hcl.free.svipss.top"
FILE_UPLOAD_CACHE_PATH="/Users/lishengdi/lib/oss_test/"
DEFAULT_PIC="/static/img/header_default.png"

# HOST_PREFIX="http://101.37.175.115"
# FILE_UPLOAD_CACHE_PATH="/home/ALL_IS_READY_CACHE"

def EXP2Rank(exp):
    if exp<81:
        return 1
    if exp>=81 and exp<=160 :
        return 2
    if exp>160 and exp<=300:
        return 3
    if exp>300 and exp<=500:
        return 4
    if exp>500 and exp<=800:
        return 5
    if exp>800 and exp<=1200:
        return 6
    if exp>1200 and exp<=1800:
        return 7
    if exp>1800 and exp<=2500:
        return 8
    if exp>2500 :
        return 9

def addEXP(usr,exp):
    usr.EXP+=exp
    usr.save()
    usr.Rank=EXP2Rank(usr.EXP)
    usr.save()


def daily_jobs():

    # 每日 0：00 积累学习时长清零

    try:
        User.objects.all().update(Accumulation=0)
    except Exception as e:
        print(e)

    # 每日 0：00 留在排行榜的用户获得经验值
    orgs = User.objects.values('OrgID').distinct().order_by('OrgID')
    OrgID_list = []
    for i in orgs:
        if i['OrgID'] != -1:
            OrgID_list.append(i['OrgID'])

    for each in OrgID_list:
        Award_usrs_pre5 = User.objects.filter(OrgID=each).order_by('-Accumulation', '-EXP')[:5].update(EXP=F('EXP')+50)
        Award_usrs_6to10 = User.objects.filter(OrgID=each).order_by('-Accumulation', '-EXP')[5:10].update(EXP=F('EXP') + 25)
        for u in Award_usrs_pre5:
            u.Rank=EXP2Rank(u.EXP)
            u.save()
        for u in Award_usrs_6to10:
            u.Rank = EXP2Rank(u.EXP)
            u.save()


    # 每日清除所有用户已完成的ToDoList项
    DoneList=ToDoList.objects.filter(Status=True)
    DoneList.delete()

    #每日检查和更新组织任务


