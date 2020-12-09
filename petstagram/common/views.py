from django.views import generic as views


class LandingPage(views.TemplateView):
    template_name = 'landing_page.html'
