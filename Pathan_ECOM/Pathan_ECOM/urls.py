
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('core_app.urls')),
    path('',include('userprofile.urls')),
    path('',include('store.urls')),
    
]
