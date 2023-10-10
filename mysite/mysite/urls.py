from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', admin.site.urls),
    # path('', include('databse_tpa.urls')),
]
