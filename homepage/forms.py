from django import forms
from .models import *

class SubscribeForm(forms.Form):

    email = forms.CharField(widget=forms.EmailInput({'placeholder': 'example@mail.ru', 'autocomplete': 'on'}),
                            label='', max_length=100, )
