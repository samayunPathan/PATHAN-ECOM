from django.urls import path
from store import views

app_name='store'

urlpatterns = [
    path('<slug:slug>/',views.product_details,name='product_detail')
]
