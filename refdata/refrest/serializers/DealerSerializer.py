from rest_framework import serializers

from ..models.model.Dealer import Dealer


class DealerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dealer
        fields = ['code',
                  'name',
                  'locked',
                  'create_time',
                  'update_time',
                  'item_uuid',
                  'effective_date',
                  'expiration_date',
                  ]
