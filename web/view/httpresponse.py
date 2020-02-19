from django.http import HttpResponse
from django.template import loader


def redirect(path):
    return redirect(path)


def template(request, path, context):
    template = loader.get_template(path)
    return HttpResponse(template.render(context, request))
