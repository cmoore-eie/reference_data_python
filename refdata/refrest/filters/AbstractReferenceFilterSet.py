import django_filters


class AbstractReferenceFilterSet(django_filters.FilterSet):
    with_uuid = django_filters.CharFilter(field_name='item_uuid', lookup_expr='exact')
    with_code = django_filters.CharFilter(field_name='code', lookup_expr='exact')
    with_name = django_filters.CharFilter(field_name='name', lookup_expr='exact')
    with_effectiveDate = django_filters.DateFilter(field_name='effectiveDate', lookup_expr='gte')
    with_expirationDate = django_filters.DateFilter(field_name='expirationDate', lookup_expr='lte')

    class Meta:
        abstract = True
