from kivy.uix.modalview import ModalView

from kivymd.theming import ThemableBehavior
from kivymd.uix.picker import MDThemePicker


class AppBaseDialog(ThemableBehavior, ModalView):
    pass


class AppDialogChangeTheme(MDThemePicker):
    pass
