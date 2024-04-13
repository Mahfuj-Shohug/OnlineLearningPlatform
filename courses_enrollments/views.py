from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Course, Enrollment
from .serializers import CourseSerializer, EnrollmentSerializer


# Course Service
@api_view(["GET"])
def get_courses(request):
    courses = Course.objects.all()
    serializer = CourseSerializer(courses, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def create_course(request):
    serializer = CourseSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def get_course_by_id(request, course_id):
    try:
        course = Course.objects.get(pk=course_id)
    except Course.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = CourseSerializer(course)
    return Response(serializer.data)


# Enrollment Service
@api_view(["POST"])
def enroll_student(request):
    serializer = EnrollmentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def validate_enrollment(request):
    # Add validation logic here based on your requirements
    return Response({"message": "Validation successful"}, status=status.HTTP_200_OK)
