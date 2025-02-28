from django.urls import path
from .views import get_students, get_student_item

urlpatterns = [
    path('', get_students, name='students_list'),
    path('<int:pk>', get_student_item, name='students_detail'),
]
