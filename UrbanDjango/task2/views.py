from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'index.html')


def class_template(request):
    return render(request, 'second_task\\class_template.html')


def func_template(request):
    return render(request, 'second_task\\func_template.html')
