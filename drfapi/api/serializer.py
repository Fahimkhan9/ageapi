from rest_framework import serializers

class AgeSerializer(serializers.Serializer):
   
   age = serializers.IntegerField()