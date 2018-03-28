import requests


def login_user(username, password):
    url = 'http://staging.tangent.tngnt.co/api-token-auth/'
    params = {'username': username, 'password': password}
    response = requests.post(url, params)
    data = response.json()
    return data


def get_user_profile(token):
    url = 'http://staging.tangent.tngnt.co/api/employee/me/'
    response = requests.get(url, headers=prep_header(token))
    user_profile = response.json()
    return user_profile


def get_employees(token):
    url = 'http://staging.tangent.tngnt.co/api/employee/'
    response = requests.get(url, headers=prep_header(token))
    employees_info = response.json()
    return employees_info


def filter_employees(token, filter_data):
    if filter_data not in ['', None]:
        url = 'http://staging.tangent.tngnt.co/api/employee/?%s' % filter_data
    else:
        url = 'http://staging.tangent.tngnt.co/api/employee/'
    response = requests.get(url, headers=prep_header(token))
    employees_info = response.json()
    return employees_info


def prep_header(token):
    token = ' '.join(['token', token])
    header = {'Authorization': token}
    return header
