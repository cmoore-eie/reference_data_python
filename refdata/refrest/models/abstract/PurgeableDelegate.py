from django.db import models

'''
This abstract class is added to models that require to have the purge or retire flags
for additional processing of the object.
'''


class PurgeDelegate(models.Model):
    purge = models.BooleanField(default=False, null=True, blank=True)

    class Meta:
        abstract = True
