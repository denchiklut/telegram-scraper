from os.path import expanduser
from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen

from kivymd.theming import ThemableBehavior
from kivymd.toast import toast
from kivymd.uix.filemanager import MDFileManager

from libs.baseclass.list_items import AppTwoLineLeftIconItem


class ParseScreen(ThemableBehavior, Screen):
    title = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.groups_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.selected = 3
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=self.select_path,
        )

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
        self.ids.group_label.text = 'Group ' + str(group)

    def save_scv(self):
        self.file_manager.show(expanduser("~"))

    def select_path(self, path):
        self.exit_manager()
        if type(path) == str:
            toast(path)
        else:
            toast(",".join(path))

    def exit_manager(self, **args):
        self.file_manager.close()
