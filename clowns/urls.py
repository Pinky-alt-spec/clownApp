"""clowns URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib.auth import views as auth_views
from account import views as user_view
from django.urls import path, include
from django.contrib import admin

from django.conf.urls.static import static
from django.conf import settings

from django.views.static import serve
from django.conf.urls import url


urlpatterns = [

    path('register/', user_view.register, name='account-register'),
    path('profile/', user_view.profile, name='account-profile'),
    path('profile/update/', user_view.profile_update, name='account-profile-update'),
    path('', auth_views.LoginView.as_view(template_name='clownApp/account/login.html'), name='account-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='clownApp/account/logout.html'), name='account-logout'),

    path('admin/', admin.site.urls),
    path('', include('clownApp.urls')),

    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),


    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
