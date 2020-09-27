from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen

from kivymd.theming import ThemableBehavior


class SettingsScreen(ThemableBehavior, Screen):
    title = StringProperty()
