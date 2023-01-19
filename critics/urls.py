# pylint: disable=missing-module-docstring
from django.urls import path
from . import views


urlpatterns = [

    path("thank_you", views.thanks, name='thank_you'),
    path("", views.critic, name='home')]
