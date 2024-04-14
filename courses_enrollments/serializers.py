from rest_framework import serializers
from .models import Course, Enrollment


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class DateOnlyField(serializers.Field):
    def to_representation(self, value):
        return value.date()


class EnrollmentSerializer(serializers.ModelSerializer):
    student_name = serializers.CharField(max_length=100)
    course = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all())
    enrollment_date = DateOnlyField(read_only=True)
    class Meta:
        model = Enrollment
        fields = "__all__"
