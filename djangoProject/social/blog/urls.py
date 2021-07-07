from django.urls import path
from . import views 

urlpatterns = [
    
    path('', views.home, name = 'blog-home'),
    path('post/new', views.newPost, name='post-new'),
    path('post/<int:id>/delete', views.deletePost, name = "post-delete"),
    path('post/<int:id>/edit', views.editPost, name='post-edit'),

]