from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.home, name='home'),
    path('posts', views.post_list, name='postlist'),
    path('posts/search', views.post_search, name='postsearch'),
    path('add-post', views.add_post, name='addpost'),
    path('post-edit/<int:id>', views.post_edit, name='postedit'),
    path('post-delete/<int:id>', views.post_delete, name='postdelete'),
    path('post-operations', views.post_operations, name='postoperations'),
    path('<slug:slug>', views.post_details, name='postdetails'),
    path('posts/<slug:slug>', views.get_posts_by_category, name='getpostsbycategory'),
]