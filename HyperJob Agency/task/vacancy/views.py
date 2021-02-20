from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponseForbidden
from .models import Vacancy


# Create your views here.
class MainPageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'vacancy/main_page.html')


class VacancyListView(View):
    def get(self, request, *args, **kwargs):
        vacancies = Vacancy.objects.all()
        return render(request, 'vacancy/vacancy_list.html', context={
            'vacancies': vacancies
        })


class NewVacancyView(View):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden('Not Authenticated!')
        elif not request.user.is_staff:
            return HttpResponseForbidden('Only staff can create vacancy!')
        else:
            return render(request, 'vacancy/new_vacancy.html')

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden('Not Authenticated!')
        elif not request.user.is_staff:
            return HttpResponseForbidden('Only staff can create vacancy!')
        else:
            description = request.POST.get('description', None)
            author_id = request.user.id

            if description is None or description.strip() == "":
                return HttpResponseForbidden('No description Entered')
            new_vacancy = Vacancy(description=description, author_id=author_id)
            new_vacancy.save()
            return redirect("/")


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = '/login'
    template_name = 'vacancy/sign_up.html'


class MyLoginView(LoginView):
    form_class = AuthenticationForm
    redirect_authenticated_user = False
    success_url = '/..'
    template_name = 'vacancy/login.html'
