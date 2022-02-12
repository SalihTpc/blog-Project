from django.urls import path
from .views import HomeView, DetailView

urlpatterns = [
    # path("", views.home, name="home")
    path("", HomeView.as_view(), name="home"),
    path("blog/<int:pk>", DetailView.as_view(), name="details")
]
