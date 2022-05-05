from rest_framework import serializers
from models.models import *

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        read_only_fields=('Rank','EXP','UID')
        extra_kwargs ={
            "Uname":{
                "required":True,
                "allow_null":False,
                "allow_blank":False
            },
            "Passwd":{
                "required": True,
                "allow_null": False,
                "allow_blank": False,
                "min_length":6,
                'write_only': True
            },
            "OrgID": {
                "required": False,

            },
            "STUID": {
                "required": False,

            },
            "Header": {
                "required": False,
            },
        }
    def validate_Uname(self,data):
        try:
            User.objects.get(Uname__exact=data)
        except Exception:
            return data

        raise serializers.ValidationError(detail="用户名已存在")
