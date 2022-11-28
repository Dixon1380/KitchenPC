from django.urls import path

from . import views


urlpatterns = [
    path('', views.price_checker, name='pricechecker'),
]