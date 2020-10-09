from rest_framework import serializers

from ..models.model.DealerLocation import DealerLocation


class DealerLocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = DealerLocation
        fields = ['locationName',
                  'addressLine1',
                  'addressLine2',
                  'city',
                  'postCode',
                  'purge',
                  'itemIdentifier',
                  ]
