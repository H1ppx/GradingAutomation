from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

Builder.load_string("""
<MenuScreen>:
    BoxLayout:
        Button:
            text: 'Go to settings'
            on_press: root.manager.current = 'settings'
        Button:
            text: 'Quit'

<SettingsScreen>:
    BoxLayout:
        Button:
            text: ''
        Button:
            text: 'Back to menu'
            on_press: root.manager.current = 'menu'
            
<CreateScreen>:
    BoxLayout:
        Button:
            text: 'Go to Menu'
            on_press: root.manager.current = 'menu'
""")

# Declare both screens
class MenuScreen(Screen):
    pass

class SettingsScreen(Screen):
    pass

class Create(Screen):
    pass

sm = ScreenManager()
sm.add_widget(MenuScreen(name='Main Menu'))
sm.add_widget(SettingsScreen(name='Settings'))



class GradingAutomationWidget(Widget):
    pass

class GradingAutomationApp(App):
    def build(self):
        return sm


if __name__ == '__main__':
    GradingAutomationApp().run()

