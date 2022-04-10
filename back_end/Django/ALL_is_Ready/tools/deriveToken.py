import jwt
import datetime
from tools.verify import salt

headers={
    'typ':'jwt',
    'alg':'HS256'
}
def create(user,due):
    data={
        'UID':user.UID,
        'Uname':user.Uname,
        'OrgID':user.OrgID,
        'Rank':user.Rank,
        'EXP':user.EXP,
        #改 token 有效期 30天
        'exp':datetime.datetime.utcnow()+datetime.timedelta(minutes=due)
    }
    token=jwt.encode(payload=data,key=salt,algorithm="HS256",headers=headers)
    return token
