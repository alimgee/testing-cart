"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.contrib.auth import views as auth_views # importing built in loginveiw
from django.urls import path, include
from django.conf.urls import url
from users import views as user_views
from products.views import ProductListView
from django.conf import settings
from django.conf.urls.static import static
from cart import urls as urls_cart


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),#using the built in log in view to log user in and returning to home page (set in settings.py)
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('profile/', user_views.profile, name='profile'),
    #path('products/', views.products, name='products'),
    path('products/', ProductListView.as_view(), name='products'),
    url(r'^cart/', include(urls_cart)),
 
]

if settings.DEBUG:# if in debug mode use local media folder
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
