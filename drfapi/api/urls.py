
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name="home"),
    path('getage/<int:day>/<int:month>/<int:year>/',views.getage,name="getage")
]