from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Cliente
from .forms import ClienteForm, BuscaClienteForm


def lista_cliente(request):
    pessoas = Cliente.objects.all()
    return render(request, 'lista_cliente.html', {'pessoas': pessoas})

def cliente(request, id):
    pessoa = Cliente.objects.get(pk=id)
    return render(request, 'cliente.html', {'pessoa': pessoa})

@login_required
def novo_cliente(request):
    novo_form = ClienteForm(request.POST or None, request.FILES or None)

    if novo_form.is_valid():
        novo_form.save()
        return redirect('lista_cliente')
    return render(request, 'cliente_form.html', {'novo_form': novo_form})

@login_required
def update_cliente(request, id):
    pes = Cliente.objects.get(pk=id)
    client_form = ClienteForm(
        request.POST or None,
        request.FILES or None,
        instance=pes
    )

    if client_form.is_valid():
        client_form.save()
        return redirect('lista_cliente')

    return render(request, 'cliente_form.html', {'client_form': client_form, 'pes': pes})

@login_required
def delete_cliente(request, id):
    pessoa = Cliente.objects.get(pk=id)

    if request.method == 'POST':
        pessoa.delete()
        return redirect('lista_cliente')

    return render(request, 'delete_cliente.html', {'pessoa': pessoa})


@login_required
def busca_cliente(request):
    busca_form = BuscaClienteForm(request.POST or None)

    if busca_form.is_valid():
        fname = busca_form.instance.first_name
        lname = busca_form.instance.last_name
        pessoa = Cliente.objects.get(first_name__icontains=fname, last_name__icontains=lname)
        return cliente(request, pessoa.id)

    return render(request, 'busca_cliente.html', {'busca_form': busca_form})

