from django.shortcuts import render, render_to_response
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from django.template.context_processors import csrf

from django.views import generic



from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm

from django.utils import timezone
from home.models import Player, Team, Season
# from django.contrib.auth import get_user_model
# User = get_user_model()

from paypal.standard.forms import PayPalPaymentsForm





def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/register/complete/')
    else:
        form = UserCreationForm()

    token = {}
    token.update(csrf(request))
    token['form'] = form


    return render(request, 'registration/registration_form.html', token)




def registration_complete(request):
    #return render_to_response('registration/registration_complete.html')
    return render(request,'registration/registration_complete.html')


def home_page(request):
    return render(request, 'index.html')

def kickball (request):
    return render(request,'kickball.html')

def captains (request):
    return render(request,'captains.html')



class PlayerRegForm(ModelForm):
    class Meta:
        model = Player
        fields = ['first_name', 'last_name', 'email', 'player_league', 'player_team', 'shirt_size', 'player_username','paid','credit']
        widgets = {
            'player_username': forms.HiddenInput(),
            'player_league' : forms.HiddenInput(attrs={'disabled': True}),
            }
        labels = {
            'first_name' : 'First Name',
            'last_name' : 'Last Name',
            'email' : 'Email',
            'player_league' : 'League',
            'player_team' : 'Team',
            'shirt_size' : 'Shirt Size',
            'paid' : '',
            'credit' : '',
            }




class SeasonSelect(generic.ListView):
    model = Season
    template_name = 'season_select.html'

    def get_context_data(self, **kwargs):
        context = super(SeasonSelect, self).get_context_data(**kwargs)
        context['upcoming_seasons'] = Season.objects.all()
        return context


def reg_kickball(request):

    if request.method == 'POST':

        form = PlayerRegForm(data=request.POST)
        if form.is_valid():

            if form.cleaned_data['credit'] == True:
                form.player_username = request.user.username
                form.save()
                return render(request, 'registration/registration_complete.html')

            if form.cleaned_data['paid'] == True:
                form.player_username = request.user.username
                form.save()
                return render(request, 'registration/registration_complete.html')





            def get_price():
                team_name = form.cleaned_data['player_team']
                team_info = Team.objects.filter(team_name__exact=team_name)
                team_league = team_info.all().values_list('league__price')
                price_obj = str(team_league[0])
                return int(price_obj[1:3])

            def get_league():
                team_name = form.cleaned_data['player_team']
                team_info = Team.objects.filter(team_name__exact=team_name)
                league_obj = str(team_info.all().values_list('league__location'))
                indices = []
                index = 0
                while index < len(league_obj):
                    index = league_obj.find("'", index)
                    if index == -1:
                        break
                    indices.append(index)
                    index += 1
                league_name = league_obj[indices[0] + 1:indices[1]]
                return league_name

            request.session['_form'] = request.POST


            return render(request, 'payment.html',
                      {
                       'league' : get_league(),
                       'form': form,
                       'price': get_price(),
                       })
    else:
        if request.user.is_authenticated():
            form=PlayerRegForm(initial={
                'first_name' : request.user.first_name,
                'last_name' : request.user.last_name,
                'email' : request.user.email,
                'player_username' : request.user
                })
            # form.fields['paid'].widget = forms.HiddenInput()
            form.exclude = ['paid','credit']


            form.fields['player_team'].queryset = Team.objects.filter(
                    league__registration_open__exact=True, approved__exact=True)
        else:
            form=PlayerRegForm()

    return render(request, 'registration_kickball.html', {'form': form})


#


def payment (request):
    form = request.session.get('_form')

    if request.method == 'POST':
        pass
    #     form = PlayerRegForm(data=request.POST)
    #     if form.is_valid():
    #
    #         form.player_username = request.user.username
    #         form.save()
    #         return render(request, 'registration/registration_complete.html')
    else:
        if request.user.is_authenticated():
            form=PlayerRegForm(initial={
                'first_name' : request.user.first_name,
                'last_name' : request.user.last_name,
                'player_username' : request.user
                })
            form.fields['player_team'].queryset = Team.objects.filter(
                    league__registration_open__exact=True, approved__exact=True)
        else:
            form=PlayerRegForm()

    return render(request, "payment.html")

