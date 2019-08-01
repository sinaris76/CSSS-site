from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import FormView

from WSS.mixins import FooterMixin
from WSS.models import WSS
from people.models import TechnicalExpert, StudentApplication
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
            school_name=form.cleaned_data.get('school_name'),
            city=form.cleaned_data.get('city'),
            email=form.cleaned_data.get('email'),
            answer=form.cleaned_data.get('answer'),
            grade=form.cleaned_data.get('grade'),
            city_wanted=form.cleaned_data.get('city_wanted')
        )
        return super().form_valid(form)


def register_success(request):
    return render(request, template_name='register_success.html', context={
        'wss': WSS.active_wss()
    })