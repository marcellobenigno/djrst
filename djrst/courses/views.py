from django.shortcuts import get_object_or_404
from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.decorators import detail_route
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from . import serializers
from .models import Course, Review


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


class ListCreateCourse(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = serializers.CourseSerializer


class RetrieveUpdateDestroyCourse(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = serializers.CourseSerializer


class ListCreateReview(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = serializers.ReviewSerializer

    def get_queryset(self):
        return self.queryset.filter(course_id=self.kwargs.get('course_pk'))

    def perform_create(self, serializer):
        course = get_object_or_404(Course, pk=self.kwargs.get('course_pk'))
        serializer.save(course=course)


class RetrieveUpdateDestroyReview(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = serializers.ReviewSerializer

    def get_object(self):
        return get_object_or_404(
            self.get_queryset(),
            course_id=self.kwargs.get('course_pk'),
            pk=self.kwargs.get('pk')
        )


class CourseViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Course.objects.all()
    serializer_class = serializers.CourseSerializer

    # detalhe da url:
    # v2/cursos/1/avaliacoes/
    @detail_route(methods=['get', 'post', 'put'])
    def avaliacoes(self, request, pk=None):
        course = self.get_object()
        serializer = serializers.ReviewSerializer(
            course.reviews.all(), many=True)
        return Response(serializer.data)


class ReviewViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Review.objects.all()
    serializer_class = serializers.ReviewSerializer
