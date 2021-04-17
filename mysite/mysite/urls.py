from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^carco2/', include('carco2.urls')),
    url(r'^admin/', admin.site.urls),
]