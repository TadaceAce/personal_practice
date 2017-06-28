from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.forms import forms
from django.forms import ModelForm


from .models import Question, Choice
from home.models import Season, Team, Player


# Register your models here.
# Have to comment this out to make new migrations typically changing models
# Might have to comment ModelForms in view as well

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    # fields = ['pub_date', 'question_text']
    fieldsets = [
        (None, {'fields':['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']


# admin.site.register(Question, QuestionAdmin)
admin.site.unregister(User)

admin.site.register(User, UserAdmin)
UserAdmin.list_display = ('username', 'email', 'first_name', 'last_name', 'is_active', 'date_joined', 'is_staff')



# KICKBALL BELOW

def Update_Rosters(modeladmin, request, queryset):
    for n in queryset:
        entry = n.player_team
        entry.update(runs_scored = 5)



class TeamInline(admin.TabularInline):
    model = Team
    extra = 0
    ordering = ('-wins','-runs_allowed')


class PlayersInline(admin.TabularInline):
    model = Player
    extra = 0



class SeasonAdmin(admin.ModelAdmin):
    fields = ['location', 'start_date', 'end_date', 'price', 'registration_open']
    list_display = ('location','start_date','end_date', 'price', 'registration_open')
    inlines = [TeamInline]
    ordering = ('-start_date','-end_date',)
    search_fields = ['start_date','end_date','location']
    actions = [Update_Rosters]



class TeamAdmin(admin.ModelAdmin):
    fields = ['team_name', 'league','wins', 'losses', 'ties','runs_scored','runs_allowed']  # add num players?
    list_display = ('team_name', 'league', 'wins', 'losses', 'ties', 'runs_scored','runs_allowed')
    search_fields = ['team_name','runs_scored','runs_allowed', 'league__location']
    inlines = [PlayersInline]



class PlayerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'player_team', 'shirt_size', 'paid', 'credit')
    search_fields = ['first_name', 'last_name','email', 'player_team__team_name']
    actions = [Update_Rosters]


admin.site.register(Season, SeasonAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Player, PlayerAdmin)


