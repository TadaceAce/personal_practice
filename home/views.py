from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView


from django.db.models.aggregates import Count
import random
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views import generic

from django.utils import timezone
from django.template.context_processors import csrf

from polls.models import Question



# Create your views here.





# Create your views here.

# def home_page(request):
#     return render(request, 'home/index.html')
#
#

class InterviewView(generic.ListView):
    model = Question
    template_name='home/interview_questions.html'

    def get_context_data(self, **kwargs):
        context = super(InterviewView, self).get_context_data(**kwargs)
        context['random_question_list'] = Question.objects.all().order_by('?')[:3]
        context['full_question_list'] = Question.objects.all()
        return context


class SingleQuestionView(generic.DetailView):
    model = Question
    template_name = 'home/single_question.html'

    def get_context_data(self, **kwargs):
        context = super(SingleQuestionView, self).get_context_data(**kwargs)
        context['all_questions'] = Question.objects.all()
        return context



# def register(request):
#     form = UserCreationForm(request.POST)
#     token = {}
#     token.update(csrf(request))
#     token['form'] = form
#     if request.method == "POST" and form.is_valid():
#         user = super(UserCreationForm, form).save(commit=False)  # changed to True
#         user.set_password(form.cleaned_data["password1"])
#         form.save(commit = True)
#         return user.cleaned_data
#         user.save()
#         return HttpResponseRedirect('/register/complete')
#
#     return render_to_response('registration/registration_form.html', token)
#
#
#
# def registration_complete(request):
#     return render_to_response('registration/registration_complete.html')