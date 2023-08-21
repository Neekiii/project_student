from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework.views import APIView
from app_api.serializers import CourseSerializer,StudentSerializer
from app_courses.models import CourseModel
from app_students.models import StudentModel

# Create your views here.
class CourseApiView(APIView):
    def get(self,request):
        course_obj= CourseModel.objects.all()

        serializer=CourseSerializer(course_obj,many=True)

        return Response(serializer.data)
    
    def post(self,request):
       
        serializer= CourseSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
class CourseApiIdView(APIView):
    def get_objects(self,id):
        try:
            course_obj = CourseModel.objects.get(id=id)
            return course_obj
        except CourseModel.DoesNotExist:
            return None

    def get(self,request,id):
        instance = self.get_objects(id)
        if instance is None:
            return Response({"error": "No data found"})
        serializer= CourseSerializer(instance)
        return Response(serializer.data)
        
    def put(self,request,id):
        instance = self.get_objects(id)
        if instance is None:
            return Response({"error": "No data found"})

        serializer=CourseSerializer(instance=instance,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def delete(self,request,id):
        instance = self.get_objects(id)
        if instance is None:
            return Response({"error": "No data found"})
        instance.delete()
        return Response({"message":"data deleted successfully"})
        
class StudentApiView(APIView):
    def get (self,request):
        std_obj = StudentModel.objects.all()
        serializer = StudentSerializer(std_obj,many=True)
        return Response (serializer.data)
    
    def post(self,request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
             serializer.save()
             return Response(serializer.data)
        return Response(serializer.errors)
