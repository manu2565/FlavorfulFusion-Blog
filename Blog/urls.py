"""
URL configuration for Blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from Blog import views
from .views import HomeView



urlpatterns = [
    path('admin/', admin.site.urls),
    path("home",views.index ,name="home"),
    path('header/',views.header,name="header"),
    path("footer/",views.footer ,name="footer"),
    path("base/",views.base, name="base"),
    path("category/",views.category, name="category"),
    path("contact/",views.contact, name="contact"),
    path("searchresult/",views.searchresult, name="searchresult"),
    path("single-post/",views.single_post, name="single-post"),
    path("about-page/",views.aboutpage, name="about"),
    path("Saveenqariy/",views.saveEnquiry,name='saveEnquiry'),
    path("login/",views.login,name='login'),
    path("singin/",views.singin,name='singin'),
    path('',views.home,name='start'),
    path('logout/',views.signout, name='logout'),
    path('hom/',HomeView.as_view(),name="home"),
    path('pricing/',views.pricing, name='pricing'),
    path('indes', views.indexes, name='index'),
    path('creates/', views.create, name='create'),
    path('update/<int:post_id>', views.update, name='update'),
    path('read/<int:post_id>', views.read, name='read'),
    path('delete/<int:post_id>', views.delete, name='delete'),
]

