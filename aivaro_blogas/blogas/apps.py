from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class BlogasConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blogas'
    verbose_name = _('blogas')