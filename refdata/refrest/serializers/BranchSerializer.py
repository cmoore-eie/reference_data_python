from rest_framework import serializers

from ..models.model.Branch import Branch


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ['code',
                  'name',
                  'locked',
                  'createTime',
                  'updateTime',
                  'itemIdentifier',
                  'effectiveDate',
                  'expirationDate',
                  'BranchType',
                  ]
