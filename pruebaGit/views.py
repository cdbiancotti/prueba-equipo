from django.http import HttpResponse

def hola(request):
    return HttpResponse('<h1>ESTO ES NUEVO</h1>')


def cdb_vista(request):
    return HttpResponse('<h1>Esta vista la hizo cristian</h1>')