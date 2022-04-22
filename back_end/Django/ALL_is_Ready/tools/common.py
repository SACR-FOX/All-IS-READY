HOST_PREFIX="http://127.0.0.1:8000"
FILE_UPLOAD_CACHE_PATH="/Users/lishengdi/lib/oss_test/"

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



