from django.urls import path,include
from . import views

app_name = "dday_portal"

urlpatterns = [

    path('updateProfile/<int:pk>', views.UpdateProfile , name='UpdateProfile'),
]
