from django.urls import path
from .views import HomePageView
from .views import FeaturesPageView
from .views import WebappPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('features/', FeaturesPageView.as_view(), name='features'),
    path('webapp/', WebappPageView.as_view(), name='webapp'),
]