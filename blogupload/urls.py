from django.contrib import admin
from django.urls import path
from .views import blog_list_create, blog_detail, index_view

urlpatterns = [
    path('', index_view),
    path('blog/', blog_list_create),
    path('blog/<int:pk>/', blog_detail),
]


