from django.contrib import admin
from django.urls import path

from oc_lettings_site import views as index
from profiles import views as profiles
from lettings import views as lettings

urlpatterns = [
    path('', index.index, name='index'),
    path('lettings/', lettings.lettings_index, name='lettings_index'),
    path('lettings/<int:letting_id>/', lettings.letting, name='letting'),
    path('profiles/', profiles.profiles_index, name='profiles_index'),
    path('profiles/<str:username>/', profiles.profile, name='profile'),
    path('admin/', admin.site.urls),
]
