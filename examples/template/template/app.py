import toga
from colosseum import CSS


class TemplateApp(toga.App):
    
    def startup(self):
        # self.name stores the app name, the first parameter of __init__
        self.main_window = toga.MainWindow(self.name, size=(300, 150))
        self.main_window.app = self

        self.main_window.show()

def main():
    app = TemplateApp('Template', 'org.pybee.guide.template')
    return app
