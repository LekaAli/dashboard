from django.shortcuts import render
from django.shortcuts import redirect
from . import services


def index(request):
    return render(request, 'html/index.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username not in ['', None] and password not in ['', None]:
            response = services.login_user(username, password)
            if 'token' in response:
                return render(request, 'html/main.html', response)
            msg = {'success': 'F', 'message': response.get('non_field_errors')[0]}
            return render(request, 'html/index.html', msg)
        else:
            msg = {'success': 'F', 'message': 'Username and Password are required'}
            return render(request, 'html/index.html', msg)
    else:
        return render(request, 'html/index.html')


def get_user_profile(request, token):
    user_profile = services.get_user_profile(token)
    return render(request, '', context={})


def get_logged_in_user(request, token):
    user = services.get_logged_in_user(token)
    return render(request, '', context={})


def get_employees(request):
    employees = services.get_employees()
    return render(request, '', context= {})


def get_employee_stats(request):
    employees = services.get_employees()
    return render(request, '', context={})
