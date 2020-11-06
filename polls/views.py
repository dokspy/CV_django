from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template('polls/index.html')
    return HttpResponse(template.render({}, request))


def cvOfficial(request):
    template = loader.get_template('polls/cvofficial.html')
    return HttpResponse(template.render({}, request))


def engcv(request):
    template = loader.get_template('polls/engcv.html')
    return HttpResponse(template.render({}, request))


def UA_CV_Official(request):
    template = loader.get_template('polls/UACVOfficial.html')
    return HttpResponse(template.render({}, request))


def data(request):
    template = loader.get_template('polls/2.html')
    return HttpResponse(template.render({}, request))
