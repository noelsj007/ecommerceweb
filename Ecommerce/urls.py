"""Ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from homepage.views import index, Aboutus, News, home, searchbar, itemdetails,store
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shop/', index, name="index"),
    #path('show/', show, name="show"),
    path('aboutus/', Aboutus, name="Aboutus"),
    path('news/', News, name="News"),
    path('', home, name="home"),
    path('store/', store, name="store"),
  #  path('buynow/', buynow, name="buynow"),
    path('searchbar/', searchbar, name="searchbar"),
    path('itemdetails/<int:itemid>/', itemdetails, name="itemdetails"),

    path('accounts/', include('accounts.urls')),
    path('cart/', include('cart.urls')),

    

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

