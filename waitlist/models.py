from django.db import models
from django.utils.translation import ugettext_lazy as _

from utils.models import Timestamps

LEVEL_CHOICES = [
    ('PRI','PRI' ),
    ('SEC','SEC'),
    ('CAMPUS', 'CAMPUS')
]

class WaitlistEntry(Timestamps, models.Model):
    first_name = models.CharField(_("First Name"), max_length=250)
    last_name = models.CharField(_("Second Name"), max_length=250)
    email = models.EmailField(_("Email"), max_length=254, unique=True)
    notes = models.TextField(_("Notes"))

    level = models.CharField(_("Level"), choices=LEVEL_CHOICES, default='SEC', max_length=255)
    
    class Meta:
        verbose_name_plural = 'Waitlist Entries'

    def __str__(self):
        return self.first_name + ' ' + self.last_name
