from django.urls import path

from petstagram.common.views import LandingPage

urlpatterns = [
    path('', LandingPage.as_view(), name='index'),
]
