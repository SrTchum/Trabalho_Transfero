from django import forms
from sistema.models import Filme  # 👈 Importe o modelo corrigido

class FilmeForm(forms.ModelForm):
    class Meta:
        model = Filme
        fields = ['nome', 'ano', 'estudio', 'genero', 'sinopse']