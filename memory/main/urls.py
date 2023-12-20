from django.urls import path
from .views import HomeView, LetterUpdateView, LetterDeleteView
from custom_users.views import logout_user

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('admin/logout/', logout_user, name='logout'),  # replaces logout django-grappelli
    path('letter/update/<int:pk>/', LetterUpdateView.as_view(), name='letter_update'),
    path('letter/delete/<int:pk>/', LetterDeleteView.as_view(), name='letter_delete'),
]