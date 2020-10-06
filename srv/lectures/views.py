from django.shortcuts import render, get_object_or_404
from .models import Lecture


def show_list(request):
    lectures = Lecture.opened.all()
    return render(request, 'lectures/list.html', {'lecs': lectures})


def show_lecture(request, lec_slug):
    lecture = get_object_or_404(Lecture, slug=lec_slug, status='opened')
    return render(request, 'lectures/lecture.html', {'lec': lecture})
