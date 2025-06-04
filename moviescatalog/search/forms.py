from django import forms

class MovieSearchForm(forms.Form):
  query = forms.CharField(
    required=False,
    label='Buscar',
    widget=forms.TextInput(attrs={
      'placeholder': 'Título, sinopse, gênero ou pessoa',
      'class': 'form-control'
    })
  )
