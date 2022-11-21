from django.urls import path
from other.views import SearchResulView, blog, Blog_Detail, About, Contact
urlpatterns = [
    path('blogs/', blog, name='blogs'),
    path('search/', SearchResulView.as_view(), name="search"),
    path('about_us/', About, name='about'),
    path('contact/', Contact, name='contact'),
    path('blog_detail/<int:pk>/', Blog_Detail.as_view(), name='blog_detail'),
]