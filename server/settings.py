from typing import Literal, TYPE_CHECKING

from pydantic import Field, validator

from ayon_server.lib.postgres import Postgres
from ayon_server.settings import BaseSettingsModel, ensure_unique_names, normalize_name,SettingsField
from ayon_server.settings.enum import folder_types_enum
from ayon_server.types import (
    ColorRGB_hex,
    ColorRGBA_hex,
    ColorRGB_float,
    ColorRGBA_float,
    ColorRGB_uint8,
    ColorRGBA_uint8,
)


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
