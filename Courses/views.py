from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import CourseModel
from .forms import CourseModelForm

class CourseCreateView(View):
    template_name = 'course_create.html'
    def get_object(self):
        context = {}
        id = self.kwargs.get('id')
        obj = None
        if id is not None:
            obj = get_object_or_404(CourseModel, id=id)
            context['object'] = obj
        return obj

    def get(self, request, *args, **kwargs):
        context = {}
        obj = self.get_object() # Show the object created
        if obj is None:
            form = CourseModelForm(instance=obj)
            context['object'] = obj
            context['form'] = form
        return render(request, self.template_name, context=context)
    
    def post(self, request, *args, **kwargs):
        form = CourseModelForm(request.POST)
        obj = self.get_object()
        if form.is_valid():
            form.save()
            form = CourseModelForm(request.POST, instance=obj)
        context = {"form": form}
        return render(request, self.template_name, context=context)

class CourseListView(View):
    template_name = "course_list.html"
    queryset = CourseModel.objects.all()

    def get_queryset(self):
        return self.queryset # Opcional

    def get(self, request, *args, **kwargs):
        context = {'object_list': self.get_queryset()}
        return render(request, self.template_name, context)
    
class CourseDetailView(View):
    template_name = 'course_detail.html'
    def get(self, request, id=None, *args, **kwargs):
        context = {}
        if id is not None:
            obj = get_object_or_404(CourseModel, id=id)
            context['object'] = obj
        return render(request, self.template_name, context=context)
    
