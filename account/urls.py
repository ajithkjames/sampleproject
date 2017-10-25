from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

from account.views import RegisterView


urlpatterns = [
    url(r'^$', auth_views.login, {'template_name': 'login.html',
                                  'authentication_form': AuthenticationForm,
                                  'redirect_authenticated_user': True}, name='login'),
    url(r'^home/$', login_required(TemplateView.as_view(template_name="home.html"),
                                   login_url='/'), name='home'),
    url(r'^logout', auth_views.logout, {'next_page': 'login'}),
    url(r'^register/$', RegisterView.as_view(), name='register'),
]
