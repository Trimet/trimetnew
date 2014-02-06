#-*- coding:utf-8 -*-

from django.http import HttpResponse
from django.template import RequestContext, loader


def show_index(request):

    if request.is_ajax():
        template = loader.get_template('services/index_ajax.html')
    else:
        template = loader.get_template('services/index.html')

    context = RequestContext(request, {
        'cmenu': 'services',
        'title': 'Услуги',
        'smenu': 'metalwork',
    })

    return HttpResponse(template.render(context))

def show_metalwork(request):

    if request.is_ajax():
        template = loader.get_template('services/metalwork_ajax.html')
    else:
        template = loader.get_template('services/index.html')

    context = RequestContext(request, {
        'cmenu': 'services',
        'title': 'Услуги',
        'smenu': 'metalwork',
    })

    return HttpResponse(template.render(context))
