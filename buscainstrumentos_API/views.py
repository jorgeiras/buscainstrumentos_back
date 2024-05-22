
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.db.models import Q
from .mypagination import CustomPageNumberPagination

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
        instruments = Instrument.objects.filter(Q(name__exact=nameInst) | Q(name__contains=nameInst)).order_by('id')

        paginator = CustomPageNumberPagination()  # Instantiate the paginator
        page = paginator.paginate_queryset(instruments, request)  # Paginate the queryset

        if page is not None:
            serializer = InstrumentSerializer(page, many=True)
            return paginator.get_paginated_response(serializer.data)  # Use the paginated response

        # Fallback for non-paginated response (optional)
        serializer = InstrumentSerializer(instruments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



class InstrumentosAll(APIView):

    def get(self, request):
        instruments = Instrument.objects.all().order_by('id')
        paginator = CustomPageNumberPagination()  # Instantiate the paginator
        page = paginator.paginate_queryset(instruments, request)  # Paginate the queryset

        if page is not None:
            serializer = InstrumentSerializer(page, many=True)
            return paginator.get_paginated_response(serializer.data)  # Use the paginated response

        # Fallback for non-paginated response (optional)
        serializer = InstrumentSerializer(instruments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

        
class Test(APIView):
    def get(self, request):
        return Response("hola mundooo", status=status.HTTP_200_OK)
        
        