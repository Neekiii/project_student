from rest_framework import serializers
from app_students.models import StudentModel
from app_courses.models import CourseModel

class CourseSerializer(serializers.ModelSerializer):
     class Meta:
          fields =["id","course_name","course_code"]
          model = CourseModel

class StudentSerializer(serializers.ModelSerializer):
     class Meta:
          fields=["id","first_name","middle_name","last_name","email","contact","address","course","current_degree","user"]          
          model = StudentModel