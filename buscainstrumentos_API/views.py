
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
        category = request.GET.get('category')
        min_price = request.GET.get('minPrice')
        max_price = request.GET.get('maxPrice')

        filters = Q()

        if nameInst:
            filters &= Q(name__icontains=nameInst)

        if category:
            filters &= Q(category__iexact=category)

        if min_price:
            filters &= Q(price__gte=min_price)

        if max_price and max_price != 'Infinity':
            filters &= Q(price__lte=max_price)

        instruments = Instrument.objects.filter(filters).order_by('id')

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
        category = request.GET.get('category')
        min_price = request.GET.get('minPrice')
        max_price = request.GET.get('maxPrice')

        filters = Q()

        if category:
            filters &= Q(category__iexact=category)

        if min_price:
            filters &= Q(price__gte=min_price)

        if max_price and max_price != 'Infinity':
            filters &= Q(price__lte=max_price)

        instruments = Instrument.objects.filter(filters).order_by('id')
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
        
        