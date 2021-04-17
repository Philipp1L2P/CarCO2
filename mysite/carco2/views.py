from django.http import HttpResponse

import datetime

def index(request):
    return HttpResponse("Ahoi, hier ist die Benutzerbedienungoberfläche im Django")

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)