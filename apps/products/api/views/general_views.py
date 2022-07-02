from rest_framework import viewsets

from apps.products.api.serializers.general_serializers import MeasureUnitSerializer, IndicatorSerializer, CategoryProductSerializer
from apps.base.api import GeneralListApiView

class MeasureUnitViewSet(viewsets.ModelViewSet):
    """Swagger allows us documentation our code

    Options:
        We are more specific with define HTTP method:
        def list():
        def retrive():
        etc.
    Others:
        On defect Swapper works automatic with ModelViwSet, if we are work ViewSet
        We need to define HTTP method so that swagger cath our code.
    """
    serializer_class = MeasureUnitSerializer

class IndicatorViewSet(viewsets.ModelViewSet):
    serializer_class = IndicatorSerializer

class CategoryProductViewSet(viewsets.ModelViewSet):
    serializer_class = CategoryProductSerializer
    

 
    
