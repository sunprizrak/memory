from django.urls import path
from .views import HomeView, LetterUpdate


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('letter/update/<int:pk>/', LetterUpdate.as_view(), name='letter_update'),
]