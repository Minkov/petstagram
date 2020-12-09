from django.urls import path, include

from petstagram.accounts.views import user_profile, signup_user, signout_user, SignUpView

urlpatterns = (
    # path('signin/', LoginView.as_view(template_name='registration/login.html'), name='signin user', ),
    path('', include('django.contrib.auth.urls')),
    path('profile/', user_profile, name='current user profile'),
    path('profile/<int:pk>/', user_profile, name='user profile'),
    # path('signup/', signup_user, name='signup user'),
    path('signup/', SignUpView.as_view(), name='signup user'),
    path('signout/', signout_user, name='signout user'),
)

from .receivers import *
