from django.forms import ModelForm
from django import forms
from .models import Person
from .models import Doc
class PersonForm(ModelForm):

    class Meta:
        model = Person
        fields = ['nome', 'idade',
                  'senha', 'email',
                  'endereço', 'cpf']


class docForm(ModelForm):

    class Meta:
        model = Doc
        fields = ['nome',
                  'senha', 'email',
                  'endereço', 'cnpj']
