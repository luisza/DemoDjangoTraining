"""IVRdemo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, re_path
from loquera.views import index, index2, myView, myjsonview, myjson2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index', index2),
    path('gemeric', myView.as_view()),
    path('myjson2', myjson2),
    path('mijson', myjsonview),
    re_path("^index/(?P<var1>\d+)/(?P<mipk>[0-9a-fA-F]+)$", index, name="var1mipk")
]