from django.urls import path
from users.API.views import RegisterView

urlpatterns = [
    path('auth/register', RegisterView.as_view()),
]