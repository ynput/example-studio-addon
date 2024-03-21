import ayon_api
import pyblish.api

from my_studio_addon import ADDON_NAME, __version__


class CollectMyStudioData(pyblish.api.ContextPlugin):
    order = pyblish.api.CollectorOrder
    label = "Collect My Studio Data"

    # This can be changed by settings
    enabled = True

    def process(self, context):
        url = ayon_api.get_addon_url(ADDON_NAME, __version__, "studio-data")
        response = ayon_api.get(url)
        context.data["myStudioData"] = response.data
