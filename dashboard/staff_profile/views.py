from django.shortcuts import render, redirect
from . import services


def index(request):
    return render(request, 'html/index.html')


def main(request):
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
    if request.method == 'GET':
        user_profile = services.get_user_profile(token)
        next_of_kin = user_profile['employee_next_of_kin']
        review = user_profile['employee_review']
        user = user_profile.get('user')
        position = user_profile.get('position')
        print review
        employee = {}
        for key in user_profile:
            if key not in ['employee_next_of_kin', 'employee_review', 'user', 'position']:
                employee[key] = user_profile.get(key)
        return render(request, 'html/profile.html',
                      context={'next_of_kin': next_of_kin,
                               'reviews': review,
                               'user': user,
                               'position': position,
                               'employee': employee
                               }
                      )


def get_logged_in_user(request, token):
    user = services.get_logged_in_user(token)
    return render(request, 'html/main.html')


def get_employees(request, token):
    if request.method == 'GET':
        employees = services.get_employees(token)
        employee_info_list = []
        for employee in employees:
            employee_data = {}
            for data_key in employee:
                if data_key not in ['github_user']:
                    if data_key not in ['position']:
                        if data_key not in ['user']:
                            employee_data[data_key] = employee[data_key]
                        else:
                            employee_data['first_name'] = employee[data_key].get('first_name')
                            employee_data['last_name'] = employee[data_key].get('last_name')
                    else:
                        position_data = employee[data_key]
                        role = position_data.get('name')
                        level = position_data.get('level')
                        employee_data['name'] = role
                        employee_data['level'] = level

            employee_info_list.append(employee_data)
        return render(request, 'html/list_employees.html', context={'all_employees': employee_info_list})


def get_employee_stats(request, token):
    if request.method == 'GET':
        employees = services.get_employees(token)
        print employees
        return render(request, 'html/statistics.html', context={'stats': None})
