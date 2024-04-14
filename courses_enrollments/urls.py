# urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Home page
    path("", views.home, name="home"),
    # Course API
    path("courses", views.get_courses, name="get_courses"),
    path("courses/<int:course_id>", views.get_course_by_id, name="get_course_by_id"),
    path("courses/create", views.create_course, name="create_course"),
    # Enrollment API
    path("enrollments", views.enroll_student, name="enroll_student"),
    path("enrollments/validate", views.validate_enrollment, name="validate_enrollment"),
]
