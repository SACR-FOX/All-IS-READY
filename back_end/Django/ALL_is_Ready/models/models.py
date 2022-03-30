
from django.db import models

# Create your models here.



class Organization(models.Model):
    class Meta:
        db_table='Organization'
        verbose_name = '组织'
        verbose_name_plural = '组织'
    OrgID=models.AutoField(verbose_name="组织ID",primary_key=True)
    OrgName=models.CharField(verbose_name="组织名称",max_length=25)
    MonitorID=models.IntegerField(verbose_name="班长ID")
    Description=models.CharField(verbose_name="描述",max_length=200)


class User(models.Model):
    class Meta:
        db_table='User'
        verbose_name = '用户'
        verbose_name_plural = '用户'

    UID = models.AutoField(verbose_name="用户ID", primary_key=True)
    Uname = models.CharField(verbose_name="用户名", max_length=20, default='unnamed')
    Passwd=models.CharField(verbose_name="密码",max_length=25,default='password-not-set')
    OrgID=models.IntegerField(verbose_name="组织ID",default=-1)
    STUID=models.IntegerField(verbose_name="学号",default=-1)
    Rank=models.IntegerField(verbose_name="等级",default=0)
    Header=models.ImageField(verbose_name="用户头像",upload_to='userHeader',default='/static/img/header_default.png')
    EXP=models.IntegerField(verbose_name="用户经验值",default=0)

class Shedule(models.Model):
    class Meta:
        db_table = 'Shedule'
        verbose_name = '课程表'
        verbose_name_plural = '课程表'

    SheduleID = models.AutoField(verbose_name="所属用户ID", primary_key=True)
    UID = models.IntegerField(verbose_name="所属用户ID")
    DurationStart=models.IntegerField(verbose_name="课程开始相对时间")
    DurationEnd = models.IntegerField(verbose_name="课程结束相对时间")
    Repeat=models.IntegerField(verbose_name="课程日期")
    CurName=models.CharField(verbose_name="课程名称",max_length=20)
    Tag=models.IntegerField(verbose_name="标签颜色")

class ToDoList(models.Model):
    class Meta:
        db_table = 'ToDoList'
        verbose_name = '提醒事项'
        verbose_name_plural = '提醒事项'

    ID=models.AutoField(verbose_name="事项ID", primary_key=True)
    OrgID=models.IntegerField(verbose_name="组织ID",default=-1)
    UID = models.IntegerField(verbose_name="所属用户ID")
    ItemName=models.CharField(verbose_name="计划名称",max_length=20)
    Time=models.DateTimeField(verbose_name="提醒时间")
    Status=models.BooleanField(verbose_name="当前状态")
    Tag = models.IntegerField(verbose_name="标签颜色")

class File(models.Model):
    class Meta:
        db_table = 'File'
        verbose_name = '课程文件'
        verbose_name_plural = '课程文件'


    FID=models.AutoField(verbose_name="文件ID", primary_key=True)
    Fname=models.CharField(max_length=256,verbose_name="文件名")
    Uri=models.CharField(max_length=256,verbose_name="文件相对地址")
    Theme=models.CharField(max_length=15,verbose_name="分类名称")
    Renewal=models.DateTimeField(verbose_name="最后访问时间")

class OrgTask(models.Model):
    class Meta:
        db_table = 'OrhTask'
        verbose_name = '班级任务'
        verbose_name_plural = '班级任务'

    TaskID=models.AutoField(verbose_name="任务ID", primary_key=True)
    OrgID=models.IntegerField(verbose_name="组织ID")
    CID=models.IntegerField(verbose_name="绑定课程ID")
    TimeStart=models.DateTimeField(verbose_name="任务开始时间")
    TimeDue=models.DateTimeField(verbose_name="任务到期时间")
    Status=models.BooleanField(verbose_name="当前状态")
    Description=models.CharField(max_length=256,verbose_name="任务描述")
    TaskName=models.CharField(max_length=30,verbose_name="任务标题")
    Creator=models.CharField(max_length=20,verbose_name="创建者")
    AckCount=models.IntegerField(verbose_name="已知人数")


class Community(models.Model):
    class Meta:
        db_table = 'Community'
        verbose_name = '社区名称'
        verbose_name_plural = '社区名称'

    CommunityID = models.AutoField(verbose_name="社区ID", primary_key=True)
    CommunityName=models.CharField(max_length=20,verbose_name="社区名称")
    PostCount=models.IntegerField(verbose_name="帖子数")
    AdministratorID=models.IntegerField(verbose_name="管理用户ID")
    Renewal=models.DateTimeField(verbose_name="最后更新时间")
    Poster=models.ImageField(verbose_name="社区封面图像",upload_to='communityHeader',default='/static/img/header_default.png')
    Description = models.CharField(max_length=256, verbose_name="社区简介")

class CommunityTopic(models.Model):
    class Meta:
        db_table = 'CommunityTopic'
        verbose_name = '社区主题'
        verbose_name_plural = '社区主题'


    TopicID = models.AutoField(verbose_name="社区主题ID", primary_key=True)
    Creator=models.IntegerField(verbose_name="创建者ID")
    Time=models.DateTimeField(verbose_name="创建时间")
    HasImage=models.BooleanField(verbose_name="是否含有图片")
    Title=models.CharField(max_length=35,verbose_name="主题标题")
    ImageUri=models.ImageField(verbose_name="话题封面图像",upload_to='TopicHeader',default='/static/img/header_default.png')

class TopicPost(models.Model):
    class Meta:
        db_table = 'TopicPost'
        verbose_name = '主题帖子'
        verbose_name_plural = '主题帖子'

    PostID=models.AutoField(verbose_name="主题帖子ID",primary_key=True)
    TopicID=models.IntegerField(verbose_name="社区主题ID")
    UID=models.IntegerField(verbose_name="用户ID")
    Time = models.DateTimeField(verbose_name="创建时间")
    HasImage = models.BooleanField(verbose_name="是否含有图片")
    Content=models.CharField(max_length=300,verbose_name="帖子内容")

class PostImage(models.Model):
    class Meta:
        db_table = 'PostImage'
        verbose_name = '帖子图片'
        verbose_name_plural = '帖子图片'

    ID = models.AutoField(verbose_name="ID",primary_key=True)
    PostID=models.IntegerField(verbose_name="所属帖子ID")
    Uri=models.ImageField(verbose_name="帖子图像",upload_to='PostImage',default='/static/img/header_default.png')


