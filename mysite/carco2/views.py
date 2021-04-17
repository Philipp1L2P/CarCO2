from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. CarCO2 lives")