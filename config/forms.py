from .models import UnidadeFederativa
from django.forms import ModelForm

class UnidadeFederativaForm(ModelForm):
    class Meta:
        model = UnidadeFederativa
        fields = '__all__'