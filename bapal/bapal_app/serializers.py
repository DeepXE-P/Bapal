from rest_framework import serializers
from .models import Test

class TestSerializer(serializers.ModelSerializer):
    # def perform_create(self, serializer):
    #     serializer.save(Test = self.request.test)

    class Meta:
        model=Test
        fields="__all__" 