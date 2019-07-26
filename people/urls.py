from django.conf.urls import url

from people.views import CreatorsListView, RegistrationView

urlpatterns = [
    url(r'^creators/$', CreatorsListView.as_view(), name='creators-list'),
    url(r'^register/$', RegistrationView.as_view(), name='register'),
]
