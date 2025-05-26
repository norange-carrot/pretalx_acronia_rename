
from django.dispatch import receiver

from pretalx.common.signals import register_locales


@receiver(register_locales)
def register_locales(**kwargs):
    event = kwargs.pop("sender", None)
    if event:
        if "pretalx_acronia_rename" not in getattr(event, "plugin_list", None) or []:
            return []
    return ["my-lang"]

