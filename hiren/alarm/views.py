from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Api, Nisha
from .serializers import ApiSerializer, NishaSerializer
from rest_framework import viewsets
# Create your views here.


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


def test(request):
    if request.method == 'GET':
        api = Api.objects.all()
        serializer = ApiSerializer(api)
        print(serializer.data)
        return JSONResponse(serializer.data)


class ApiViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Api.objects.all()
    serializer_class = ApiSerializer