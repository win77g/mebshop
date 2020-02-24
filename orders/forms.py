from django import forms
from .models import *

class CheckoutContactForm(forms.Form):
    surname = forms.CharField(widget=forms.TextInput({'placeholder': 'Фамилия', 'autocomplete': 'on'})
                              ,required=True,label='',max_length=20)
    name = forms.CharField(widget=forms.TextInput({'placeholder': 'Имя', 'autocomplete': 'on'})
                           ,required=True,label='',max_length=20)
    phone = forms.CharField(widget=forms.TextInput({'placeholder': 'Телефон', 'autocomplete': 'on'})
                                                   ,required=True,label='',max_length=13)
    email = forms.CharField(widget=forms.EmailInput({'placeholder': 'example@mail.ru', 'autocomplete': 'on'}),
                            label='', max_length=30, )
    city = forms.CharField(widget=forms.TextInput({'placeholder': 'Город/населённый пункт', 'autocomplete': 'on'})
                                                  ,required=True,label='',max_length=30)
    street = forms.CharField(widget=forms.TextInput({'placeholder': 'Улица', 'autocomplete': 'on'})
                             ,required=True,label='',max_length=30)
    text = forms.CharField(widget=forms.Textarea({'placeholder': 'Дополнение к заказу', 'autocomplete': 'on'})
                           ,required=False,label='',max_length=300,)

    def __init__(self, *args, **kwargs):
        super(CheckoutContactForm, self).__init__(*args, **kwargs)

        self.fields['phone'].help_text = 'Пример (+380503337788).Не более 13 символов.'
        self.fields['email'].help_text = 'Пример (example@mail.ru).Не более 30 символов.'




class CartForm(forms.Form):
    # name = forms.CharField(required=True)
    # phone = forms.CharField(required=True)
    nmb = forms.CharField(required=True)



