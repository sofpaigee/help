from django.urls import path
from . import views
from .views import (
    PostUpdateView,
    PostDeleteView,
    PostDetailView,
    UserPostListView,
)
from . import views as blog_views

urlpatterns = [
    path('', blog_views.home, name='blog-home'),
    path('incident-list/', blog_views.incident_list, name='incident_list'),
    path('incident-report/', blog_views.report_incident, name='post-create'),
    path('user/<str:username>/', UserPostListView.as_view(), name='user-posts'),
    path('natural-disasters/', views.natural_disasters, name='natural_disasters'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', blog_views.about, name='blog-about'),
]