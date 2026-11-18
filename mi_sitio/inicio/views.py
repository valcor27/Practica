from django.shortcuts import render

# Create your views here.
def hola_mundo(request):
    # Renderiza el HTML que creamos con Bootstrap
    return render(request, 'index.html') 
