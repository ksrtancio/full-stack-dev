from django.http import response
from django.http import request
from django.http.response import HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views import View
from django.urls import reverse
from courses.models import Course, Student

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView

# Create your views here.

# class CoursesView(View):
#     def get(self, request):
#         courses = Course.objects.all()
#         context = {
#             "courses" : courses
#         }
#         return render(request, "courses.html", context)

# class DetailsView(View):
    
#     def get(self, request, course_id):
#         print(f"COURSE ID: {course_id}")
#         course = Course.objects.get(id=course_id)
#         context = {
#             "title": "Courses",
#             "course" : course,
#         }
#         return render(request, "detail2.html", context)

# class CreateView(View):
    
#     def get(self, request):
#         context={
#             "title" : "Create Course"
#         }
#         return render(request, "create2.html", context)
    
#     def post(self, request):
#         name = request.POST["name"]
#         semester = request.POST["semester"]

#         Course.objects.create(name=name, semester=semester)

#         return HttpResponseRedirect(reverse("courses_list"))

# class UpdateView(View):

#     def get(self, request, course_id):
#         course = Course.objects.get(id=course_id)
#         context={
#             "title": "Edit Course",
#             "course" : course
#         }
#         return render(request, "update2.html", context)
    
#     def post(self, request, course_id):
#         course = get_object_or_404(Course, id=course_id)
#         course.name = request.POST["name"]
#         course.semester = request.POST["semester"]
#         course.save()
#         return HttpResponseRedirect(reverse("courses_detail", kwargs={"course_id":course_id}))

class CoursesView(ListView):
    model = Course
    template_name = 'courses/list.html'
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['courses'] = Course.objects.all()
        return context

class CreateCoursesView(CreateView):
    model = Course
    fields = ['name', 'semester']
    success_url = '/courses/list'

class StudentApiView(View):
    def get(self, *args, **kwargs):
        course_id = kwargs.get('course_id')
        course = Course.objects.get(id=course_id)
        context = {'course': course, 'students': course.student_set.all()}
        return render(self.request, 'courses/student_list.html', context)
    
    def post(self, *args, **kwargs):
        data = self.request.POST
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        course_id = kwargs.get('course_id')
        course = Course.objects.get(id=course_id)

        student = Student.objects.create(first_name=first_name, last_name=last_name, course=course)

        response_data = {}
        response_data['first_name'] = student.first_name
        response_data['last_name'] = student.last_name

        return JsonResponse(response_data)
        