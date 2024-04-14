from rest_framework import serializers
from .models import Course, Enrollment


class CourseSerializer(serializers.ModelSerializer):
    enrollment_count = serializers.SerializerMethodField()
    enrolled_students = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = "__all__"

    def get_enrollment_count(self, obj):
        return Enrollment.objects.filter(course=obj).count()

    def get_enrolled_students(self, obj):
        enrolled_students = Enrollment.objects.filter(course=obj)
        return [
            {
                "student_name": enrollment.student_name,
                "enrollment_date": enrollment.enrollment_date,
            }
            for enrollment in enrolled_students
        ]


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
