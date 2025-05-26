from django.apps import AppConfig
from django.utils.translation import gettext_lazy

from . import __version__


class PluginApp(AppConfig):
    name = "pretalx_acronia_rename"
    verbose_name = "pretalx Acronia rename plugin"

    class PretalxPluginMeta:
        name = gettext_lazy("pretalx Acronia rename plugin")
        author = "Nora Küchler"
        description = gettext_lazy("Pretalx plugin to change some pretalx wording")
        visible = True
        version = __version__
        category = "LANGUAGE"

    def ready(self):
        from . import signals  # NOQA
