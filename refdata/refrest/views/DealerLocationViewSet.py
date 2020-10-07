from ..models.model.DealerLocation import DealerLocation
from ..serializers.DealerLocationSerializer import DealerLocationSerializer
from rest_framework import viewsets


class DealerLocationViewSet(viewsets.ModelViewSet):
    queryset = DealerLocation.objects.all()
    serializer_class = DealerLocationSerializer
