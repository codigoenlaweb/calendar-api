from django.db import models
from django.utils.translation import gettext_lazy as _
from modules.users.models import User
from django.core.validators import MinLengthValidator

# Model Event.
class Event(models.Model):
    """Model definition for Event."""
    title = models.CharField(_("title"), max_length=255, validators=[MinLengthValidator(3)])
    note = models.TextField(_("note"), blank=True, null=True)
    start = models.DateTimeField(_("start"))
    end = models.DateTimeField(_("end"))
    user = models.ForeignKey(User(), on_delete=models.CASCADE, related_name='events')

    class Meta:
        """Meta definition for Event."""

        verbose_name = 'Event'
        verbose_name_plural = 'Events'

    def __str__(self):
        """Unicode representation of Event."""
        return f'{self.title}'

    # TODO: Define custom methods here
