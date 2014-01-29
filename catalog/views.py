#-*- coding:utf-8 -*-

from django.http import HttpResponse
from django.template import RequestContext, loader


def show_index(request):

    if request.is_ajax():

        template = loader.get_template('catalog/index_ajax.html')

        context = RequestContext(request, {
            'hello': 'Здесь можно купить металл онлайн',
            'cmenu': 'catalog',
            'title': 'Онлайн прайс',
        })

        return HttpResponse(template.render(context))


    else:

        template = loader.get_template('catalog/index.html')

        context = RequestContext(request, {
            'hello': 'Здесь можно купить металл онлайн',
            'cmenu': 'catalog',
            'title': 'Онлайн прайс',
        })

        return HttpResponse(template.render(context))
