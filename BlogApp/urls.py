from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('blog.urls')),
    path('courses/', include('Courses.urls'))
]
