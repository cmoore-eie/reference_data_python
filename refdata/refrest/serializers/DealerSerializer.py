from drf_writable_nested import WritableNestedModelSerializer

from .DealerLocationSerializer import DealerLocationSerializer
from ..models.model.Dealer import Dealer
from ..models.model.DealerLocation import DealerLocation
from ..utils.ChildType import ChildType
from ..utils.ChildUpdate import update_item


class DealerSerializer(WritableNestedModelSerializer):
    dealer_locations = DealerLocationSerializer(many=True)

    def update(self, instance, validated_data):
        location_data = validated_data.pop("dealer_locations")

        for field, value in validated_data.items():
            setattr(instance, field, value)

        update_item(instance, location_data, ChildType.DEALER_LOCATION)

        instance.save()

        return instance

    def create(self, validated_data):
        location_data = validated_data.pop("dealer_locations")
        dealer = Dealer.objects.create(**validated_data)

        for location in location_data:
            DealerLocation.objects.create(dealer=dealer, **location)

        return dealer

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
                  'dealer_locations',
                  ]
