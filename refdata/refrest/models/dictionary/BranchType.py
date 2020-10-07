from django.db import models


class BranchType(models.TextChoices):
    LOCAL = "local", "Local"
    MAIN = "main", "Main"
