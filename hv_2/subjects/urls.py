from django.urls import path
from .views import course_list, get_course_item

urlpatterns = [
    path('', course_list),
    path('<int:pk>', get_course_item, name='courses_list'),
]