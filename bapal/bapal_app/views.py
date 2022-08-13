from urllib import response
from django.shortcuts import render
from rest_framework.response import Response
from .models import Test
from rest_framework.views import APIView
from .serializers import TestSerializer

# Create your views here.
class TestListAPI(APIView):
    def get(self, request):
        queryset=Test.objects.all()
        print(queryset)
        serializer=TestSerializer(queryset, many=True)
        return Response(serializer.data)

def test_view(request):
    tests = Test.objects.all()

    return render(request, 'bapal_app/index.html', {'tests': tests})

def index(request):
    return render(request, 'bapal_app/index.html')