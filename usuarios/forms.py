from django import forms 
from sistema.models import Usuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario # Defina qual é o modelo que o form representa
        fields = ['nome', 'sobrenome', 'cpf', 'telefone', 'email', 'endereco',
              'imagem',] # São os campos que serão exibidos no form

