from rest_framework import serializers
from buscainstrumentos_API.models import Instrument


class InstrumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instrument
        fields = ('id','name', 'price', 'link', 'image', 'location', 'category', 'expiration', 'publish','website')