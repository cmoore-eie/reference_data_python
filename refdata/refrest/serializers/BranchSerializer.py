from rest_framework import serializers

from ..models.model.Branch import Branch


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ['code',
                  'name',
                  'locked',
                  'create_time',
                  'update_time',
                  'item_uuid',
                  'effective_date',
                  'expiration_date',
                  'BranchType',
                  ]
