from django import forms


class MovelForm(forms.Form):
    titulo = forms.CharField(max_length=50)
    descricao = forms.CharField()
    preco = forms.DecimalField(decimal_places=2, min_value=0)
