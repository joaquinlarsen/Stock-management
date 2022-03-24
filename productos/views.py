from django.shortcuts import render, redirect
from productos.models import Producto
from .forms import ProductoForm
from .filters import ProductoFilter

# Create your views here.


def productos(request):
    productos = Producto.objects.all()

    myfilter = ProductoFilter(request.GET, queryset=productos)
    productos = myfilter.qs

    context = {"productos": productos, "myFilter": myfilter}
    return render(request, "productos/productos.html", context)


def createOrder(request):
    form = ProductoForm()
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")

    context = {
        "form": form,
    }
    return render(request, "productos/productos_form.html", context)


def updateOrder(request, pk):

    producto = Producto.objects.get(id_interno=pk)
    form = ProductoForm(instance=producto)
    if request.method == "POST":
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect("/")
    context = {
        "form": form,
    }
    return render(request, "productos/productos_form.html", context)


def deleteOrder(request, pk):
    producto = Producto.objects.get(id_interno=pk)
    if request.method == "POST":
        producto.delete()
        return redirect("/")
    context = {"item": producto}
    return render(request, "productos/delete.html", context)
