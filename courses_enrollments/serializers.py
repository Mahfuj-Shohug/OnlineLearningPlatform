from rest_framework import serializers
from datetime import date
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
        if isinstance(value, date):
            return value.strftime("%Y-%m-%d")
        raise TypeError("Expected a date object")


class EnrollmentSerializer(serializers.ModelSerializer):
    student_name = serializers.CharField(max_length=100)
    enrollment_date = DateOnlyField(read_only=True)

    class Meta:
        model = Enrollment
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        try:
            course = Course.objects.get(id=representation["course"])
            course_info = {
                "id": course.id,
                "title": course.title,
                "price": course.price,
                "duration": course.duration,
                "instructor": course.instructor,
            }
        except Course.DoesNotExist:
            course_info = None

        final_representation = {
            "student_name": representation["student_name"],
            "enrollment_date": representation["enrollment_date"],
            "course_details": course_info,
        }
        return final_representation
