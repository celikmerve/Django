"""proje URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path,include
from article import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , views.index,name="index"),
    path('index/',views.index,name="index"),
    path('Kullanim_Klavuzlari/' , views.Kullanim_Klavuzlari,name="Kullanim_Klavuzlari"),
    path('Notlar/',views.Notlar,name="Notlar"),
    path('detail/<int:id>' , views.detail,name="detail"),
    path('articles/',include("article.urls")),
    path('user/',include("user.urls")),
    path('Python/',views.Python,name="Python"),
    path('veri_yapilari/',views.veri_yapilari,name="veri_yapilari"),
    path('Siber_Ataklar/',views.Siber_Ataklar,name="Siber_Ataklar"),
    path('yeni/',views.yeni,name="yeni"),
]
