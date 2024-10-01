from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
def root(request):
    return render(request,'index.html')


def sign_up_by_html(request):
    if request.method == 'POST':
        # Получаем данные:
        username = request.POST.get('username')
        password = request.POST.get('password')
        age = request.POST.get('age')

        print(f'username: {username}')
        print(f'password: {password}')
        print(f'age: {age}')

        return HttpResponse(f'Приветствуем, {username}!')
    return render(request, 'fifth_task/registration_page.html')


def sign_up_by_django(request):
    if request.method == 'POST':
        # Получаем данные:
        username = request.POST.get('username')
        password = request.POST.get('password')
        age = request.POST.get('age')

        print(f'username: {username}')
        print(f'password: {password}')
        print(f'age: {age}')
    return render(request, 'fifth_task/registration_page.html')