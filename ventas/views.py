from django.shortcuts import render, redirect
from .models import Venta
from .forms import VentaForm
from productos.models import Producto

# Create your views here.


def ventas(request):
    ventas = Venta.objects.all()
    context = {"ventas": ventas}
    return render(request, "ventas/ventas.html", context)


def createVenta(request):
    form = VentaForm()
    if request.method == "POST":
        form = VentaForm(request.POST)
        pk = form["producto"].value()
        cantidad_vendida = int(form["cantidad_vendida"].value())
        cantidad_stock = Producto.objects.get(pk=pk).cantidad_stock
        a = Producto.objects.get(pk=pk)

        a.cantidad_stock = cantidad_stock - cantidad_vendida
        a.save()

    if form.is_valid():
        form.save()
        return redirect("/ventas")
    context = {
        "form": form,
    }
    return render(request, "ventas/ventas_form.html", context)
