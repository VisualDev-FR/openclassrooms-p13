from django.urls import path

from lettings import views as lettings

app_name = "lettings"

urlpatterns = [
    path('', lettings.index, name='index'),
    path('<int:letting_id>/', lettings.letting, name='letting'),
]
