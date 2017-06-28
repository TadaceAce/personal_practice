
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

import django
django.setup()
from home.models import Player, Team, Season


from polls.models import *
from django.utils import timezone

import datetime
from django.utils import timezone
from polls.models import Question

from django.db.models import CharField
from django.db import migrations


def update_rosters():
    for person in Player.objects.all():
        if person.player_team == None:
            print('yes')
            team_nm = Team.objects.get(id=1)  
            team_nm.runs_scored = 5
            
            
            person.save()
update_rosters()
            

#print(get_fields())

##
##future_question = Question(pub_date=timezone.now())
##
##print(future_question.was_published_recently())
                        


#Let's test our custom definition in the Question model.




# check choices for a question
##print(q.choice_set.all())
##
### create choices for question
##q.choice_set.create(choice_text='Not much', votes=0) # recall choice texe and votes were the fields for the choice model
##q.choice_set.create(choice_text='The sky', votes=0) 
##
### We can set c equal to choice object
##c = q.choice.set.create(choice_text='Just hacking again', votes=0)
##
### choice objects have access to their related question
##print(c.question)
##
### question objects get access to Choice objects
##print(q.choice_set.all())




# CREATE
##q1 = Question(question_text="Question1?", pub_date=timezone.now())
##q1.save()
##q1.choice_set.create(choice_text='This is test answer1', votes=0)
##q1.choice_set.create(choice_text='This is test answer2', votes=0)



# CLEAR 
##c = Question.objects.all()
##c.delete()


# QUERY
##q = Question.objects.all()
##q = Question.objects.get(pk=3) # first question for some reason



##q.choice_set.create(choice_text='a1', votes=0)
##q.choice_set.create(choice_text='a2', votes=0)
##
##total = q.choice_set.count
##
##c = q.choice_set.all()
##c.delete()
##print(c)



## FILTER
##to_del = q.choice_set.filter(choice_text__startswith = 'a')
##print (to_del)





