from django.core.validators import FileExtensionValidator
from django.db import models
from polymorphic.models import PolymorphicModel
from enum import Enum

from people.utils import phone_number_validator, national_id_validator


class Human(PolymorphicModel):
    name = models.CharField(max_length=40)
    picture = models.ImageField(upload_to='human_pictures/', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True

    @property
    def picture_url(self):
        return self.picture.url if self.picture else None


class Speaker(Human):
    degree = models.CharField(max_length=30)
    place = models.CharField(null=True, blank=True, max_length=50)
    bio = models.TextField()

    @property
    def short_bio(self):
        return '{}'.format(self.degree)


class HoldingTeam(models.Model):
    wss = models.ForeignKey(to='WSS.WSS', related_name='holding_teams', verbose_name='WSS')
    name = models.CharField(max_length=50)
    staff = models.ManyToManyField(to='Staff', related_name='holding_teams', blank=True)

    class Meta:
        ordering = ('pk',)

    def __str__(self):
        return self.name


class Staff(Human):
    class Meta:
        verbose_name_plural = 'Staff'


class Role(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class TechnicalExpert(Human):
    role = models.ForeignKey(to=Role, related_name='technical_experts')


class City(Enum):
    Isfahan = 'اصفهان'
    Tehran = 'تهران'


class Grade(Enum):
    abbas = 'دهم'
    hashtom = 'یازدهم'
    nohom = 'دوازدهم'


class StudentApplication(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    school_name = models.CharField(max_length=100)
    national_id = models.CharField(max_length=10, validators=[national_id_validator])
    city = models.CharField(max_length=40)
    email = models.EmailField(max_length=40)
    phone_number = models.CharField(max_length=20, validators=[phone_number_validator])
    answer = models.FileField(upload_to='answers/', validators=[FileExtensionValidator(['pdf', 'docx'])],
                              help_text='فایل ارسالی می‌تواند فرمت‌های pdf و docx داشته باشد.')
    grade = models.CharField(max_length=7, choices=[(tag.name, tag.value) for tag in Grade],
                             help_text='پایه‌ای که مهر امسال به آن وارد خواهید شد.')
    city_wanted = models.CharField(max_length=7, choices=[(tag.name, tag.value) for tag in City], default='اصفهان')
    request_dorm = models.BooleanField(default=False, help_text='خوابگاه تنها برای مدرسه اصفهان پیش‌بینی شده است.')
    description = models.TextField(max_length=500, null=True, blank=True)
    second_choice_available = models.BooleanField(
        default=False,
        help_text='در صورتی که برای شهر اول پذیرفته نشوم، مایل به حضور در مدرسه شهر دیگر هستم.'
    )

    def __str__(self):
        return self.first_name + ' ' + self.last_name

