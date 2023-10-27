from django.urls import reverse_lazy
from django.views.generic import FormView
from .forms import MemorandumForm


class HomeView(FormView):
    form_class = MemorandumForm
    template_name = 'main/index.html'
    success_url = reverse_lazy('home')
    extra_context = {
        'title': 'Memory'
    }

    def form_valid(self, form):
        form = form.save(commit=False)
        form.save()
        return super().form_valid(form)