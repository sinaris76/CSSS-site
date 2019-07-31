from django import forms
from people.models import *
from captcha.fields import CaptchaField


class RegistrationForm(forms.ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = StudentApplication
        fields = ('first_name', 'last_name', 'school_name', 'city', 'email', 'answer', 'grade', 'city_wanted')
        labels = {
            'first_name': 'نام',
            'last_name': 'نام خانوادگی',
            'school_name': 'نام مدرسه',
            'city': 'شهر',
            'email': 'ایمیل',
            'answer': 'پاسخ به سوالات',
            'grade': 'پایه',
            'city_wanted': 'شهری که می‌خواهید در کلاس‌هایش شرکت کنید'
        }
        label_suffix = ''

