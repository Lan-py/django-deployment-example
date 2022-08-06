from django.urls import path
from basic_app import views
from django.contrib.auth import views as auth_views
# Template urls
app_name = 'basic_app'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('logout/', views.user_logout, name='logout'),
    # path('special/', views.special, name='special'),
    path('login/', views.user_login, name='login'),
]
