from .AbstractReferenceFilterSet import AbstractReferenceFilterSet
from ..models.model.Dealer import Dealer


class DealerFilterSet(AbstractReferenceFilterSet):
    class Meta:
        model = Dealer
        fields = ['with_uuid',
                  'with_code',
                  'with_name',
                  'with_effectiveDate',
                  'with_expirationDate',
                  ]
