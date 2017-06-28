from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import UserCreationForm


from . import views

app_name = 'home'
urlpatterns = [
    # /home/interview_questions
    url(r'^interview_questions/$', views.InterviewView.as_view(), name='interview_questions'),

    url(r'^(?P<pk>[0-9]+)/$', views.SingleQuestionView.as_view(), name='detail'),


    # added

    # url(r'^$', views.home_page, name='index'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    # url(r'^register/$', views.register, name='register'),
    # url(r'^register/complete/$', views.registration_complete, name='registration_complete'),

]
