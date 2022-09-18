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

class MyVideosApiView(APIView):
    def get(self, request, username):
        try:
            videos = Video.objects.filter(user__username=username)
            if videos:
                serializer = VideoSerializer(instance=videos, many=True)
                res = {
                    'success':True,
                    'videos':serializer.data
                }
                return Response(data=res, status=status.HTTP_200_OK)
            else:
                return Response(
                            data={"error":"No videos for this user ID {}".format(user_id)},
                            status = status.HTTP_400_BAD_REQUEST)
            
        except Exception as e:
            print(e)
            res = {'success':False, 'data':None, 'errors':str(e)}
            return Response(data=res, status=status.HTTP_400_BAD_REQUEST)

class AddVideoApiView(APIView):

    def post(self, request):
        try:
            src = request.data.get('src')
            print(src)
            if not src:
                return Response(
                            data = {'error':'empty src'}, 
                            status = status.HTTP_400_BAD_REQUEST)

            Video.objects.create(
                            src = src,
                            user_id = request.user.id)

            return Response(data=None, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            res = {'success':False, 'data':None, 'errors':str(e)}
            return Response(data=res, status=status.HTTP_400_BAD_REQUEST)

class VideoDetailApiView(APIView):
    def get(self, request, video_id):
        video = Video.objects.get(id=video_id)
        serializer = VideoSerializer(instance=video)
        res = {
            'video': serializer.data
        }
        return Response(data=res, status=status.HTTP_200_OK)

class VideoLikeApiView(APIView):

    def post(self, request, video_id, *args, **kwargs):
        try:
            like_objs = MetaData.objects.filter(video_id=video_id, user_id=request.user.id)
            if like_objs.exists():
                obj = like_objs[0]
                if obj.is_liked:
                    obj.is_liked = False
                else:
                    obj.is_liked = True
                    obj.is_disliked = False
                obj.save()
            else:
                MetaData.objects.create(
                                    user_id=request.user.id, 
                                    video_id = video_id,
                                    is_liked = True)
        except Exception as e:
            return Response(data={'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response(data=None, status=status.HTTP_200_OK)

class VideoDislikeApiView(APIView):

    def post(self, request, video_id):

        try:
            # Check dislike is already given
            meta_objs = MetaData.objects.filter(video_id=video_id, user_id=request.user.id)
            if meta_objs.exists():
                obj = meta_objs[0]

                # check the video is already disliked or not
                if obj.is_disliked:
                    obj.is_disliked = False
                else:
                    obj.is_disliked = True
                    obj.is_liked = False
                obj.save()
            else:
                # For new like
                MetaData.objects.create(
                                    user_id=request.user.id, 
                                    video_id = video_id,
                                    is_disliked = True)
        except Exception as e:
            return Response(data={'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response(data=None, status=status.HTTP_200_OK)

class VideoLikesApiView(APIView):
    def get(self, request, video_id, *args, **kwargs):
        like_objs = MetaData.objects.filter(video_id=video_id, is_liked=True)
        if like_objs:
            serializer = LikesSerializer(instance=like_objs, many=True)
            res = {
                'likes': serializer.data,
                'success': True
            }
        else:
            res = {
                'likes': None
            }
        return Response(data=res, status=status.HTTP_200_OK)

class DislikesApiView(APIView):

    def get(self, request, video_id, *args, **kwargs):
        dislike_objs = MetaData.objects.filter(video_id=video_id, is_disliked=True)
        if dislike_objs:
            serializer = LikesSerializer(instance=dislike_objs, many=True)
            res = {
                'dislikes': serializer.data,
                'success': True
            }
        else:
            res = {
                'dislikes': None
            }
        return Response(data=res, status=status.HTTP_200_OK)

class VideoViewCountApiView(APIView):

    def post(self, request, video_id):
        video_obj = Video.objects.get(id=video_id)
        view_count = video_obj.view_count+1
        video_obj.view_count = view_count
        video_obj.save()

        return Response(data=None, status=status.HTTP_200_OK)


