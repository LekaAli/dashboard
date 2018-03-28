from django.test import TestCase
from .services import login_user, get_user_profile, get_employees, filter_employees


class EmployeeTesCases(TestCase):


    def test_login_user(self):
        login_credentials = {'username': 'pravin.gordhan', 'password': 'pravin.gordhan'}
        login_results = login_user(**login_credentials)
        self.assertIn('token', login_results)
        self.assertTrue(login_results.get('token') != '')

    def test_get_user_profile(self):
        token = '2a3d1af2f3f6d1cddaa3012c1c465fcbdffa3678'
        user_profile = get_user_profile(token)
        user_profile_info = [
            u'is_employed',
            u'id_number',
            u'employee_next_of_kin',
            u'visa_document',
            u'id',
            u'github_user',
            u'personal_email',
            u'is_foreigner',
            u'start_date',
            u'phone_number',
            u'physical_address',
            u'end_date',
            u'employee_review',
            u'next_review',
            u'id_document',
            u'user',
            u'position',
            u'leave_remaining',
            u'gender', u'age',
            u'days_to_birthday',
            u'email',
            u'race',
            u'birth_date',
            u'years_worked',
            u'tax_number']
        self.assertListEqual(user_profile_info, user_profile.keys())

    def test_get_employees(self):
        token = '2a3d1af2f3f6d1cddaa3012c1c465fcbdffa3678'
        employees = get_employees(token)
        employee_info = [
            u'phone_number',
            u'gender',
            u'github_user',
            u'days_to_birthday',
            u'age',
            u'race',
            u'user',
            u'years_worked',
            u'birth_date',
            u'position',
            u'email']
        self.assertTrue(type(employees) == type(employee_info))
        for employee in employees:
            self.assertTrue(type(employee) == type({}))
            self.assertListEqual(employee_info, employee.keys())


