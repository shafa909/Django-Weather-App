
from django.conf.urls import url
from django.contrib import admin
from w_app.views import index

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^weather/',index),

]
