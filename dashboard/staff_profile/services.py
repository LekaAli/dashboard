import requests


def login_user(username, password):
    url = 'http://staging.tangent.tngnt.co/api-token-auth/'
    params = {'username': username, 'password': password}
    response = requests.post(url, params)
    data = response.json()
    return data


def get_logged_in_user(token):
    url = 'http://staging.tangent.tngnt.co/api/user/me/'
    param = {'token': token}
    response = requests.get(url, param)
    logged_in_user = response.json()
    return logged_in_user


def get_user_profile(token):
    url = 'http://staging.tangent.tngnt.co/api/employee/me/'
    param = {'token': token}
    response = requests.get(url, param)
    user_profile = response.json()
    return user_profile


def get_employees():
    url = 'http://staging.tangent.tngnt.co/api/employee/'
    response = requests.get(url)
    employees_info = response.json()
    return employees_info

