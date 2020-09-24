import os

from kivy.animation import Animation
from kivy.clock import Clock
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen

from src.components.file_picker_modal import LoadDialog


class AddScreen(Screen):
    ext_input = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_interval(self.animate, 1)

    def animate(self, dt):
        bar = self.ids['CircularProgressBar']
        if bar.value < bar.max:
            bar.value += 1
        else:
            bar.value = bar.min

        # Showcase that setting the values using value_normalized property also works
        bar = self.ids['CircularProgressBar']
        if bar.value < bar.max:
            bar.value_normalized += 0.01
        else:
            bar.value_normalized = 0

    def show_load(self):
        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self._popup = Popup(title="Выберите файл", content=content, size_hint=(0.9, 0.9))
        self._popup.open()

    def dismiss_popup(self):
        self._popup.dismiss()

    def load(self, path, filename):
        with open(os.path.join(path, filename[0])) as stream:
            self.text_input.text = stream.read()

        self.dismiss_popup()

    def save(self, path, filename):
        with open(os.path.join(path, filename), 'w') as stream:
            stream.write(self.text_input.text)

        self.dismiss_popup()

    def animate_rotate(self, widget, *args):
        anim = Animation(angle=180)
        anim.bind(on_complete=self.reset)
        anim.start(widget)

    def reset(self, *args):
        widget = args[1]
        widget.angle = 0