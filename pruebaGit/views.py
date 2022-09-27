from django.http import HttpResponse

def hola(request):
    return HttpResponse('<h1>ESTO ES NUEVO</h1>')