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


def get_user_profile(request):
    pass


def get_logged_in_user(request):
    pass


def get_employees(request):
    pass


def get_employee_stats(request):
    pass
