from rest_framework import serializers
from models.models import Community,CommunityTopic,TopicPost,PostImage
import time


class CommunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Community
        fields = "__all__"
        read_only_fields = ('CommunityID','PostCount','Renewal')
        extra_kwargs = {
            "CommunityName":{
                "required": True,
                "allow_null": False,
                "allow_blank": False,
                "max_length": 20
            },
            "AdministratorID":{
                "required": True,
                "allow_null": False,

            },
            "Poster":{
                "required": False,
            },
            "Description":{
                "required": False,
                "max_length": 256,
                "default":"该社区还未设置相应描述"
            }
        }

    def validate_CommunityName(self, data):
        try:
            Community.objects.get(CommunityName__exact=data)
        except Exception:
            return data

        raise serializers.ValidationError(detail="社区名已存在")



#
class TopicSerializers(serializers.ModelSerializer):

    class Meta:
        model = CommunityTopic
        fields = "__all__"
        read_only_fields = ('CommunityID','TopicID','Creator','Time')
        extra_kwargs = {
            "CommunityID":{
                "required": True,
                "allow_null": False,
            },
            "HasImage":{
                "required": True,
                "allow_null": False,
            },
            "Title":{
                "required": True,
                "allow_null": False,
                "allow_blank": False,
                "max_length": 35
            },
            "ImageUri":{
                "required": False
            }

        }

class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = TopicPost
        fields = "__all__"
        read_only_fields = ('TopicID','UID','PostID','Time')
        extra_kwargs = {

            "HasImage":{
                "required": True,
                "allow_null": False,
            },
            "Content":{
                "required": True,
                "allow_null": False,
                "allow_blank": False,
                "max_length": 300
            }

        }