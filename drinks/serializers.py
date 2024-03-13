# the process of going python object to Json
from rest_framework import serializers
from .models import Drink

# when we trying to return our model through our API
class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drink
        fields = ['id', 'name', 'description']