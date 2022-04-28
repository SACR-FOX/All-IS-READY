from datetime import datetime
import time
class switcher:
    day2num_dict={
        "Mon":1,
        "Tue":2,
        "Wed":3,
        "Thus":4,
        "Fri":5
    }
    def sec2hm(self,Sec):
        h=str(Sec//3600) if (Sec//3600)>10 else "0"+str(Sec//3600)
        m=str((Sec%3600)//60) if (Sec%3600)//60 > 10 else "0"+str((Sec%3600)//60)
        return h+":"+m

    def secFrom0(self):
        now = int(time.time())
        day_time = now - now % 86400 + time.timezone
        past = now - day_time
        return past

    def due(self,end):
        return (end-self.secFrom0())

    def daySec(self):
        now = int(time.time())
        day_time = now - now % 86400 + time.timezone
        return int(day_time)

    def ifSameDay(self,last):
        now = int(time.time())
        day_start_time = now - now % 86400 + time.timezone

        if last < day_start_time:
            return False
        else :
            return True

