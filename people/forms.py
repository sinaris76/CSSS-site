import requests
from django import forms
from people.models import *


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = StudentApplication
        fields = ('first_name', 'last_name', 'phone_number', 'email', 'school_name', 'city', 'answer', 'grade',
                  'city_wanted', 'request_dorm', 'description')
        labels = {
            'first_name': 'نام',
            'last_name': 'نام خانوادگی',
            'school_name': 'نام مدرسه',
            'city': 'شهر محل سکونت',
            'email': 'ایمیل',
            'phone_number': 'شماره تلفن همراه',
            'answer': 'پاسخ به سوالات',
            'grade': 'پایه',
            'city_wanted': 'مایل به شرکت در مدرسهٔ کدام شهر هستید؟',
            'request_dorm': 'درخواست خوابگاه دارم.',
            'description': 'توضیحات بیشتر'
        }
        label_suffix = ''

