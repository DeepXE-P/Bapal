from django.shortcuts import render

# Create your views here.
from .models import Test

def test_view(request):
    tests = Test.objects.all()

    return render(request, 'bapal_app/index.html', {'tests': tests})

def index(request):
    return render(request, 'bapal_app/index.html')