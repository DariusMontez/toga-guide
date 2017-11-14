# THE TOGA GUIDE

## Chapter One: Getting Started

Welcome to the Toga guide! Although Toga is designed to work on many platforms, we suggest learning on one with a keyboard!

> *__Note:__ the examples in this document have been tested on Ubuntu 16.04*

### Installing toga

Toga can be installed with `pip`.

`pip install toga`

> *__Note:__ Toga requires Python 3.4+*

Toga is ready to use!

### A Minimal Application

If you've installed toga with success, you can now make applications Toga. Toga apps can be very simple! Let's start with the `minimal` example:

*__example:__ `minimal`*
```python
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

# tell the app to run!
app.main_loop()
```

#### Using the Example Apps

Thoughout this guide, a good many examples are provided to create a hands-on learning experience. To use the examples, follow these steps:

1. In a terminal, move into the example app's directory. For the minimalist example app, that would be `cd examples/minimal`
2. Inside will be another directory, which is the package (also named `minimal`, in this case)
3. Run the example with python's `-m` flag: `python -m minimal`

All together, that is:

```
cd examples/minimal
python -m minimal
```

Hopefully, you will see something like this:

![Screenshot: `mininal` example](images/screenshot-example-minimal.png)

Now on to greater things!

### The `startup` Function
In the `minimal` example, we defined a simple function called `starup` and gave it to `toga.App` as a keyword argument. The function will be used as the entry point for the app, and it should return the top-level widget or container of your app's user interface. In the case of the example, `startup` returns a `toga.Label` (which, as you might have guessed, is a widget that displays text).

> *__Note:__ The `startup` function must only return one widget*

As your app grows, your `startup` function will too. We will examine different approaches to writing `startup` functions in [Chapter Two](#chapter-two-application-ui-layout).

### Subclassing toga.App

An alternative to the script-like file structure used in the `minimal` example is to create a class which inherits from `toga.App`. This allows access to more features and control of the app, such as setting the initial window size (on desktop platforms).

## Chapter Two: Application UI Layout

In [Chapter One](#chapter-one-getting-started), we breifly touched on `startup` functions. In this chapter, we will expand on this topic and examine several approaches to laying out an application's UI.

### Imparative Approach

In this approach, every widget is created and stored as a variable so that container widgets can `add()` their children.

### Declarative Approach

This time, widgets and containers are provided as arguments to a top-level, so that the hierarchy is constructed at once. This approach makes use of various container constructor arguments like `children=[...]` or `content=...`. Widgets that need to be kept track of are attached to `self` in the `startup` function.

*__example:__ `declarative_layout`*
```python
import toga
from colosseum import CSS

# Note that the indent has been reduced from 4 to 2 spaces -- this layout style
# has a tendency to "move to the right"

class DeclarativeLayoutApp(toga.App):
    
  def startup(self):
      # self.name stores the app name, the first parameter of __init__
    self.main_window = toga.MainWindow(self.name, size=(300, 150))
    self.main_window.app = self
    
    # widgets that need reference are attached to self before being inserted
    # into the hierarchy
    
    self.table = toga.Table(headings=["Items"])
    self.newRowInput = toga.TextInput(placeholder="Row content")
    self.infoLabel = toga.Label("Click a table row to see more info")
      
    self.main_window.content = toga.Box(
      style=CSS(flex_direction="row"),
      children=[
              
        # left container
        toga.Box(
          style=CSS(padding=24),
          children=[
                
            self.table
                    
          ]
        ),
              
        # right container
        toga.Box(
          style=CSS(padding=24),
          children=[
                
            toga.Box(
              style=CSS(flex_direction="row"),
              children=[
                
                self.newRowInput,
                toga.Button("Add Row", self.add_row)
                      
              ]
            ),
            
            toga.Button("Remove Row", self.remove_row),
            
            self.infoLabel
          ]
        ),
        
      ]
    )

    self.main_window.show()
    
  def on_table_select(self, table, row):
    self.infoLabel.text = table.data.rows[row]
    
  def add_row(self):
    self.table.data.insert(0, ["a new row"])
    
  def remove_row(self):
    self.table.data.remove(self.table.data.rows[0])

def main():
  return DeclarativeLayoutApp('Declarative Layout', 'org.pybee.guide.template')
```
