pretalx Acronia rename plugin
==========================

This is a plugin for `pretalx`_.
Pretalx plugin to change some pretalx wording

Development setup
-----------------

1. Make sure that you have a working `pretalx development setup`_.

2. Clone this repository, eg to ``local/pretalx-acronia-rename``.

3. Activate the virtual environment you use for pretalx development.

4. Run ``pip install -e .`` within this directory to register this application with pretalx's plugin registry.

5. Run ``make`` within this directory to compile translations.

6. In the settings.py of the main pretalx project add the following:

    a) to the LOCALE_PATHS add the path to this plugin's locale directory, e.g.::

        LOCALE_PATHS = [
            ...,
            'your_path_to_the_plugin_folder/pretalx-acronia-rename/locale',
        ]
    b) to the LANGUAGES_INFORMATION add the following entries::

        LANGUAGES_INFORMATION = {
            ...,
            "en-acronia": {
                "name": _("English (Acronia)"),
                "natural_name": "English",
                "official": False,
                "percentage": 100,
                "public_code": "en_Acronia",
            },
            "de-acronia": {    
                "name": _("Deutsch (Acronia)"),
                "natural_name": "Deutsch",
                "official": False,
                "percentage": 100,
                "public_code": "de_Acronia",
            },
        }

7. Restart your local pretalx server. This plugin should show up in the plugin list shown on startup in the console.
   You can now use the plugin from this repository for your events by enabling it in the 'plugins' tab in the settings.

8. In the settings of your event, you can now select the language "English (Acronia)" or "Deutsch (Acronia)".

This plugin has CI set up to enforce a few code style rules. To check locally, you need these packages installed::

    pip install flake8 flake8-bugbear isort black

To check your plugin for rule violations, run::

    black --check .
    isort -c .
    flake8 .

You can auto-fix some of these issues by running::

    isort .
    black .


License
-------

Copyright 2025 Nora Küchler

Released under the terms of the Apache License 2.0


.. _pretalx: https://github.com/pretalx/pretalx
.. _pretalx development setup: https://docs.pretalx.org/en/latest/developer/setup.html
