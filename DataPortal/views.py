from django.shortcuts import render, HttpResponse
from Base.models import (
    Indicator
)

# Create your views here.


def index(request):
    return render(request, 'data_portal/index.html')


def detail_indicator(request, id):
    try:
        indicator = Indicator.objects.get(id=id)
    except Indicator.DoesNotExist:
        return HttpResponse(404)
    return render(request, 'data_portal/detail_indicator.html')