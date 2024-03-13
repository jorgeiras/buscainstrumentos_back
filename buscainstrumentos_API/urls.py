from django.urls import path, re_path
from buscainstrumentos_API.views import InstrumentosList, InstrumentosDetails, InstrumentosAll

urlpatterns = [
    path("addInstrument", InstrumentosList.as_view()),
    path("listInstrument", InstrumentosAll.as_view()),
    re_path(r'^searchInstrument/$', InstrumentosDetails.as_view()),
]