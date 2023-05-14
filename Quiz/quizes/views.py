from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.exceptions import AuthenticationFailed
from . serializer import *
from rest_framework.response import Response
import pymongo
from .models import QuizData
from bson import ObjectId

connect_string="mongodb://localhost:27017"
from django.conf import settings
my_client = pymongo.MongoClient(connect_string)
dbname = my_client['Heliverse']
collection_name = dbname["quizes_quizdata"]

class postQuiz(APIView):
    def post(self, request):
        serializer = quizSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
class getQuiz(APIView):
    def get(self, request,**kwargs):
        postcode = kwargs.get('postcode', None)
        postcode=ObjectId(postcode)
        filter={"_id":0}
        data=collection_name.find_one({"_id" :postcode},filter)
        return Response(data)