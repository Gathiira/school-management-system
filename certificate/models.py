from django.db import models
from django.utils.translation import ugettext_lazy as _

from utils.models import Timestamps


class CertificateModel(Timestamps, models.Model):
    name = models.CharField(_("Name"), max_length=250)
    description = models.TextField(_("Description"))
