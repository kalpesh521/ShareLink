from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *

def home(request):
    return render(request,'home.html')
def download(request,uid):
    return render(request,'download.html',context={'uid':uid})


class HandleFileUpload(APIView):
    def post(self,request):
        try:
            
            data=request.data
            serializer= FileListSerializer(data=data)
            
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status':200,
                    'message':'Successfully uploaded file',
                    'data':serializer.data,
                })
            return Response({
                    'status':400,
                    'message':'Something went wrong',
                    'data':serializer.errors,
                    })
        except Exception as e : 
              print(e) 
        