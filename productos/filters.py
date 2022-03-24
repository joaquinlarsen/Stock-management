import django_filters
from django_filters import DateFilter, CharFilter
from .models import Producto


class ProductoFilter(django_filters.FilterSet):
    nombre = CharFilter(field_name="nombre", lookup_expr="icontains")

    class Meta:
        model = Producto
        fields = "__all__"
