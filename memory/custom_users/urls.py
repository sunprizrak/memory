from django.urls import path
from .views import RegisterUserView, logout_user, LoginUserView, ProfileView, PasswordEditView, activate

urlpatterns = [
    path('registration', RegisterUserView.as_view(), name='registration'),
    path('activate/<uidb64>/<token>', activate, name='activate'),
    path('login', LoginUserView.as_view(), name='login'),
    path('logout', logout_user, name='logout'),
    path('profile', ProfileView.as_view(), name='profile'),
    path('change-password', PasswordEditView.as_view(), name='change-password'),

]