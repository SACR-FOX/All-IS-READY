from rest_framework import serializers
from models.models import Schedule

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = "__all__"
        read_only_fields=('ScheduleID',)
        extra_kwargs ={
            "DurationStart":{
                "required":True,
                "allow_null":False,
            },
            "DurationEnd":{
                "required": True,
                "allow_null": False,
            },
            "Day": {
                "required": False,
                'write_only': True
            },
            "CurName": {
                "required": True,
                "allow_null": False,
                "allow_blank": False,
                "max_length":20
            },
            "Tag": {
                "required": False,
            },
            "Loaction":{
                "required":False,
                "max_length": 20,
                "default":"未设置教室位置"
            },
            "UID":{
                "required":True,
                "allow_null": False,
                "write_only":True
            },
            "OrgID": {
                "required": False,
                "default":-1,
                "write_only": True
            },
            "UUID":{
                "required":True,
                "write_only":True
            }

        }