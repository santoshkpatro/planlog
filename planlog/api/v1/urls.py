from django.urls import path
from .user.views import LoginView, RegisterView, AvailabilityView


urlpatterns = [
    path('user/login/', LoginView.as_view()),
    path('user/register/', RegisterView.as_view()),
    path('user/availability/', AvailabilityView.as_view()),
]
