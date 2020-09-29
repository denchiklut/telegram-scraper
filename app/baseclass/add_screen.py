from kivy.uix.screenmanager import Screen
from kivymd.theming import ThemableBehavior

from libs.baseclass.list_items import AppTwoLineLeftIconItem


class AddScreen(ThemableBehavior, Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.groups_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.selected = 3

        for group in self.groups_data:
            self.ids.group_list.add_widget(
                AppTwoLineLeftIconItem(
                    text=str(group) + ' User name',
                    icon='settings',
                    secondary_text='Face',
                    on_release=lambda widget=self, _group=group: self.set_active_group(widget, _group)
                )
            )

    def set_active_group(self, widget, group):
        self.selected = group
        for child in self.ids.group_list.children:
            child.bg_color = [0, 0, 0, 0]

        widget.bg_color = [0, 0, 0, 0.3]

