from typing import Type

from nxtools import logging

from ayon_server.addons import BaseServerAddon
from ayon_server.api.dependencies import CurrentUser, ProjectName
from ayon_server.entities import FolderEntity
from ayon_server.exceptions import NotFoundException
from ayon_server.lib.postgres import Postgres


from .settings import ExampleSettings
from .site_settings import ExampleSiteSettings


class ExampleAddon(BaseServerAddon):
    settings_model: Type[ExampleSettings] = ExampleSettings
    site_settings_model: Type[ExampleSiteSettings] = ExampleSiteSettings

    # frontend_scopes defines, where the web frontend of the addon
    # should be displayed in openpype web app. Currently only "project"
    # is supported. Additional arguments may be passed (in this case)
    # to show the project hierarchy sidebar. This feature is not yet
    # fully functional and will be changed in the future.

    frontend_scopes: dict[str, dict[str, str]] = {"settings": {}}

    # intitalize method is called during the addon initialization
    # You can use it to register its custom REST endpoints

    def initialize(self):
        logging.info("Example addon INIT")
        self.add_endpoint(
            "studio-data",
            self.get_studio_data,
            method="GET",
        )

    async def setup(self):
        pass

        # If the addon makes a change in server configuration,
        # e.g. adding a new attribute, you may trigger a server
        # restart by calling self.restart_server()
        # Use it with caution and only when necessary!
        # You don't want to restart the server every time the addon is loaded.

        # self.request_server_restart()

    # Example REST endpoint
    # Depends(dep_current_user) ensures the request is authenticated

    async def get_studio_data(
        self,
        user: CurrentUser
    ):
        """Return a random folder from the database"""
        return {
            "secret-of-the-studio": "There is no secret"
        }
