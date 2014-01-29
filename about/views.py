#-*- coding:utf-8 -*-

from django.http import HttpResponse
from django.template import RequestContext, loader


def show_index(request):

    if request.is_ajax():

        template = loader.get_template('about/index_ajax.html')

        context = RequestContext(request, {
            'hello': 'Это страница о компании',
            'cmenu': 'about',
            'title': 'О компании',
        })

        return HttpResponse(template.render(context))


    else:

        template = loader.get_template('about/index.html')

        context = RequestContext(request, {
            'hello': 'Это страница о компании',
            'cmenu': 'about',
            'title': 'О компании',
        })

        return HttpResponse(template.render(context))


def show_history(request):

    if request.is_ajax():

        template = loader.get_template('about/history_ajax.html')
        context = RequestContext(request, {})

        return HttpResponse(template.render(context))

    else:

        template = loader.get_template('about/history.html')

        context = RequestContext(request, {
            'cmenu': 'about',
            'smenu': 'history',
            'title': 'О компании | История'
        })

        return HttpResponse(template.render(context))

def show_photo(request):

    if request.is_ajax():

        template = loader.get_template('about/test_ajax.html')
        context = RequestContext(request, {})

        return HttpResponse(template.render(context))

    else:

        template = loader.get_template('about/test.html')

        context = RequestContext(request, {
            'cmenu': 'about',
            'smenu': 'photo',
            'title': 'О компании | История'
        })

        return HttpResponse(template.render(context))

def show_leadership(request):

    if request.is_ajax():

        template = loader.get_template('about/test_ajax.html')
        context = RequestContext(request, {})

        return HttpResponse(template.render(context))

    else:

        template = loader.get_template('about/test.html')

        context = RequestContext(request, {
            'cmenu': 'about',
            'smenu': 'leaderships',
            'title': 'О компании | История'
        })

        return HttpResponse(template.render(context))

def show_strong(request):

    if request.is_ajax():

        template = loader.get_template('about/test_ajax.html')
        context = RequestContext(request, {})

        return HttpResponse(template.render(context))

    else:

        template = loader.get_template('about/test.html')

        context = RequestContext(request, {
            'cmenu': 'about',
            'smenu': 'strong',
            'title': 'О компании | История'
        })

        return HttpResponse(template.render(context))

def show_awards(request):

    if request.is_ajax():

        template = loader.get_template('about/test_ajax.html')
        context = RequestContext(request, {})

        return HttpResponse(template.render(context))

    else:

        template = loader.get_template('about/test.html')

        context = RequestContext(request, {
            'cmenu': 'about',
            'smenu': 'awards',
            'title': 'О компании | История'
        })

        return HttpResponse(template.render(context))

def show_wordpress(request):

    if request.is_ajax():

        template = loader.get_template('about/test_ajax.html')
        context = RequestContext(request, {})

        return HttpResponse(template.render(context))

    else:

        template = loader.get_template('about/test.html')

        context = RequestContext(request, {
            'cmenu': 'about',
            'smenu': 'wordpress',
            'title': 'О компании | История'
        })

        return HttpResponse(template.render(context))

def show_partners(request):

    if request.is_ajax():

        template = loader.get_template('about/test_ajax.html')
        context = RequestContext(request, {})

        return HttpResponse(template.render(context))

    else:

        template = loader.get_template('about/test.html')

        context = RequestContext(request, {
            'cmenu': 'about',
            'smenu': 'partners',
            'title': 'О компании | История'
        })

        return HttpResponse(template.render(context))

def show_vacancies(request):

    if request.is_ajax():

        template = loader.get_template('about/test_ajax.html')
        context = RequestContext(request, {})

        return HttpResponse(template.render(context))

    else:

        template = loader.get_template('about/test.html')

        context = RequestContext(request, {
            'cmenu': 'about',
            'smenu': 'vacancies',
            'title': 'О компании | История'
        })

        return HttpResponse(template.render(context))
