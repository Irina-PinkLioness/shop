
from django.contrib import admin
from django.urls import path, include

admin.site.site_title = 'On-line shop'
admin.site.site_header = 'On-line shop'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('backend.urls')),
]
