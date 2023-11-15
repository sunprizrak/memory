from django.http import Http404
from django.urls import reverse_lazy
from django.views.generic import FormView, UpdateView, DeleteView
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


class LetterUpdateView(UpdateView):
    model = PostalLetterModel
    form_class = PostalLetterForm
    template_name = 'main/letter_update.html'
    extra_context = {
        'title': 'Letter update'
    }

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if self.request.user != obj.user:
            raise Http404("Вы не можете редактировать эту запись.")
        return obj

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            user = self.request.user
            form.instance.user = user

        form = form.save(commit=False)
        form.save()
        return super(LetterUpdateView).form_valid(form)

    def get_initial(self):
        initial = super().get_initial()
        if self.object and hasattr(self.object, 'send_date'):
            initial['send_date'] = self.object.send_date.strftime('%Y-%m-%d')
        return initial

    def get_success_url(self):
        return reverse_lazy('profile')


class LetterDeleteView(DeleteView):
    model = PostalLetterModel
    context_object_name = 'delete_letter'
    template_name = 'main/letter_delete.html'
    success_url = reverse_lazy('profile')

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if self.request.user != obj.user:
            raise Http404("Вы не можете удалить эту запись.")
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['letters'] = self.model.objects.filter(user=self.request.user).order_by('-created')
        return context