from django.shortcuts import render
from .models import teacherTimeSheet


def index(request):
    teacher_time = teacherTimeSheet.objects.all
    context = {'teacher_time': teacher_time}
    return render(request, 'app/basic.html', context)