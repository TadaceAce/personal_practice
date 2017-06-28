from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Question, Choice


# /polls/
class IndexView(generic.ListView):
    template_name='polls/index.html'
    context_object_name='latest_question_list'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]



# /polls/32
class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
    def get_queryset(self):
        ''' excludes any questions that aren't published yet'''
        return Question.objects.filter(pub_date__lte=timezone.now())

    

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

    

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
        # posts based on submitted key name, always string
    except (KeyError, Choice.DoesNotExist):
        # returns KeyError if choice wasn't provided with POST data
        # redisplay question voting form
        return render(request, 'polls/detail.html', {
            'question' : question,
            'error_message' : "You didn't select a choice",
            })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # always return httpresponse redirect after a post.
        # this prevents posting twice if user hits back button
        # reverse helps avoid having to hardcode a url in view function
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

        
   


