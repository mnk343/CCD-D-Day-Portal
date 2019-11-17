from django.contrib import admin
from django.urls import path, include
from dday_portal import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('updateProfile/<int:pk>/<int:pk2>', views.UpdateProfile , name='UpdateProfile'),
    path('UpdateAnnouncement/<int:pk>', views.UpdateAnnouncement , name='UpdateAnnouncement'),
    path('showStudents/<int:pk>', views.showStudents , name='showStudents'),
    path('showAnnouncements', views.showAnnouncements , name='showAnnouncements'),
    path('deleteAnnouncement/<int:pk>/<int:pk2>', views.deleteAnnouncement , name='deleteAnnouncement'),
    path('accounts/', include('allauth.urls')),

]
