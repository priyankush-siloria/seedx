from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Seed(models.Model):
    STATUS = (
        ("OK", "OK"),
        ("INVALID", "INVALID")
    )
    row = models.IntegerField(_("row"), null=False)
    col = models.IntegerField(_("col"), null=False)
    status = models.CharField(_("status"),choices=STATUS ,max_length=7)
    tags = models.ManyToManyField("core.Tag", verbose_name=_("tags"))

    def __str__(self):
        return f"{self.row}, {self.col} | {self.status}"
    

class Tag(models.Model):
    tag_type = models.CharField(_("tag type"), max_length=50, null=False)
    value = models.CharField(_("tag value"), max_length=50, null=False)
    short_name = models.CharField(_("tag short name"), max_length=50, null=False, unique=True)
    deleted = models.BooleanField(_("deleted"), default=False)

    class Meta:
        unique_together = ("tag_type", "value")

    def __str__(self) -> str:
        return f"{self.tag_type} - {self.value} - {self.short_name}"
