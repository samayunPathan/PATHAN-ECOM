from django.urls import path
from core_app import views

app_name='core_app'

urlpatterns = [
    path('',views.font_page,name='font_page'),
    path('about/',views.about,name='about'),
]
