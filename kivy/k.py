import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout

kivy.require("1.11.1")


class MyApp(App):

    def build(self):
        layout = GridLayout(cols=1)
        self.label = Label(text="Hello, Kivy!")
        button = Button(text="Click me!")
        button.bind(on_press=self.on_button_click)  # type: ignore
        layout.add_widget(self.label)
        layout.add_widget(button)
        return layout

    def on_button_click(self, instance):
        self.label.text = "Button Clicked!"


if __name__ == "__main__":
    MyApp().run()
