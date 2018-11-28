from django import forms

from .models import Challenge

class ChallengeForm(forms.ModelForm):

    class Meta:
        model = Challenge
        #fields =['title','description','image','total_events','points_events','goal','beat_events',]
        fields =['title','description','image','total_events','points_events','goal','beat_events',]
        #fields =
        labels = {
            'title'             :   'Título',
            'description'       :   'Descrição',
            'image'             :   'Imagem',
            'total_events'      :   'Quantidade de eventos',
            'points_events'     :   'Pontos por evento',
            'goal'              :   'Meta',
            'beat_events'       :   'Quantidade de eventos conquistada',
            'beat_points'       :   'Total de pontos conquistados',
            'porcent'           :   'Progress',
        }
        #labels = {'título','descrição','imagem','pontos por eventos','numero total de eventos', 'numero de eventos conquiatados','meta', }




