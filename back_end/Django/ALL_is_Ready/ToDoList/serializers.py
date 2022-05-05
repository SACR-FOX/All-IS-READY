from rest_framework import serializers
from models.models import ToDoList
import time
class ToDoListSerializer(serializers.ModelSerializer):
    class Meta:
        model=ToDoList
        fields="__all__"
        read_only_fields=("ID",)
        extra_kwargs = {
            "OrgID": {
                "required": False,
                "default": -1
            },
            "UID": {
                "required": True,
                "allow_null": False,
                'write_only': True
            },
            "Time": {
                "required": False,

            },
            "Status": {
                "required": False,
                "default": False
            },
            "Tag": {
                "required": False,
            },
            "UUID": {
                "required": True,
                'write_only': True
            },
            "ItemName":{
                "required": True,
                "allow_null": False,
                "allow_blank": False,
                "max_length": 20
            }
        }

    def validate_Time(self,data):
        if time.time() > data:
            raise serializers.ValidationError(detail="interval invalid")
        return data
