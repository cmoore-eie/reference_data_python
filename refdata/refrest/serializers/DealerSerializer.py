from django.core.exceptions import ObjectDoesNotExist
from drf_writable_nested import WritableNestedModelSerializer

from .DealerLocationSerializer import DealerLocationSerializer
from ..models.model.Dealer import Dealer
from ..models.model.DealerLocation import DealerLocation
from ..utils.ChildType import ChildType
from ..utils.ChildUpdate import update_item


class DealerSerializer(WritableNestedModelSerializer):
    locations = DealerLocationSerializer(many=True)

    def update(self, instance, validated_data):
        print(validated_data)
        location_data = validated_data.pop("locations")

        for field, value in validated_data.items():
            setattr(instance, field, value)
            print(location_data)
            update_item(instance, location_data, ChildType.DEALER_LOCATION)

        instance.save()

        return instance

    def create(self, validated_data):
        location_data = validated_data.pop("locations")
        dealer_item = Dealer.objects.update_or_create(**validated_data)[0]
        print(dealer_item)
        for location_item in location_data:
            print(location_item)
            DealerLocation.objects.create(dealer=dealer_item, **location_item)
        return dealer_item

    class Meta:
        model = Dealer
        fields = ['code',
                  'name',
                  'locked',
                  'createTime',
                  'updateTime',
                  'itemIdentifier',
                  'effectiveDate',
                  'expirationDate',
                  'locations',
                  ]
