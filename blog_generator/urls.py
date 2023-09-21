from django.urls import path
from .views import *
app_name =  'aiblog'

urlpatterns = [
    path('', index, name='index'),
    path('login', user_login, name='login'),
    path('logout', user_logout, name='logout'),
    path('signup', user_signup, name='signup'),
    path('generate-blog', generate_blog, name='generate-blog'),
    path('blog-list', blog_list, name='blog-list'),
    path('blog-details/<int:pk>/', blog_details, name='blog-details'),
]
