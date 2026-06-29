from django.shortcuts import render
from .models import StudentStudentdetail
from django.core.paginator import Paginator
# Create your views here.
def home(request):
    students_obj = StudentStudentdetail.objects.all()

    p = Paginator(students_obj,20)
    page = request.GET.get('page')
    print(page)
    if not page:
        page = 1
    minus_range =[]
    plus_range=[]
    students = p.page(page)
    if students.has_previous():
        # print("yesss")
        num = students.previous_page_number()
        if num - 5 < 1:
            start = 1
        else:
            start = num - 5
        for i in range(start,num):
            minus_range.append(i)
    if students.has_next():
        # print("yesss")
        num = students.next_page_number()
        last = students.paginator.num_pages
        if num + 5 > last:
            end = last
        else:
            end = num + 5
        for i in range(num,end):
            plus_range.append(i)
        # print(minus_range)
    return render(request, 'sample/home.html', {'students':students, 'minus_range':minus_range,'plus_range':plus_range})