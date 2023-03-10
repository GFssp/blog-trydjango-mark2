from django.urls import path
from .views import (
    CourseDetailView, 
    CourseListView
)

app_name = "Courses"
urlpatterns = [
    path('', CourseDetailView.as_view(), name='courses-list'),
    path('<int:id>/', CourseDetailView.as_view(), name='courses-detail'),
    path('list/', CourseListView.as_view(), name='course-list')
]