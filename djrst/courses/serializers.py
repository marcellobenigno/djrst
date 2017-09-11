from rest_framework import serializers

from . import models


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {
            'email': {'write_only': True}
        }
        fields = '__all__'
        model = models.Review


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.Course
