
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.db.models import Q


from buscainstrumentos_API.models import Instrument
from buscainstrumentos_API.serializers import InstrumentSerializer


class InstrumentosList(APIView):

    def post(self, request):
        serializer = InstrumentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class InstrumentosDetails(APIView):

    def get(self, request):
        nameInst = request.GET.get('name')
        instruments = Instrument.objects.filter(Q(name__exact=nameInst) | Q(name__contains=nameInst))
        serializer = InstrumentSerializer(instruments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



class InstrumentosAll(APIView):

    def get(self, request):
        instruments = Instrument.objects.all()
        serializer = InstrumentSerializer(instruments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

        
    
        
        