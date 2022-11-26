<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/rdbende/Sun-Valley-ttk-theme/master/assets/hero_dark.png">
  <img alt="Cover image" src="https://raw.githubusercontent.com/rdbende/Sun-Valley-ttk-theme/master/assets/hero_light.png">
</picture>

## Installation [![image](https://static.pepy.tech/badge/sv-ttk)](https://pypi.org/project/sv-ttk)
The theme is easily installable as a Python package

```
pip install sv-ttk
```


### Usage
For detailed documentation, see the [wiki page](https://github.com/rdbende/Sun-Valley-ttk-theme/wiki/Usage-with-Python)

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


## Known bugs and limitations
- Tkinter (Tk) isn't really good at displaying `png` images, so the window can be quite laggy when resizing, especially on Windows.

## What's next?
Check out my other ttk themes!
- [Azure ttk theme](https://github.com/rdbende/Azure-ttk-theme)
- [Forest ttk theme](https://github.com/rdbende/Forest-ttk-theme)
