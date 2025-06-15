
from django.dispatch import receiver
from django.template.loader import get_template

from pretalx.common.signals import register_locales
import i18nfield
from pretalx.orga.signals import html_head

@receiver(register_locales)
def register_locales(**kwargs):
    event = kwargs.pop("sender", None)
    if event:
        if "pretalx_acronia_rename" not in getattr(event, "plugin_list", None) or []:
            return []
    return ["de-acronia", "en-acronia"]
