from rest_framework import serializers
from instrCopyAPI.models import Instrument


class InstrumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instrument
        fields = ('Id','name', 'price', 'link','WebSite')