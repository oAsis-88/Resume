from django.urls import path
from .views import index, smiley

urlpatterns = [
    path('smiley/', smiley, name='smiley'),
    path('', index, name='index'),
]