from django.urls import reverse_lazy
from django.views.generic import FormView, UpdateView
from .forms import PostalLetterForm
from .models import PostalLetterModel


class HomeView(FormView):
    form_class = PostalLetterForm
    template_name = 'main/index.html'
    success_url = reverse_lazy('home')
    extra_context = {
        'title': 'Memory'
    }

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            user = self.request.user
            form.instance.user = user

        form = form.save(commit=False)
        form.save()
        return super().form_valid(form)


class LetterUpdate(UpdateView):
    model = PostalLetterModel
    form_class = PostalLetterForm
    template_name = 'main/letter_update.html'
    extra_context = {
        'title': 'Letter update'
    }

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            user = self.request.user
            form.instance.user = user

        form = form.save(commit=False)
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('profile')