from kivy.properties import ListProperty, StringProperty, BooleanProperty
from kivy.uix.widget import Widget

from kivymd.uix.list import (
    ILeftBody,
    IRightBodyTouch,
    OneLineAvatarListItem,
    OneLineIconListItem,
    TwoLineAvatarListItem,
)
from kivymd.uix.selectioncontrol import MDCheckbox


class AppOneLineLeftAvatarItem(OneLineAvatarListItem):
    divider = None
    source = StringProperty()


class AppTwoLineLeftAvatarItem(TwoLineAvatarListItem):
    icon = StringProperty()
    secondary_font_style = "Caption"


class AppTwoLineLeftIconItem(TwoLineAvatarListItem):
    icon = StringProperty()


class AppOneLineLeftIconItem(OneLineAvatarListItem):
    icon = StringProperty()


class AppOneLineIconListItem(OneLineIconListItem):
    icon = StringProperty()


class AppOneLineLeftWidgetItem(OneLineAvatarListItem):
    color = ListProperty()


class LeftWidget(ILeftBody, Widget):
    pass


class IconRightSampleWidget(IRightBodyTouch, MDCheckbox):
    pass
