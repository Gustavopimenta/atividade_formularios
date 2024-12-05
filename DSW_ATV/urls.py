from django.urls import path
from DSW_ATV import views

urlpatterns = [
    path('', views.index, name='index'),
]
