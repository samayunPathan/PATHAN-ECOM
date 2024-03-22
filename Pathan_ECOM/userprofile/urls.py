from django.contrib.auth import views as auth_views
from django.urls import path
from userprofile import views
from django.shortcuts import redirect

app_name='userprofile'

urlpatterns = [
    path('login/',auth_views.LoginView.as_view(template_name='userprofile/login.html'),name='login'),
    path('signup/',views.signup,name='signup'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    path("myaccount/", views.myaccount, name="myaccount"),
    path('vendors/<int:pk>/',views.verdor_detail,name='vendor_detail'),
    
]
