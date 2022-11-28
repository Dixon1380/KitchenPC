"""KitchenPC URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import include, path
# import kitchenpc_api.main

urlpatterns = [
    # path('api/', include(kitchenpc_api.main.app.root())),
    path('recipes/', include('recipes.urls')),
    path('admin/', admin.site.urls),
    path('pricechecker/', include('price_checker.urls')),
    path('mealprep/', include('meal_prep.urls')),
    path('settings/', include('settings.urls')),
    path('inventory/', include('inventories.urls')),
    path('shoppinglist/', include('shop_generator.urls')),
    path('dashboard/', include('dashboard.urls')),
]
