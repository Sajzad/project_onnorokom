import json, os

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import permissions

from django.contrib.auth.models import User

from .serializers import *

from base.models import *

class VideoApiView(APIView):
    def get(self, request):
        print("sdfsd")
        try:
            videos = Video.objects.all()
            serializer = VideoSerializer(instance=videos, many=True)
            res = {
                'success':True,
                'videos':serializer.data
            }
            return Response(data=res, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            res = {'success':False, 'data':None, 'errors':str(e)}
            return Response(data=res, status=status.HTTP_400_BAD_REQUEST)  

