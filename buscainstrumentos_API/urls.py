from django.urls import path, re_path
from buscainstrumentos_API.views import InstrumentosList, InstrumentosDetails, InstrumentosAll, Test

urlpatterns = [
    path("addInstrument", InstrumentosList.as_view()),
    path("listInstrument", InstrumentosAll.as_view()),
    path('test', Test.as_view()),
    re_path(r'^searchInstrument/$', InstrumentosDetails.as_view()),
]