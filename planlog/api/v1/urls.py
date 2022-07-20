from django.urls import path
from .user.views import LoginView, RegisterView, AvailabilityView, AuthenticationStatusView, ProfileView
from .boards.views import BoardListCreateView
from .templates.views import TemplateListView


urlpatterns = [
    # /user
    path('user/', AuthenticationStatusView.as_view()),
    path('user/login/', LoginView.as_view()),
    path('user/register/', RegisterView.as_view()),
    path('user/profile/', ProfileView.as_view()),
    path('user/availability/', AvailabilityView.as_view()),

    # /boards
    path('boards/', BoardListCreateView.as_view()),

    # /templates
    path('templates/', TemplateListView.as_view()),
]
