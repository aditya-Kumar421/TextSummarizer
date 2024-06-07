from django.urls import path
from .views import RegisterView, LoginView, LogoutView, EditUserView, DeleteUserView, SearchUserView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('edit/', EditUserView.as_view(), name='edit_user'),
    path('delete/', DeleteUserView.as_view(), name='delete_user'),
    path('search/', SearchUserView.as_view(), name='search_user'),
]
