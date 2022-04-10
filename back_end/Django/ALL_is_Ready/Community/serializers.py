from rest_framework import serializers
from models.models import Community,CommunityTopic,TopicPost,PostImage
import time


class CommunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Community
        fields = "__all__"
        read_only_fields = ('CommunityID','PostCount','Renewal')
        extra_kwargs = {


        }