from django.urls import path

from . import views

urlpatterns = [
    path ('blog/', views.blog_list, name="blog_list"),
    path ('blog/<int:blog_id>', views.blog_detail, name="blog_detail"),
]