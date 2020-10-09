from django.db import models


class EffectiveExpirationDate(models.Model):
    effectiveDate = models.DateField(max_length=20, null=False)
    expirationDate = models.DateField(max_length=20, null=True, blank=True)

    class Meta:
        abstract = True
