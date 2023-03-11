from django.urls import path
from .views import (
    CourseDetailView, 
    CourseListView,
    CourseCreateView
)

app_name = "Courses"
urlpatterns = [
    path('', CourseListView.as_view(), name='courses-list'),
    path('<int:id>/', CourseDetailView.as_view(), name='courses-detail'),
    path('create/', CourseCreateView.as_view(), name='course-create')
]