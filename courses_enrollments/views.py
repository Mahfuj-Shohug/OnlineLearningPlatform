from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Course, Enrollment
from .serializers import CourseSerializer, EnrollmentSerializer


# Course Service
@api_view(["GET"])
def get_courses(request):
    instructor = request.query_params.get("instructor")
    price = request.query_params.get("price")
    duration = request.query_params.get("duration")
    title = request.query_params.get("title")

    queryset = Course.objects.all()

    if instructor:
        queryset = queryset.filter(instructor__icontains=instructor)
    if price:
        queryset = queryset.filter(price=price)
    if duration:
        queryset = queryset.filter(duration=duration)
    if title:
        queryset = queryset.filter(title__icontains=title)

    serializer = CourseSerializer(queryset, many=True)

    response_data = {
        "success": True,
        "message": "Retrieve data successfully",
        "courses": serializer.data,
    }

    if not queryset.exists():
        response_data["success"] = False
        response_data["message"] = "Data is empty"

    return Response(response_data)


@api_view(["GET"])
def get_course_by_id(request, course_id):
    try:
        course = Course.objects.get(pk=course_id)
        serializer = CourseSerializer(course)
        response_data = {
            "success": True,
            "message": "Retrieve data successfully",
            "data": serializer.data,
        }
        return Response(response_data)
    except Course.DoesNotExist:
        response_data = {
            "success": False,
            "message": "Course not found",
        }
        return Response(response_data, status=status.HTTP_404_NOT_FOUND)


@api_view(["POST"])
def create_course(request):
    serializer = CourseSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
    student_name = request.data.get("student_name", "")
    course_id = request.data.get("course_id", None)

    try:
        course = Course.objects.get(pk=course_id)
    except Course.DoesNotExist:
        return Response(
            {"error": "Course does not exist"}, status=status.HTTP_400_BAD_REQUEST
        )

    if not student_name:
        return Response(
            {"error": "Student name is required"}, status=status.HTTP_400_BAD_REQUEST
        )

    return Response({"message": "Enrollment is valid"}, status=status.HTTP_200_OK)
