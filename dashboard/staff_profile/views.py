import token

from django.shortcuts import render, redirect
from . import services


def index(request):
    if request.method == 'GET':
        return render(request, 'html/index.html')


def filter_employees(request, token):
    if request.method == 'GET':
        return render(request, 'html/filtering.html', context={'token': token})


def main(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username not in ['', None] and password not in ['', None]:
            response = services.login_user(username, password)
            if 'token' in response:
                return render(request, 'html/main.html', response)
            msg = {'success': 'F', 'message': response.get('non_field_errors')[0]}
            return render(request, 'html/index.html', context=msg)
        else:
            msg = {'success': 'F', 'message': 'Username and Password are required'}
            return render(request, 'html/index.html', context=msg)
    else:
        return render(request, 'html/index.html')


def get_user_profile(request, token):
    if request.method == 'GET':
        user_profile = services.get_user_profile(token)
        next_of_kin = user_profile['employee_next_of_kin']
        review = user_profile['employee_review']
        user = user_profile.get('user')
        position = user_profile.get('position')
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


def prepare_filter_query(filter_data):
    filter_query = ''
    for filter_key in filter_data:
        if filter_key not in ['csrfmiddlewaretoken', 'token']:
            if filter_data.get(filter_key) not in ['', None]:
                if filter_key in ['email']:
                    filter_query += '%s__contains=%s&' % (filter_key, filter_data.get(filter_key))
                else:
                    filter_query += '%s=%s&' % (filter_key, filter_data.get(filter_key))

    return filter_query


def get_employees(request):
    if request.method == 'POST':
        employee_filtering_data = request.POST
        token = employee_filtering_data.get('token')
        filter_query = prepare_filter_query(employee_filtering_data)
        employees = services.filter_employees(token, filter_query)
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
        stats = {}
        employees = services.get_employees(token)
        print employees[0].keys()
        stats['no_of_employees'] = len(employees)
        stats['frontend'] = len(
                [ employee for employee in employees if employee.get('position')['name'] in ['Front-end Developer']])
        stats['backend'] = len(
                [ employee for employee in employees if employee.get('position')['name'] in ['Back-end Developer']])
        stats['projectmanager'] = len(
                [employee for employee in employees if employee.get('position')['name'] in ['Project Manager']])
        stats['gender_male'] = len([employee for employee in employees if employee.get('gender') in ['M']])
        stats['gender_female'] = len([employee for employee in employees if employee.get('gender') in ['F']])
        stats['race_B'] = len([employee for employee in employees if employee.get('race') in ['B']])
        stats['race_C'] = len([employee for employee in employees if employee.get('race') in ['C']])
        stats['race_I'] = len([employee for employee in employees if employee.get('race') in ['I']])
        stats['race_W'] = len([employee for employee in employees if employee.get('race') in ['W']])
        stats['race_N'] = len([employee for employee in employees if employee.get('race') in ['N']])
        return render(request, 'html/statistics.html', context=stats)
