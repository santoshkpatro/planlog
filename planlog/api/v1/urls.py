from django.urls import path
from .user.views import LoginView, RegisterView, AvailabilityView, AuthenticationStatusView, ProfileView
from .boards.views import BoardListCreateView


urlpatterns = [
    path('user/', AuthenticationStatusView.as_view()),
    path('user/login/', LoginView.as_view()),
    path('user/register/', RegisterView.as_view()),
    path('user/profile/', ProfileView.as_view()),
    path('user/availability/', AvailabilityView.as_view()),

    path('boards/', BoardListCreateView.as_view())
]
