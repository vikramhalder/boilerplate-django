from django.shortcuts import redirect

from web.view import httpresponse


def index(request):
    return httpresponse.template(request, "index.html", {})


def index_redirect(request):
    return redirect("/u", permanent=True)
