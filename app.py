from kivy.app import App
from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, SlideTransition
from kivy.utils import get_color_from_hex

import src.components.groups_rv
import src.screens.add_screen
import src.screens.parse_screen
import src.screens.settings_screen


class MainApp(App):
    def navigate_to_settings(self):
        screen_manager: ScreenManager = self.root.ids['screen_manager']
        screen_manager.transition = SlideTransition(direction='left')
        screen_manager.current = 'settings_screen'

    def navigate_to_add(self):
        screen_manager: ScreenManager = self.root.ids['screen_manager']
        screen_manager.transition = SlideTransition(direction='left')
        screen_manager.current = 'add_screen'

    def navigate_to_home(self):
        screen_manager: ScreenManager = self.root.ids['screen_manager']
        screen_manager.transition = SlideTransition(direction='right')
        screen_manager.current = 'parse_screen'


if __name__ == '__main__':
    Window.clearColor = get_color_from_hex('#101216')
    LabelBase.register(
        name='Roboto',
        fn_regular='src/assets/fonts/Roboto-Thin.ttf',
        fn_bold='src/assets/fonts/Roboto-Medium.ttf'
    )
    MainApp().run()
