import csv
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import FormView

from WSS.mixins import FooterMixin
from WSS.models import WSS
from people.models import TechnicalExpert, StudentApplication, Grade
from people.forms import RegistrationForm


class CreatorsListView(FooterMixin, ListView):
    model = TechnicalExpert
    template_name = 'people/creators_list.html'
    context_object_name = 'technical_experts'

    def get_context_data(self, **kwargs):
        context = super(CreatorsListView, self).get_context_data(**kwargs)
        context['wss'] = WSS.active_wss()
        return context


class RegistrationView(FormView):
    form_class = RegistrationForm
    form_class.label_suffix = ""
    template_name = 'people/register.html'
    success_url = reverse_lazy('people:register_success')

    def get_context_data(self, **kwargs):
        context = super(RegistrationView, self).get_context_data(**kwargs)
        context['wss'] = WSS.active_wss()
        return context

    def form_valid(self, form):
        application = StudentApplication.objects.create(
            first_name=form.cleaned_data.get('first_name'),
            last_name=form.cleaned_data.get('last_name'),
            phone_number=form.cleaned_data.get('phone_number'),
            national_id=form.cleaned_data.get('national_id'),
            school_name=form.cleaned_data.get('school_name'),
            city=form.cleaned_data.get('city'),
            email=form.cleaned_data.get('email'),
            answer=form.cleaned_data.get('answer'),
            grade=form.cleaned_data.get('grade'),
            city_wanted=form.cleaned_data.get('city_wanted'),
            request_dorm=form.cleaned_data.get('request_dorm'),
            second_choice_available=form.cleaned_data.get('second_choice_available'),
            description=form.cleaned_data.get('description')
        )
        return super().form_valid(form)


def register_success(request):
    return render(request, template_name='register_success.html', context={
        'wss': WSS.active_wss()
    })


@login_required
def get_export(request):
    if not request.user.is_superuser:
        return PermissionDenied
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=export.csv'
    writer = csv.writer(response)
    head = [
        'first_name',
        'last_name',
        'national_id',
        'phone_number',
        'city_wanted',
        'city',
        'request_dorm',
        'second_choice',
        'grade',
        'school_name',
        'email',
        'answer',
        'description',
    ]
    writer.writerow(head)
    for sa in StudentApplication.objects.all():
        row = [
            sa.first_name,
            sa.last_name,
            sa.national_id,
            sa.phone_number,
            sa.city_wanted,
            sa.city,
            sa.request_dorm,
            sa.second_choice_available,
            Grade[sa.grade].value,
            sa.school_name,
            sa.email,
            request.build_absolute_uri().split(request.get_full_path())[0] + sa.answer.url,
            sa.description
        ]
        writer.writerow(row)
    return response
