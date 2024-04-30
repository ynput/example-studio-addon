import os
from ayon_core.addon import (
    click_wrap,
    AYONAddon,
    IPluginPaths,
    ITrayAddon
)

MY_STUDIO_ADDON_ROOT = os.path.dirname(os.path.abspath(__file__))
ADDON_NAME = "my_studio_addon"
ADDON_LABEL = "My Studio Addon"

class MyStudioAddon(AYONAddon, IPluginPaths, ITrayAddon):
    name = ADDON_NAME
    label = ADDON_LABEL

    def initialize(self, settings):
        """Initialization of module."""
        self.enabled = True
        self._my_dialog = None


    def get_plugin_paths(self):
        return {
            "publish": [
                os.path.join(MY_STUDIO_ADDON_ROOT, "plugins", "publish")
            ]
        }

    # ITrayAddon
    def tray_init(self):
        """Tray init."""
        pass

    def tray_start(self):
        """Tray start."""
        pass

    def tray_exit(self):
        """Tray exit."""
        return

    def _get_my_dialog(self):
        if self._my_dialog is None:
            from .widgets.my_widgets import MyDialog

            self._my_dialog = MyDialog()

        return self._my_dialog

    def show_my_dialog(self):
        """Show dialog to My Dialog."""

        # Make sure dialog is created
        dialog = self._get_my_dialog()

        # Show dialog
        dialog.open()

           # Definition of Tray menu

    def tray_menu(self, tray_menu):
        # Menu for Tray App
        from qtpy import QtWidgets

        menu = QtWidgets.QMenu(self.label, tray_menu)
        menu.setProperty("submenu", "on")

        # Actions
        action_show_my_dialog = QtWidgets.QAction("My Dialog", menu)
        menu.addAction(action_show_my_dialog)
        action_show_my_dialog.triggered.connect(self.show_my_dialog)

        tray_menu.addMenu(menu)

    # Add CLI
    def cli(self, click_group):
        click_group.add_command(cli_main.to_click_obj())


@click_wrap.group(
    MyStudioAddon.name,
    help="MyStudio Addon related commands.")
def cli_main():
    print("<<<< MyStudioAddon CLI >>>>")


@cli_main.command()
def welcome_cli():
    print("Welcome to MyStudioAddon command line interface!")
    print("This is an example of supporting command lines.")


@cli_main.command()
@click_wrap.option(
    "--word",
    help="A word to be repeated.",
    type=str,
    required=False
)
def echo(word):
    print("Echo Echo,", word, "!")
