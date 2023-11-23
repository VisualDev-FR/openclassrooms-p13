from django.contrib import admin
from django.urls import path, include

from oc_lettings_site import views as index

urlpatterns = [
    path('', index.index, name='index'),
    path('admin/', admin.site.urls),
    path('lettings/', include('lettings.urls', namespace="lettings"), name="lettings"),
    path('profiles/', include('profiles.urls', namespace="profiles"), name="profiles"),
]
