from django.db import models


class DealerLocation(models.Model):
    dealer = models.ForeignKey("Dealer", on_delete=models.CASCADE, related_name="dealer_locations", null=True)
    location_name = models.CharField(max_length=255, blank=True)
    address_line1 = models.CharField(max_length=255, blank=True)
    address_line2 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    post_code = models.CharField(max_length=255, blank=True)
    objects = models.Manager()
