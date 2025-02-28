from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse  # Добавляем HttpResponse для быстрой заглушки

# Функция для главной страницы
def home_view(request):
    return HttpResponse("<h1>Welcome to my Django project</h1><p>Go to <a href='/students/'>Students</a> or <a href='/subjects/'>Subjects</a></p>")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', include('students.urls')),
    path('subjects/', include('subjects.urls')),
    path('', home_view, name='home'),  # Маршрут для главной страницы
]
