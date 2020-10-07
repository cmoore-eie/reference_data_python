from django.db import models

from ..abstract.BaseDelegate import BaseDelegate
from ..abstract.EffectiveExpirationDate import EffectiveExpirationDate


class Dealer(BaseDelegate, EffectiveExpirationDate):
    objects = models.Manager()
