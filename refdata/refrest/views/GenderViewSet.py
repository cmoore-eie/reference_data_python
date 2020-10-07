from ..models.model.Gender import Gender
from ..serializers.GenderSerializer import GenderSerializer
from rest_framework import viewsets


class GenderViewSet(viewsets.ModelViewSet):
    queryset = Gender.objects.all()
    serializer_class = GenderSerializer
