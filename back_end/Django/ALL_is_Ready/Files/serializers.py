from rest_framework import serializers
from models.models import FileModel

class FileSerializers(serializers.ModelSerializer):
    class Meta:
        model = FileModel
        fields = "__all__"
        read_only_fields=('ID',)
        extra_kwargs ={
            "FolderName":{
                "required":True,
                "allow_null":False,
                "allow_blank": False,
                "max_length":15
            },
            "FileName": {
                "required": True,
                "allow_null": False,
                "allow_blank": False,
                "max_length": 50
            },
            "OrgID":{
                "required": False,
                "default": -1
            },
            "Renewal":{
                "required": False,
                "default": 0
            }
        }