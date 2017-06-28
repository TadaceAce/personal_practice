
from django.db import models
from django.utils import timezone
from django.http import request

from django.contrib.auth import get_user_model
import uuid
User = get_user_model()
# Create your models here.

from smart_selects.db_fields import ChainedForeignKey, GroupedForeignKey



class Season(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    location = models.CharField(max_length=55)
    registration_open = models.BooleanField(default=False)
    price = models.IntegerField(default=65)


    class Meta:
        app_label = 'home'

    def current_season(self):
        now = timezone.now()
        return self.start_date <= now <= self.end_date

    def __str__(self):
        return self.location



class Team(models.Model):
    league = models.ForeignKey(Season)
    team_name= models.CharField(max_length=55)
    wins = models.IntegerField(blank = True, default = '0')
    losses = models.IntegerField(blank = True, default= '0')
    ties = models.IntegerField(blank = True, default = '0')
    runs_allowed = models.IntegerField(blank = True, default='0')
    runs_scored = models.IntegerField(default='0', blank = True)
    approved = models.BooleanField(default=True)

    class Meta:
        app_label = 'home'

    def __str__(self):
        return self.team_name

    def __unicode__(self):
        return self.name

shirt_size_choices= (
    ('S','Small'),
    ('M', 'Medium'),
    ('L','Large'),
    ('XL','XLarge'),
    ('XXL','XXLarge'),
)


class Player(models.Model):
    player_username = models.ForeignKey(User, null=True, blank=True)
    player_league = models.ForeignKey(Season, null=True, blank=True)
    player_team = GroupedForeignKey(Team,'league', null=True)

    # player_team = ChainedForeignKey(Team,
    #     blank=True,
    #     null=True,
    #     chained_field='team_name',
    #     chained_model_field='player_team',
    #     show_all=False,
    #     auto_choose=True,
    #     sort=True
    # )

    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField()
    picture = models.ImageField(blank = True)
    shirt_size = models.CharField(max_length=25, choices = shirt_size_choices)
    paid = models.BooleanField(default = False)
    credit = models.BooleanField(default = False)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    class Meta:
        app_label = 'home'


