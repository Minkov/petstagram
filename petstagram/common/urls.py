from django.urls import path

from petstagram.common.views import landing_page

urlpatterns = [
    path('', landing_page, name='index'),
]
