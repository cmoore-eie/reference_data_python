from rest_framework import serializers

from ..models.model.Gender import Gender


class GenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gender
        fields = ['code',
                  'name',
                  'locked',
                  'create_time',
                  'update_time',
                  'item_uuid',
                  'effective_date',
                  'expiration_date',
                  ]
