import re
from django.core.exceptions import ValidationError


def english_digits(s):
    s = str(s)
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    return re.sub(r'۰|۱|۲|۳|۴|۵|۶|۷|۸|۹', lambda c: digits[int(c.group())], s)


def phone_number_validator(phone_number):
    """
    validate a phone number
    valid patterns are: +9999999999, 0999999999, +۹۸۹۹۹۹۹۹۹۹, ۰۹۹۹۹۹۹۹۹۹
    """
    phone_number = english_digits(phone_number)
    regex = re.compile("^\+?\d{4,13}$")
    if not regex.match(phone_number):
        raise ValidationError(
            'شماره همراه معتبر وارد کنید.'
        )

