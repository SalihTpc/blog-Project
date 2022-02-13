from django.urls import path
from .views import HomeView, DetailView, AddPostView, UpdatePostView, DeletePostView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path("", views.home, name="home")
    path("", HomeView.as_view(), name="home"),
    path("blog/<int:pk>", DetailView.as_view(), name="details"),
    path("add_post/", AddPostView.as_view(), name="add_post"),
    path("edit/<int:pk>", UpdatePostView.as_view(), name="update"),
    path("delete/<int:pk>", DeletePostView.as_view(), name="delete")
] 
# + static(settings.Media_URL, document_root=settings.MEDIA_ROOT)