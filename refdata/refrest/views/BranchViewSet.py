from ..filters.BranchFilterSet import BranchFilterSet
from ..models.model.Branch import Branch
from ..serializers.BranchSerializer import BranchSerializer
from rest_framework import viewsets


class BranchViewSet(viewsets.ModelViewSet):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer
    filterset_class = BranchFilterSet
