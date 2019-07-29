from django.conf.urls import url

from people.views import CreatorsListView, RegistrationView, register_success

urlpatterns = [
    url(r'^creators/$', CreatorsListView.as_view(), name='creators-list'),
    url(r'^register/$', RegistrationView.as_view(), name='register'),
    url(r'^register_success/$', register_success, name='register_success')
]
