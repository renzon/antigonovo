from django import forms

from antigonovo.moveis.models import Movel


class MovelForm(forms.ModelForm):
    class Meta:
        model = Movel
        fields = 'titulo preco descricao foto'.split()
