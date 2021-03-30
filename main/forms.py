from django import forms
from .models import Data, Option2


class DataForm(forms.ModelForm):
    class Meta:
        model = Data
        fields = ('gender', 'exercise', 'endurance_or_strength', 'body_part', 'problems')


class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Option2
        fields = ['gender', 'exercise', 'endurance_or_strength', 'body_part', 'problems']
        widgets = {
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'exercise': forms.Select(attrs={'class': 'form-control'}),
            'endurance_or_strength': forms.Select(attrs={'class': 'form-control'}),
            'body_part': forms.Select(attrs={'class': 'form-control'}),
            'problems': forms.Select(attrs={'class': 'form-control'}),
        }