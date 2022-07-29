"""foodmenuproject URL Configuration

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
from django.contrib import admin
from django.urls import path
from restaurantapp import views as views
from productapi.views import ProductsView,ProductDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('menu/view/',views.MenuItemsView.as_view()),
    path('menu/view/<int:id>',views.MenuDetailView.as_view()),
    path('myg/products/',ProductsView.as_view()),
    path('myg/products/<int:id>',ProductDetailView.as_view()),
]
