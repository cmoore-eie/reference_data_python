from rest_framework import serializers

from ..models.model.Gender import Gender


class GenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gender
        fields = ['code',
                  'name',
                  'locked',
                  'createTime',
                  'updateTime',
                  'itemIdentifier',
                  'effectiveDate',
                  'expirationDate',
                  ]
