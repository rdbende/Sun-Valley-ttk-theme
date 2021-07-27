# Sun-Valley-ttk-theme
A stunning theme for ttk based on Microsoft's Sun Valley visual style

![Light screenshot](https://github.com/rdbende/Sun-Valley-ttk-theme/blob/master/Light%20screenshot.png)
![Dark screenshot](https://github.com/rdbende/Sun-Valley-ttk-theme/blob/master/Dark%20screenshot.png)
###### Yup, this isn't Windows 11, this is KDE Plasma :)

<br>

## Documentation
For the documentation see the [documentation](DOCUMENTATION.pdf)!

## How to use?
I wanted to make usage of the theme very simple, so the theme setting is handled by a separate tcl script.
This way whether you want to use a dark or light theme, you need to import just a single file. The other thing
that makes this a good solution is that normally switching between light and dark theme is not entirely perfect,
and the colors are incorrect.

```python
# Just simply import the sun_valley.tcl file
widget.tk.call("source", "sun_valley.tcl")

# Then set the theme you want with the set_theme procedure
widget.tk.call("set_theme", "light")
# or
widget.tk.call("set_theme", "dark")
```

### Changing themes
Normally changing between themes isn't that easy, because then the colors aren't correct. See this [Stackoverflow question](https://stackoverflow.com/questions/66576662/how-to-switch-between-dark-and-light-ttk-theme). However, with my current solution, you can change theme at any time, without any color issues.

```python
import tkinter as tk
from tkinter import ttk

root = tk.Tk()

# Pack a big frame so, it behaves like the window background
big_frame = ttk.Frame(root)
big_frame.pack(fill="both", expand=True)

# Set the initial theme
root.tk.call("source", "sun-valley.tcl")
root.tk.call("set_theme", "light")

def change_theme():
    # NOTE: The theme's real name is sun-valley-mode
    if root.tk.call("ttk::style", "theme", "use") == "sun-valley-dark":
        # Set light theme
        root.tk.call("set_theme", "light")
    else:
        # Set light theme
        root.tk.call("set_theme", "dark")

# Remember, you have to use ttk widgets
button = ttk.Button(big_frame, text="change theme!", command=change_theme)
button.pack()

root.mainloop()
```

## Bugs
Tk isn't really good at displaying `png` images, so if your program is slow due to the theme, please check out the [gif-based branch!](https://github.com/rdbende/Sun-Valley-ttk-theme/tree/gif-based/)

## Examples
I made a separate repo for the examples: [Sun-Valley-ttk-examples](https://github.com/rdbende/Sun-Valley-ttk-examples). 
Be sure to **star** and **watch** it because I will make more examples, with awesome tips and tricks!!

## What's next?
Check out my other themes!
- [Azure ttk theme](https://github.com/rdbende/Azure-ttk-theme)
- [Forest ttk theme](https://github.com/rdbende/Forest-ttk-theme)
