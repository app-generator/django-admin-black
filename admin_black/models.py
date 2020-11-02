from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _


class AdminBlackSetting(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT, related_name='admin_black_setting')
    sidebar_background = models.CharField(_('sidebar background'), max_length=20, default='primary')
    dark_mode = models.BooleanField(_('dark mode'), default=True)
    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated at"), auto_now=True)

    class Meta:
        verbose_name = _('dashboard setting')
        verbose_name_plural = _('dashboard settings')
