from rest_framework import generics
from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from . import serializers
from .models import Course


def list_(resquest):
    courses = Course.objects.all()
    context = {
        'courses': courses,
    }
    return render(resquest, 'courses/list.html', context)


def detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    context = {
        'course': course,
    }
    return render(request, 'courses/detail.html', context)


class ListCreateCourse(APIView):
    def get(self, request, format=None):
        courses = Course.objects.all()
        serializer = serializers.CourseSerializer(courses, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = serializers.CourseSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
