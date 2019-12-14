# laporan/urls.py
# 
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views 

router = DefaultRouter()
router.register('kedinasan', views.KedinasanRestView)



app_name = 'master'

urlpatterns = [
    path('api/master/', include(router.urls))
]