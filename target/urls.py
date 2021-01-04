from django.urls import path

from target.views import home
from target import views
urlpatterns = [
    path('', home, name='home'),
    path('contact',views.contact, name='contact'),
    path('aboutus',views.about_us, name='about-us'),
    path('post_index',views.post_index, name='postindex'),
    path('post/<int:pk>',views.post_detail, name='postdetail'),
    path('post/<int:pk>/remove', views.post_delete, name='deletepost')
]