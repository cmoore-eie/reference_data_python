from ..filters.DealerFilterSet import DealerFilterSet
from ..models.model.Dealer import Dealer
from ..serializers.DealerSerializer import DealerSerializer
from rest_framework import viewsets


class DealerViewSet(viewsets.ModelViewSet):
    queryset = Dealer.objects.all()
    serializer_class = DealerSerializer
    filterset_class = DealerFilterSet
