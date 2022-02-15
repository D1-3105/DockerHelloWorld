from django.urls import path
from .views import ViewCurrentBlog,DeleteBlog,EditBlog, CreateBlog

urlpatterns=[
    path('', ViewCurrentBlog.as_view(), name='cur_blog'),
    path('del/<int:pk>', DeleteBlog.as_view(), name='delete_post'),
    path('edit/<int:pk>', EditBlog.as_view(), name='edit_post'),
    path('new/', CreateBlog.as_view(), name='create_post'),

]