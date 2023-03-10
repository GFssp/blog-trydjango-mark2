from django.urls import path
from .views import (
    CourseView
)

app_name = "Courses"
urlpatterns = [
    path('', CourseView.as_view(template_name="about.html"), name='courses-list'),
]