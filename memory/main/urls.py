from django.urls import path
from .views import HomeView, LetterUpdateView, LetterDeleteView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('letter/update/<int:pk>/', LetterUpdateView.as_view(), name='letter_update'),
    path('letter/delete/<int:pk>/', LetterDeleteView.as_view(), name='letter_delete'),
]