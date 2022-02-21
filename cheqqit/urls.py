from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signupPage, name='signup'),
    path('signin/', views.signinPage, name='login'),
    path('signout/', views.signoutUser, name='logout'),
]