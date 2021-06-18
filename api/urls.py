from django.urls import path
from .views import UserApi


app_name = "api"
urlpatterns = [
    path("user",UserApi.as_view())
]
