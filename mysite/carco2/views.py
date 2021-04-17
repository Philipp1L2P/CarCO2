from django.http import HttpResponse


def index(request):
    return HttpResponse("Ahoi, hier ist die Benutzerbedienungoberfläche im Django")