from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'home.html'

class FeaturesPageView(TemplateView):
    template_name = 'features.html'

class WebappPageView(TemplateView):
    template_name = 'webapp.html'
