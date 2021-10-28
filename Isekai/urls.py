"""Isekai URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views as myapp_views
from movies import views as movies_views
# from courses.views import CoursesView, DetailsView, CreateView, UpdateView
from courses.views import CoursesView, CreateCoursesView, StudentApiView

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # MYAPP URLS
    path('', myapp_views.index, name="index"),

    # MOVIES URLS
    path('movies/', movies_views.list, name="movies_list"),
    path('movies/create/', movies_views.create, name="movies_create"),
    path('movies/update/<int:movie_id>/', movies_views.update, name="movies_update"),
    path('movies/detail/<int:movie_id>/', movies_views.detail, name="movies_detail"),

    # COURSES URLS
    # path("courses/", CoursesView.as_view(), name="courses_list"),
    # path("courses/create", CreateView.as_view(), name="courses_create"),
    # path('courses/create/<int:course_id>/', UpdateView.as_view(), name="courses_update"),
    # path("courses/detail/<int:course_id>/", DetailsView.as_view(), name="courses_detail"),
    path('courses/list/', CoursesView.as_view()),
    path("courses/create/", CreateCoursesView.as_view(), name="courses_create"),
    path("courses/<int:course_id>/students/", StudentApiView.as_view(), name='students_list')
]
