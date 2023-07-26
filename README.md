<div align="center">

<h1>Sun Valley ttk theme</h1>
Make you Tkinter application look like never before!

[![PyPi downloads badge](https://static.pepy.tech/badge/sv-ttk)](https://pypi.org/project/sv-ttk)
[![Documentation](https://img.shields.io/badge/-documentation-%2398b427)](https://github.com/rdbende/Sun-Valley-ttk-theme/wiki/Usage-with-Python)

</div>


![Screenshot of Sun Valley ttk theme](assets/screenshot.png)


## Installation 
The theme is easily installable as a Python package

```
pip install sv-ttk
```


### Usage
> ❕**Note:**
> The theme will only work with themable (`tkinter.ttk`) widgets, and not with the regular Tkinter widgets, they only get the colorscheme.
Please don't open issues about the theme not working with plain Tkinter widgets.

For detailed documentation, see the [wiki page](https://github.com/rdbende/Sun-Valley-ttk-theme/wiki/Usage-with-Python).

```python
import tkinter
from tkinter import ttk

import sv_ttk

root = tkinter.Tk()

button = ttk.Button(root, text="Click me!")
button.pack()

# This is where the magic happens
sv_ttk.set_theme("dark")

root.mainloop()
```


## Wanna see more?
Check out my other ttk themes!
- The [Azure ttk theme](https://github.com/rdbende/Azure-ttk-theme)
- The [Forest ttk theme](https://github.com/rdbende/Forest-ttk-theme)
