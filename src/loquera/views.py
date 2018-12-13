import json

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.core.validators import RegexValidator
from django import forms
from django.http import HttpResponse, JsonResponse

# Create your views here.
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_http_methods
from django.views.generic import TemplateView


def giveme5():
    return "5"


class GeoCheck(forms.Form):
    lat = forms.IntegerField()
    lon = forms.IntegerField()
    city = forms.CharField()


@require_http_methods(["POST"])
def index(request, var1, mipk):
    isvalid = False
    form = GeoCheck(request.POST)
    isvalid = form.is_valid()
    # param  >     lat lon city
    v = giveme5()
    context = {
        'giveme5': v,
        'isvalid': isvalid,
        'form': form
    }
    return render(request, 'hola.html', context)


class NewForm(forms.Form):
    var1 = forms.IntegerField()
    mipk = forms.CharField(validators=[RegexValidator("^[0-9a-fA-F]+$")])


@require_http_methods(["GET"])
def index2(request):
    form = NewForm(request.GET)
    val = form.is_valid()
    if not val:
        return HttpResponse("UPS FALTAN COSAS")
    geoform = GeoCheck()
    context = {
        'form': geoform,
        'isvalid': True,
        'mipk': form.cleaned_data['mipk'],
        'var1': form.cleaned_data['var1']
    }
    return render(request, 'hola.html', context)


@method_decorator(login_required, name='dispatch')
class myView(TemplateView):
    template_name = 'templategeneric.html'

    # @login_required
    # def dispatch(self, *args, **kwargs):
    #     return super(myView, self).dispatch(*args, **kwargs)



def myjsonview(request ):
    contexto = {
        'a': 1,
        'b': 2,
        'c': 3
    }
    response = HttpResponse(json.dumps(contexto), content_type='application/json')
    return response

def myjson2(request):
    contexto = {
        'a': 1,
        'b': 2,
        'c': 3
    }
    return JsonResponse(contexto)