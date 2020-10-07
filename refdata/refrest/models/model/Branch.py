from django.db import models

from ..abstract.BaseDelegate import BaseDelegate
from ..abstract.EffectiveExpirationDate import EffectiveExpirationDate
from ..dictionary.BranchType import BranchType


class Branch(BaseDelegate, EffectiveExpirationDate):
    objects = models.Manager()

    BranchType = models.CharField(
        max_length=30,
        choices=BranchType.choices,
        default=BranchType.LOCAL
    )
