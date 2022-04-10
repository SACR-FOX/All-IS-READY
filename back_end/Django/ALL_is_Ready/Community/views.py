import json
import time
from django.db.models import Q

from models.models import Organization,User,OrgTask,TaskAck
from . serializers import CommunitySerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.views import APIView
from datetime import datetime
from tools.timeTool import switcher
from django.core.cache import cache
import uuid