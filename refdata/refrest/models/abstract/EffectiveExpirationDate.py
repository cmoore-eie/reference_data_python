from django.db import models


class EffectiveExpirationDate(models.Model):
    effective_date = models.DateField(max_length=20, null=False)
    expiration_date = models.DateField(max_length=20, null=True, blank=True)

    class Meta:
        abstract = True
