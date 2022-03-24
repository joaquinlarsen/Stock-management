from django.forms import ModelForm
from .models import Venta


class VentaForm(ModelForm):
    class Meta:
        model = Venta
        fields = "__all__"
