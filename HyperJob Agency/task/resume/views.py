from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponseForbidden
from .models import Resume


# Create your views here.
class ResumeListView(View):
    def get(self, request, *args, **kwargs):
        resumes = Resume.objects.all()

        return render(request, 'resume/resume_list.html', context={
            'resumes': resumes
        })


class ProfileView(View):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            username = None
            user_resumes = None
            is_staff = False
        else:
            username = request.user.username
            user_resumes = Resume.objects.filter(author_id=request.user.id)
            if len(user_resumes) == 0:
                user_resumes = None
            is_staff = request.user.is_staff

        return render(request, 'resume/user_profile.html', context={
            'username': username,
            'user_resumes': user_resumes,
            'is_staff': is_staff
        })


class NewResumeView(View):
    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden('Not Authenticated!')
        else:
            description = request.POST.get('description', None)
            author_id = request.user.id

            if description is None or description.strip() == "":
                return HttpResponseForbidden('No description Entered')
            new_resume = Resume(description=description, author_id=author_id)
            new_resume.save()
            return redirect("/")
