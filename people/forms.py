from django import forms
from people.models import *
from captcha.fields import CaptchaField


class RegistrationForm(forms.ModelForm):
    captcha = CaptchaField(label='حروف تصویر زیر را وارد کنید.')

    class Meta:
        model = StudentApplication
        fields = ('first_name', 'last_name', 'national_id', 'phone_number', 'email', 'school_name', 'city', 'answer', 'grade',
                  'city_wanted', 'second_choice_available', 'request_dorm', 'description')
        labels = {
            'first_name': 'نام',
            'last_name': 'نام خانوادگی',
            'national_id': 'کد ملی',
            'school_name': 'نام مدرسه',
            'city': 'شهر محل سکونت',
            'email': 'ایمیل',
            'phone_number': 'شماره تلفن همراه',
            'answer': 'پاسخ به سوالات',
            'grade': 'پایه',
            'city_wanted': 'کدام شهر اولویت اول شما برای حضور در مدرسه است؟',
            'second_choice_available':  'امکان‌پذیری اولویت دوم',
            'request_dorm': 'درخواست خوابگاه دارم. (لطفا شیوه‌نامهٔ خوابگاه را در بالا مطالعه کنید.)',
            'description': 'توضیحات بیشتر'
        }

        label_suffix = ''
