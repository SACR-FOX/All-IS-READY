from rest_framework import serializers
from models.models import Organization,OrgTask,TaskAck
import time

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = "__all__"
        read_only_fields = ('OrgID',)
        extra_kwargs = {
            "OrgName":{
                "required": True,
                "allow_null": False,
                "allow_blank": False,
                "max_length": 25
            },
            "MonitorID":{
                "required": False,
                "default":-1
            },
            "Description":{
                "required": False,
                "default":"该组织还没有设置简介～"
            }

        }

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrgTask
        fields = "__all__"
        read_only_fields = ('TaskID','AckCount',)
        extra_kwargs = {
            "OrgID":{
                "required": True,
                "allow_null": False,

            },
            "TimeStart":{
                "required": True,
                "allow_null": False,
            },
            "TimeDue": {
                "required": True,
                "allow_null": False,
            },
            "Status": {
                "required": False,
                "default": False
            },
            "CID":{
                "required": False,
                "default":-1
            },
            "Description": {
                "required": False,
                "default": "该任务无详细描述"
            },
            "TaskName":{
                "required": True,
                "allow_null": False,
                "allow_blank": False,
                "max_length":30
            },
            "Creator": {
                "required": False,
                "default": "anonymous"
            },
            "AckCount":{
                "required": False,
                "default": 0
            }
        }

    def validate_TimeDue(self,data):
        if time.time() > data:
            raise serializers.ValidationError(detail="interval invalid")
        return data

class AckSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskAck
        fields = "__all__"
        read_only_fields = ('TaskID', 'UID',)
        extra_kwargs = {
            "TaskID": {
                "required": True,
                "allow_null": False,
            },
            "UID": {
                "required": True,
                "allow_null": False,
            },
        }
