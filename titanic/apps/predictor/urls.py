from django.conf.urls import url 
from . import views

app_name = "predictor"

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^result$', views.result, name="result"),
]