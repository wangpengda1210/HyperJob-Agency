"""hyperjob URL Configuration

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
from django.urls import path
from django.contrib.auth.views import LogoutView
from vacancy.views import MainPageView, VacancyListView, SignUpView, MyLoginView, NewVacancyView
from resume.views import ResumeListView, ProfileView, NewResumeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainPageView.as_view()),
    path("vacancies", VacancyListView.as_view()),
    path('resumes', ResumeListView.as_view()),
    path('login', MyLoginView.as_view()),
    path('signup', SignUpView.as_view()),
    path('login/', MyLoginView.as_view()),
    path('signup/', SignUpView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('home', ProfileView.as_view()),
    path('resume/new', NewResumeView.as_view()),
    path('vacancy/new', NewVacancyView.as_view()),
]
