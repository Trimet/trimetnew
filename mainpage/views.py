# Create your views here.

from django.http import HttpResponse
from django.template import RequestContext, loader


def show_index(request):

    template = loader.get_template('mainpage/index.html')

    context = RequestContext(request, {
        'hello': 'hello, username',
    })

    return HttpResponse(template.render(context))
