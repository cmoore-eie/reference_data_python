from django.db import models

from ..abstract.PurgeableDelegate import PurgeDelegate


class DealerLocation(PurgeDelegate):
    dealer = models.ForeignKey("Dealer", on_delete=models.CASCADE, related_name="locations", null=True, blank=True)
    itemIdentifier = models.CharField(max_length=255, primary_key=True)
    locationName = models.CharField(max_length=255, blank=True)
    addressLine1 = models.CharField(max_length=255, blank=True)
    addressLine2 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    postCode = models.CharField(max_length=255, blank=True)
    objects = models.Manager()

    class Meta:
        select_on_save = True
