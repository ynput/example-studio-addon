from typing import Literal, TYPE_CHECKING

from pydantic import Field, validator

from ayon_server.settings import BaseSettingsModel,SettingsField


class CollectMyStudioDataModel(BaseSettingsModel):
    enabled : bool = SettingsField(True, title = "Enabled")


class PublishPluginsModel(BaseSettingsModel):
    CollectMyStudioData: CollectMyStudioDataModel = SettingsField(
        default_factory = CollectMyStudioDataModel,
        title = "Publish"
    )

class PluginsModel(BaseSettingsModel):
    publish: PublishPluginsModel = SettingsField(
        default_factory = PublishPluginsModel,
        title = "Publish"
    )

class ExampleSettings(BaseSettingsModel):
    """Test addon settings.


    This is a test addon settings. It is used to test various
    features of the settings system.

    Docstrings are propagated to the frontend, so you can use
    them to describe your settings, submodels and their fields.

    On the frontend, docstrings are rendered as markdown, so you
    can use markdown syntax to format your descriptions, e.g.:
    **bold** , *italic* , `code`, [links](https://openpype.io)...
    """
    plugins: PluginsModel = SettingsField(
        default_factory = PluginsModel,
        title = "Plugins"
    )

# class ExampleSettings(BaseSettingsModel):
#     """Test addon settings"""
#
#     colors: Colors = Field(default_factory=Colors, title="Colors")
