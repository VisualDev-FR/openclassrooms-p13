from django.urls import path

from profiles import views as profiles

app_name = "profiles"

urlpatterns = [
    path('', profiles.index, name='index'),
    path('<str:username>/', profiles.profile, name='profile'),
]
