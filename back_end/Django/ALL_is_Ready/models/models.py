from django.db import models

# Create your models here.
class User(models.Model):
    class Meta:
        db_table='User'
        verbose_name = '用户'
        verbose_name_plural = '用户'

    UID = models.AutoField(verbose_name="用户ID", primary_key=True)
    Uname = models.CharField(verbose_name="用户名", max_length=25, default='unnamed')
    Passwd=models.CharField(verbose_name="密码",max_length=25,default='password-not-set')
    OrgID=models.IntegerField(verbose_name="班级ID")
    STUID=models.IntegerField(verbose_name="学号")
    Rank=models.IntegerField(verbose_name="等级")
    Header=models.ImageField(verbose_name="用户头像",upload_to='userHeader',default='/static/img/header_default.png')
    EXP=models.IntegerField(verbose_name="用户经验值")