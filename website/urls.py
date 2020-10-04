from django.urls import path
from .views import hello_blog, post_detail


urlpatterns = [
    path('', hello_blog, name='website'),
    path('post/<int:id>', post_detail, name='post_detail'),
]