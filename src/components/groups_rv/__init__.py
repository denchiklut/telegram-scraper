from random import sample
from string import ascii_uppercase

from kivy.uix.recycleview import RecycleView
from kivy.properties import BooleanProperty
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.uix.recycleview.views import RecycleDataViewBehavior


class GroupsRV(RecycleView):
    def __init__(self, **kwargs):
        super(GroupsRV, self).__init__(**kwargs)
        self.populate()

    def populate(self):
        self.data = [{'id': str(x + 1), 'value': ''.join(sample(ascii_uppercase, 5))} for x in range(10)]

    def sort(self):
        self.data = sorted(self.rv.data, key=lambda x: x['value'])

    def clear(self):
        self.data = []

    def insert(self, value):
        self.data.insert(0, {'value': value or 'default value'})

    def update(self, value):
        if self.rv.data:
            self.rv.data[0]['value'] = value or 'default new value'
            self.rv.refresh_from_data()

    def remove(self):
        if self.data:
            self.data.pop(0)


class SelectableRecycleBoxLayout(FocusBehavior, LayoutSelectionBehavior, RecycleBoxLayout):
    """ Adds selection and focus behaviour to the view. """


class SelectableLabel(RecycleDataViewBehavior, BoxLayout):
    index = None
    selected = BooleanProperty(False)
    selectable = BooleanProperty(True)

    def refresh_view_attrs(self, rv, index, data):
        self.index = index
        return super(SelectableLabel, self).refresh_view_attrs(rv, index, data)

    def on_touch_down(self, touch):
        if super(SelectableLabel, self).on_touch_down(touch):
            return True
        if self.collide_point(*touch.pos) and self.selectable:
            return self.parent.select_with_touch(self.index, touch)

    def apply_selection(self, rv, index, is_selected):
        self.selected = is_selected
        if is_selected:
            print("selection changed to {0}".format(rv.data[index]))
        else:
            print("selection removed for {0}".format(rv.data[index]))