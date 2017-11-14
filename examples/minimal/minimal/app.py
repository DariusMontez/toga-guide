import toga

def startup(app):
  return toga.Label("Hello, World")

app = toga.App(
    # the `name` will be shown in the window frame
    name="Hello, World", 

    # the `app_id` identifies the application
    app_id="hello_world",
    
    # a function that returns the app's topmost widget
    # (explained in the guide)
    startup=startup
)

# tell the 
app.main_loop()
