from rest_framework import serializers
from .models import c2

class c2Serializer(serializers.ModelSerializer):

    class Meta:

        model = c2
        fields = '__all__'
