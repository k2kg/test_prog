from django import forms
from .models import Question

class QuestionForm(forms.Form):
    answer = forms.CharField(label='Ваш ответ', widget=forms.TextInput(attrs={'class': 'form-control'}))
