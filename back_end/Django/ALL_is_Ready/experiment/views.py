from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response

import oss2
import os

 # 阿里云账号AccessKey拥有所有API的访问权限，风险很高。强烈建议您创建并使用RAM用户进行API访问或日常运维，请登录RAM控制台创建RAM用户。
auth = oss2.Auth('LTAI5tNtrJxgmQ5pgAMjGoH2', 'BlKZ0n8As55Jqgju1RObVCOsaT1705')
# yourEndpoint填写Bucket所在地域对应的Endpoint。以华东1（杭州）为例，Endpoint填写为https://oss-cn-hangzhou.aliyuncs.com。
# 填写Bucket名称。
bucket = oss2.Bucket(auth, 'oss-cn-hangzhou.aliyuncs.com', 'all-is-ready-file-storage')

cachePath='/Users/lishengdi/lib/oss_test'
class test(APIView):
    authentication_classes = []
    def post(self,request):
        f=request.FILES.get('book')

        if not f:
            return Response({"no file detect"})
        try:
            Path=os.path.join(cachePath,f.name)

            with open(Path,'wb+') as fileobj:
                for chunk in f.chunks():
                    fileobj.write(chunk)

            try:
                bucket.put_object_from_file('user3PDF/Test2.pdf', Path)

            except Exception as e:
                print(e)
                return Response({"oss err"})


        except Exception as e:
            print(e)
            return Response({"save file faild"})

        # 必须以二进制的方式打开文件。
        # 填写本地文件的完整路径。如果未指定本地路径，则默认从示例程序所属项目对应本地路径中上传文件。
        # with open('D:\\localpath\\examplefile.txt', 'rb') as fileobj:
            # Seek方法用于指定从第1000个字节位置开始读写。上传时会从您指定的第1000个字节位置开始上传，直到文件结束。
        # fileobj.seek(1000, os.SEEK_SET)
        # # Tell方法用于返回当前位置。
        # current = fileobj.tell()
        # # 填写Object完整路径。Object完整路径中不能包含Bucket名称。


        try:
            os.remove(Path)
        except Exception as e:
            print(e)
            return Response({"remove error"})

        return Response({"result":"ok"})

    def get(self,request):
        obj="userPDF/Test2.pdf"
        url=bucket.sign_url('GET',obj,3600,slash_safe=True)
        print(url)
        return Response(url)
