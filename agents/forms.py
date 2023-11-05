from django import forms
from .models import Agent


class AgentForm(forms.ModelForm):
    class Meta:
        model = Agent
        fields = ['thumbnail','name', 'firstname', 'lastname', 'adress', 'nationality', 'phone']