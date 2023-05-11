from django.urls import path 
from  . import views

urlpatterns = {
    path('course/', views.course_index,name='course-index')
}