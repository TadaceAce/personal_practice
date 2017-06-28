# import datetime
# from django.db import models
# from django.utils import timezone
#
# # Create your models here.
#
#
#
#
#
# class Season(models.Model):
#     start_date = models.DateField()
#     end_date = models.DateField()
#     location = models.CharField(max_length=55)
#
#     class Meta:
#         app_label = 'home'
#
#     def current_season(self):
#         now = timezone.now()
#         return self.start_date <= now <= self.end_date
#
#     def __str__(self):
#         return self.location
#
#     def __unicode__(self):
#         return self.name
#
#
# class Team(models.Model):
#     league = models.ForeignKey(Season, related_name='season')
#     team_name= models.CharField(max_length=55)
#     record =  models.CharField(max_length=55, default='')
#     runs_allowed = models.IntegerField(blank = True, default='0')
#     runs_scored = models.IntegerField(default='0')
#
#
#     class Meta:
#         app_label = 'home'
#
#     def __str__(self):
#         return self.team_name
#
#     def __unicode__(self):
#         return self.name
#
# shirt_sizes=['S','M','L','XL','XXL']
#
# class Player(models.Model):
#     player_team = models.ForeignKey(Team)
#     first_name = models.CharField(max_length=25)
#     last_name = models.CharField(max_length=25)
#     email = models.EmailField()
#     picture = models.ImageField(blank = True)
#     shirt_size = models.CharField(max_length=3)
#
#
#
#     def __str__(self):
#         return self.first_name + ' ' + self.last_name
#
#
#
#
#
#     class Meta:
#         app_label = 'home'
#
#
