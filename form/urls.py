from django.urls import path
from .views import createForm


urlpatterns = [
    path('', createForm, name='create-form'),
]