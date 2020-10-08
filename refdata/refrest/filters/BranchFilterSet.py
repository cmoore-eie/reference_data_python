from .AbstractReferenceFilterSet import AbstractReferenceFilterSet
from ..models.model.Branch import Branch


class BranchFilterSet(AbstractReferenceFilterSet):
    class Meta:
        model = Branch
        fields = ['with_uuid',
                  'with_code',
                  'with_name',
                  'with_effectiveDate',
                  'with_expirationDate',
                  ]
