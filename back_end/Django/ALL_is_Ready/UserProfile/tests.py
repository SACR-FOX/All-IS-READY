from django.test import TestCase
from tools.common import EXP2Rank
from tools.timeTool import switcher
from models.models import User

sw=switcher()
# Create your tests here.
class exp2rank_test(TestCase):
    def Test(self):
        res=EXP2Rank(801)
        self.assertEqual(res, 6, '经验转换函数异常')

class userCreate_test(TestCase):
    def test_user_and_show(self):
        print ('testing')
        u= User.objects.create(Uname="test", Passwd="123123", Rank=1, Accumulation=0, EXP=0)
        # djangotE(7get_xxx_disploy##,sex_show
        self.assertEqual(u.OrgID,-1,'组织初始化失败')
        self.assertEqual(u.Header.url,'/media/static/img/header_default.png','默认头像赋值失败')

class time_test(TestCase):
    def StampTest(self):
        self.assertEqual(sw.stamp2str(1654001032),"05月31日 20:43" , '时间戳转换函数异常')
    def sec2hm_test(self):
        self.assertEqual(sw.sec2hm(36000), "10:00", '日记时时间戳转换函数异常')
    def pass_test(self):
        self.assertEqual(sw.ifPass(1654001032),True,"是否过期检测函数异常")
    def sameday_test(self):
        self.assertEqual(sw.ifSameDay(1654001032),False,"是否同日判断函数异常")