
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

@receiver(html_head, dispatch_uid="acronia_html_head")
def add_stylesheet(sender, request, **kwargs):
    if "de-acronia" and "en-acronia" not in request.event.locales:
        return ""
    template = get_template("pretalx_acronia_rename/style.html")
    return template.render()
