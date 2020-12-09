from django.contrib.auth import login
from django.contrib.auth import views as auth_views
from django.contrib.auth.models import User

from django.urls import reverse_lazy
from django.views import generic as views

from petstagram.accounts.forms import SignUpForm, UserProfileForm
from petstagram.accounts.models import UserProfile


class UserProfileView(views.UpdateView):
    template_name = 'accounts/user_profile.html'
    form_class = UserProfileForm
    model = UserProfile
    success_url = reverse_lazy('current user profile')

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk', None)
        user = self.request.user \
            if pk is None \
            else User.objects.get(pk=pk)
        return user.userprofile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['profile_user'] = self.get_object().user
        context['pets'] = self.get_object().pet_set.all()

        return context


class SignInView(auth_views.LoginView):
    template_name = 'accounts/signin.html'


class SignUpView(views.CreateView):
    template_name = 'accounts/signup.html'
    form_class = SignUpForm
    success_url = reverse_lazy('current user profile')

    def form_valid(self, form):
        valid = super().form_valid(form)
        user = form.save()
        login(self.request, user)
        return valid


class SignOutView(auth_views.LogoutView):
    next_page = reverse_lazy('index')
