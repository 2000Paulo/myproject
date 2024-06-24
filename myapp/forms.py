from django import forms
from .models import Objeto
from .models import MeuObjeto

class ObjetoForm(forms.ModelForm):
    class Meta:
        model = Objeto
        fields = ('nome', 'descricao')

class MeuObjetoForm(forms.ModelForm):
    class Meta:
        model = MeuObjeto
        fields = ['campo_texto']