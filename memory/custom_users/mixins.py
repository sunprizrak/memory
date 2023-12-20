from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect


class UnauthorizedRequiredMixin(AccessMixin):
    """Mixin, ограничивающий доступ для авторизованных пользователей."""

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('profile')
        return super().dispatch(request, *args, **kwargs)
