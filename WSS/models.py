from django.db import models
from django.utils.safestring import mark_safe
from sorl.thumbnail import ImageField

from events.models import Workshop, Seminar
from people.models import Staff


class WSS(models.Model):
    year = models.PositiveSmallIntegerField()
    description = models.TextField()
    registration_link = models.URLField(null=True, blank=True)
    proposal_link = models.URLField(null=True, blank=True)
    start_date = models.DateField()
    start_date_isf = models.DateField(null=True)
    start_date_teh = models.DateField(null=True)
    end_date = models.DateField()
    main_clip = models.OneToOneField(to='Clip', null=True, blank=True, related_name='+')
    main_image = models.OneToOneField(to='Image', null=True, blank=True, related_name='+')

    class Meta:
        ordering = ('-year',)
        verbose_name = 'Winter Seminar Series'
        verbose_name_plural = 'Winter Seminar Series'

    def __str__(self):
        return 'مدرسه تابستانه علوم کامپیوتر {}'.format(self.year)

    @property
    def main_image_url(self):
        if not self.main_image:
            return None
        return self.main_image.image.url

    @property
    def main_clip_url(self):
        if not self.main_clip:
            return None
        return self.main_clip.clip.url

    @property
    def workshops(self):
        return Workshop.objects.filter(wss=self)

    @property
    def seminars(self):
        return Seminar.objects.filter(wss=self)

    @property
    def staff_count(self):
        return len(set().union(
            *[holding_team.staff.values_list('pk') for holding_team in self.holding_teams.all()]
        ))

    @property
    def staff(self):
        staff = Staff.objects.all()
        return staff

    @property
    def keynote_seminars(self):
        return self.seminars.filter(is_keynote=True)

    @property
    def non_keynote_seminars(self):
        return self.seminars.filter(is_keynote=False)

    @property
    def main_sponsorships(self):
        return self.sponsorships.filter(is_main=True)

    @property
    def not_main_sponsorships(self):
        return self.sponsorships.filter(is_main=False)

    @classmethod
    def active_wss(cls):
        return cls.objects.first()

    @property
    def is_active(self):
        return self.pk == WSS.active_wss().pk


class Clip(models.Model):
    wss = models.ForeignKey(to='WSS', related_name='clips', verbose_name='WSS')
    clip = models.FileField(upload_to='clips/')

    def __str__(self):
        return 'Clip of {}'.format(self.wss)


class Image(models.Model):
    wss = models.ForeignKey(to='WSS', related_name='images', verbose_name='WSS')
    image = ImageField(upload_to='images/')

    def __str__(self):
        return 'Image of {}'.format(self.wss)


class Sponsor(models.Model):
    name = models.CharField(max_length=70)
    logo = models.ImageField(upload_to='logos/')
    url = models.URLField()

    def __str__(self):
        return self.name

    def logo_tag(self):
        if not self.logo:
            return None
        return mark_safe('<img src={} width=40 height=40>'.format(self.logo.url))

    logo_tag.short_description = 'logo'


class Sponsorship(models.Model):
    wss = models.ForeignKey(to='WSS', related_name='sponsorships')
    sponsor = models.ForeignKey(to=Sponsor, related_name='sponsorships')
    is_main = models.BooleanField()

    def __str__(self):
        return self.sponsor.name

    @property
    def logo_url(self):
        if not self.sponsor.logo:
            return None
        return self.sponsor.logo.url


class ExternalLink(models.Model):
    type = models.CharField(max_length=40)
    title = models.CharField(max_length=40)
    url = models.URLField()
    def __str__(self):
        return '{}: {}'.format(self.type, self.url)
