from django.shortcuts import render
from .tasks import test_func
from django.http import HttpResponse


def test(request):
    test_func.delay()
    return HttpResponse("Done")
# Create your views here.
