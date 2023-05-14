from django.shortcuts import render
import json
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.exceptions import AuthenticationFailed
from . serializer import *
from rest_framework.response import Response
import pymongo
from .models import QuizData
from bson import ObjectId,json_util
from pymongo.mongo_client import MongoClient
uri = "mongodb+srv://thisisvishal:Vishal9634@cluster0.b1vrwir.mongodb.net/?retryWrites=true&w=majority"
from django.conf import settings
my_client = MongoClient(uri)
try:
    my_client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
    
except Exception as e:
    print(e)
dbname = my_client['Heliverse']
collection_name = dbname["quizes_quizdata"]

def welcome(request):
    return HttpResponse("welcome to quiz APIs")

class postQuiz(APIView):
    def post(self, request):
        try:
            serializer = quizSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        except:
            return Response({'result':"wrong data passed"})
    
class getQuiz(APIView):
    def get(self, request,**kwargs):
        try:
            postcode = kwargs.get('postcode', None)
            postcode=ObjectId(postcode)
            filter={"_id":0}
            data=collection_name.find_one({"_id" :postcode},filter)
            return Response(data)
        except:
            return Response({'result':"something went wrong check id again"})

class ansQuiz(APIView):
    def get(self, request,**kwargs):
        try:
            postcode = kwargs.get('postcode', None)
            postcode=ObjectId(postcode)
            filter={"_id":0}
            data=collection_name.find_one({"_id" :postcode},filter)
            opt = data['options'].strip('][').split(', ')
            ansIndex=data['rightAnswer']
            return Response({'ans':opt[ansIndex]})
        except:
            return Response({'result':"something went wrong check id again"})
        
class getQuizes(APIView):
    def parse_json(self,data):
        return json.loads(json_util.dumps(data))
    def get(self, request):
        try:
            data=collection_name.find({})
            x=self.parse_json(data)
            return Response({'ans':x})
        except:
            return Response({'result':"something went wrong"})
class getActiveQuize(APIView):
    def parse_json(self,data):
        return json.loads(json_util.dumps(data))
    def get(self, request):
        try:
            data=collection_name.find({})
            for i in data:
                print(i)
                if i['status']=="active":
                    return Response(self.parse_json(i))
        except:
            return Response({'result':"something went wrong"})