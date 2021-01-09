from django.conf.urls.static import static
from django.contrib.auth import login
from .views import *
from django.urls import path


urlpatterns = [
    path('', HomeView, name='home'),
    path('acoounts/login/', user_login, name='login'),
    path('accounts/logount/', LogoutView.as_view(), name='logout'),
    path('accounts/register/', RegisterView.as_view(), name='register'),
    path('accounts/profile/', ProfileView.as_view(), name='profile'),

] #+ static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)

