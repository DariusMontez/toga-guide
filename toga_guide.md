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

#### The `startup` Function
In the `minimal` example, we defined a simple function called `starup` and gave it to `toga.App` as a keyword argument. The function will be used as the entry point for the app, and it should return the top-level widget or container of your app's user interface. In the case of the example, `startup` returns a `toga.Label` (which, as you might have guessed, is a widget that displays text).

> *__Note:__ The `startup` function must only return one widget*

As your app grows, your `startup` function will too. We will examine different approaches to writing `startup` functions in a later section

## Chapter Two: Application UI Layout

In [Chapter One](#chapter-one-getting-started), we breifly touched on `startup` functions. In this chapter, we will expand on this topic and examine several approaches to laying out an application's UI.
