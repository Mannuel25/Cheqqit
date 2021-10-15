from django.urls import path
from .views import HomePageView
from .views import FeaturesPageView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('features/', FeaturesPageView.as_view(), name='features'),
]