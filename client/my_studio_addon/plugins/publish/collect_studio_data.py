import ayon_api
import pyblish.api

from my_studio_addon import ADDON_NAME, __version__


class CollectMyStudioData(pyblish.api.ContextPlugin):
    order = pyblish.api.CollectorOrder
    label = "Collect My Studio Data"

    settings_category = "my_studio_addon"

    # This can be changed by settings
    enabled = True

    def process(self, context):
        response = ayon_api.get(
            f"addons/{ADDON_NAME}/{__version__}/studio-data"
        )
        response.raise_for_status()
        self.log.debug("MyStudio data: %s", response.data)
        context.data["myStudioData"] = response.data
