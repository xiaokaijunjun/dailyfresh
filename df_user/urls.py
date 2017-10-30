"""dailyfresh_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from df_user import views

urlpatterns = [
    url(r'^index/$',views.index,name="index"),
    url(r'^register/$',views.register,name="register"),
    url(r'^login/$',views.login,name="login"),
    url(r'^info/$',views.info,name="info"),
    url(r'^logout/$',views.logout,name="logout"),
    url(r'^recent/$',views.recent,name="recent"),
    url(r'^order/$',views.order,name="order"),
    url(r'^site/$',views.site,name="site"),
    url(r'^cart/$',views.cart,name="cart"),

]
