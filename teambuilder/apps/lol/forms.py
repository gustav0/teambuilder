from django import forms
from teambuilder.apps.lol.models import Champion


class ChampionForm(forms.ModelForm):

    class Meta:
        model = Champion

