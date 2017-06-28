"""mysite URL Configuration

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

from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from . import views


from django.contrib import admin
admin.autodiscover()




urlpatterns = [

        # AUTH
        url(r'^login/$', auth_views.login, name='login'),
        url(r'^logout/$', auth_views.logout, name='logout'),
        url(r'^accounts/register/$', views.register, name='register'),
        url(r'^accounts/register/complete/$', views.registration_complete, name='registration_complete'),
        url(r'^oauth/', include('social_django.urls', namespace='social')),


        # KICKBALL
        url(r'^kickball/$', views.kickball, name='kickball'),
        url(r'^captains/$', views.captains, name='captains'),
        url(r'^reg_kickball/$', views.reg_kickball, name='reg_kickball'),
        # url(r'^season/$', views.SeasonSelect.as_view(), name='season_select'),
        url(r'^reg_kickball/payment/$', views.payment, name='payment'),


        # APPS
        url(r'^admin/', admin.site.urls),
        url(r'^polls/', include('polls.urls')),
        url(r'^home/', include('home.urls')),

        # HOME
        url(r'$', views.home_page, name='index'),

        # OTHER
        url(r'^chaining/', include('smart_selects.urls')),
        url(r'^paypal/', include('paypal.standard.ipn.urls')),
]


