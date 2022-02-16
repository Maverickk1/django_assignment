from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from studentdata.models import Student,Address
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter


 
@api_view()
def home(request):
    student_obj=Student.objects.all()
    s = StudentSerializer(student_obj,many=True)
    return Response(s.data)

@api_view(['GET'])
def byid(request,id):
    students=Student.objects.get(id=id)
    s=StudentSerializer(students)
    return Response(s.data)

class StudentList(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class=StudentSerializer
    filter_backends=[DjangoFilterBackend,SearchFilter]
    filterset_fields = ['standard']



