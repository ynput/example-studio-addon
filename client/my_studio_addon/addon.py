import os
from ayon_core.addon import AYONAddon, IPluginPaths

MY_STUDIO_ADDON_ROOT = os.path.dirname(os.path.abspath(__file__))
ADDON_NAME = "my_studio_addon"


class MyStudioAddon(AYONAddon, IPluginPaths):
    name = ADDON_NAME

    def get_plugin_paths(self):
        return {
            "publish": [
                os.path.join(MY_STUDIO_ADDON_ROOT, "plugins", "publish")
            ]
        }
