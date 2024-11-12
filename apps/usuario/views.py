from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ClienteForm

def registro_cliente(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registro exitoso, ya puede iniciar sesión con sus datos.')
            return redirect('login')
    else:
        form = ClienteForm()

    return render(request, 'registration/login.html', {'form': form})
