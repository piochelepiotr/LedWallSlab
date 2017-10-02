from django.conf.urls import include, url
from django.contrib import admin
from config import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('config.urls')),

]
