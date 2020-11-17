from django.db import models
from django.utils.translation import ugettext_lazy as _

from utils.models import Timestamps



class Lecture(Timestamps, models.Model):
    title = models.CharField(_("Title"), max_length=250)
    lecturer_name = models.CharField(_("Lecturer"), max_length=250, default='', blank=True)
    duration = models.IntegerField(_("Duration"), default=2, help_text='Enter duration in hours')
    description = models.TextField(_("Description"))
    date = models.DateField(_("Date"))
    slides_url = models.CharField(_("Slides Url"), max_length=250)

    is_required = models.BooleanField(_("Is Required"), default=True)

    def __str__(self):
        return self.title
    