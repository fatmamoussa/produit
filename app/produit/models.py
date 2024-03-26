from django.db import models
from autoslug import AutoSlugField
from django.utils.translation import gettext_lazy as _

class produit(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    thumbnail = models.ImageField(_("Logo"), upload_to="produit/%Y/%m/", default="default.png")
    slug = AutoSlugField(populate_from='name', unique=True)

