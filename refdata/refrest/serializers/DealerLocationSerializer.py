from rest_framework import serializers

from ..models.model.DealerLocation import DealerLocation


class DealerLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = DealerLocation
        fields = ['id',
                  'location_name',
                  'address_line1',
                  'address_line2',
                  'city',
                  'post_code',
                  'dealer',
                  'purge',
                  ]
