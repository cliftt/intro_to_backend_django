from django.shortcuts import render
from .models import Course

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'indexsub.html', {'courses': courses})
def get_course_item(request, pk):
    course = Course.objects.get(id=pk)
    return render(request, 'courses-details.html', {'course': course})
