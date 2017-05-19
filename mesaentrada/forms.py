from django import forms
from .models import Nota


# uso solamente ModelForm no uso Form comuncitos
class NotaModelForm(forms.ModelForm):
    class Meta:
        model = Nota
        fields = ['idficha', 'area', 'descripcion']
