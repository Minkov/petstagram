from django.contrib.auth import mixins as auth_mixins
from django.core import exceptions


class OwnerRequiredMixin(auth_mixins.LoginRequiredMixin):
    user_field = "user"

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        obj_user = getattr(obj, self.user_field, None)
        if obj_user != self.request.user:
            raise exceptions.PermissionDenied

        return obj
