from django.urls import path
from .views import index, auth_signUp, auth_login, auth_logout, admin_control

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path ('index/', index, name='Index'),
    path ('signup/', auth_signUp, name='SignUp'),
    path ('', auth_login, name='SignIn'),
    path ('logout/', auth_logout, name='Logout'),
    path ('Admin_control/<str:username>', admin_control, name='AdminControl')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)