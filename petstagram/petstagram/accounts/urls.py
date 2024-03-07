from django.urls import path, include
from django.contrib.auth import views as auth_views

from petstagram.accounts.views import \
    SignInUserView, SignUpUserView, signout_user, \
    ProfileDetailsView, ProfileUpdateView, ProfileDeleteView

urlpatterns = (
    path("signup/", SignUpUserView.as_view(), name="signup user"),
    path("signin/", SignInUserView.as_view(), name="signin user"),
    path("signout/", signout_user, name="signout user"),

    path(
        "profile/<int:pk>/", include([
            path("", ProfileDetailsView.as_view(), name="details profile"),
            path("edit/", ProfileUpdateView.as_view(), name="edit profile"),
            path("delete/", ProfileDeleteView.as_view(), name="delete profile")
        ]),
    )
)
