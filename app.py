from kivy.app import App
from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.uix.button import ButtonBehavior
from kivy.uix.image import Image
from kivy.utils import get_color_from_hex


class ImageButton(ButtonBehavior, Image):
    pass


class HomeScreen(Screen):
    pass


class SettingsScreen(Screen):
    pass


class MainApp(App):
    def navigate_to_settings(self):
        screen_manager: ScreenManager = self.root.ids['screen_manager']
        screen_manager.transition = SlideTransition(direction='left')
        screen_manager.current = 'settings_screen'

    def navigate_to_home(self):
        screen_manager: ScreenManager = self.root.ids['screen_manager']
        screen_manager.transition = SlideTransition(direction='right')
        screen_manager.current = 'home_screen'


if __name__ == '__main__':
    Window.clearColor = get_color_from_hex('#101216')
    LabelBase.register(
        name='Roboto',
        fn_regular='assets/fonts/Roboto-Thin.ttf',
        fn_bold='assets/fonts/Roboto-Medium.ttf'
    )
    MainApp().run()