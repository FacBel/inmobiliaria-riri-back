from django.shortcuts import render


# Vista principal: la bienvenida de la API
def inicio(request):
    return render(request, "inicio.html")
