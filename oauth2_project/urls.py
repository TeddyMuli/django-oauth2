from django.contrib import admin
from django.urls import path, include
from oauth2_app.views import login_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('oauth2_app.urls')),
    path('accounts/', include('allauth.urls')),
    path('o/', include('oauth2_provider.urls')),
    path('login/', login_view, name="login")
]
