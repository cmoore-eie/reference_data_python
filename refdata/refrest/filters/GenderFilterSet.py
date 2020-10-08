from .AbstractReferenceFilterSet import AbstractReferenceFilterSet
from ..models.model.Gender import Gender


class GenderFilterSet(AbstractReferenceFilterSet):
    class Meta:
        model = Gender
        fields = ['with_uuid',
                  'with_code',
                  'with_name',
                  'with_effectiveDate',
                  'with_expirationDate',
                  ]
