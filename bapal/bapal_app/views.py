from urllib import response
from django.shortcuts import render
from rest_framework.response import Response
from .models import Test
from rest_framework.views import APIView
from .serializers import TestSerializer
from rest_framework import status

# Create your views here.
class TestListAPI(APIView):
    def get(self, request):
        queryset=Test.objects.all()
        print(queryset)
        serializer=TestSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TestSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save() # 저장하는 구문
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request):
        queryset=Test.objects.all()
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

def test_view(request):
    tests = Test.objects.all()

    return render(request, 'bapal_app/index.html', {'tests': tests})

def index(request):
    return render(request, 'bapal_app/index.html')