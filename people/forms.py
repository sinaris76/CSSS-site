from django import forms
from people.models import *


class RegistrationForm(forms.ModelForm):

    class Meta:
        model = StudentApplication
        fields = ('first_name', 'last_name', 'school_name', 'city', 'email', 'answer', 'grade', 'city_wanted')
