import ast
import os
import sys

from kivy.core.window import Window
from kivy.lang import Builder
from kivy.loader import Loader

from kivymd import images_path
from kivymd.app import MDApp
from libs.baseclass.dialog import AppDialogChangeTheme

from libs.baseclass.list_items import (  # NOQA: F401
    AppOneLineLeftIconItem,
)

os.environ["KIVY_PROFILE_LANG"] = "1"

if getattr(sys, "frozen", False):  # bundle mode with PyInstaller
    os.environ["APP_ROOT"] = sys._MEIPASS
else:
    sys.path.append(os.path.abspath(__file__).split("app")[0])
    os.environ["APP_ROOT"] = os.path.dirname(os.path.abspath(__file__))
    os.environ["APP_ASSETS"] = os.path.join(os.environ["APP_ROOT"], f"assets{os.sep}")
Window.softinput_mode = "below_target"


class App(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.theme_cls.primary_palette = "Pink"
        self.toolbar = None
        self.data_screens = {}
        Loader.loading_image = f"{images_path}transparent.png"

    def build(self):
        Builder.load_file(
            f"{os.environ['APP_ROOT']}/libs/kv/list_items.kv"
        )
        return Builder.load_file(
            f"{os.environ['APP_ROOT']}/libs/kv/navigation_drawer.kv"
        )

    def on_start(self):
        with open(
                f"{os.environ['APP_ROOT']}/screens_data.json"
        ) as read_file:
            self.data_screens = ast.literal_eval(read_file.read())
            data_screens = list(self.data_screens.keys())
            data_screens.sort()

            for screen in data_screens:
                self.root.ids.content_drawer.ids.nav_item.data.append(
                    {
                        "viewclass": "AppOneLineLeftIconItem",
                        "text": screen,
                        "icon": self.data_screens[screen]["icon"],
                        "on_release": lambda x=screen: self.set_new_screen(x),
                    }
                )

    def show_dialog_change_theme(self):
        AppDialogChangeTheme().open()

    def switch_theme_style(self):
        self.theme_cls.theme_style = (
            "Light" if self.theme_cls.theme_style == "Dark" else "Dark"
        )

    def set_new_screen(self, name_screen):
        manager = self.root.ids.screen_manager
        if not manager.has_screen(
            self.data_screens[name_screen]["name_screen"]
        ):
            name_kv_file = self.data_screens[name_screen]["kv_string"]
            Builder.load_file(
                f"{os.environ['APP_ROOT']}/kv/{name_kv_file}.kv",
            )
            if "Import" in self.data_screens[name_screen]:
                exec(self.data_screens[name_screen]["Import"])
            screen_object = eval(self.data_screens[name_screen]["Factory"])
            self.data_screens[name_screen]["object"] = screen_object
            manager.add_widget(screen_object)

        if "toolbar" in self.root.ids:
            self.root.ids.toolbar.title = self.data_screens[name_screen]['name_screen']

        manager.current = self.data_screens[name_screen]["name_screen"]

    def back_to_home_screen(self):
        self.root.ids.screen_manager.current = "home"

    def refresh_callback(self):
        pass


App().run()
