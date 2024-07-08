<div align="center">
  
# Sun Valley ttk theme
Make your Tkinter application look better than ever with just two lines of code!

![Screenshot of Sun Valley ttk theme](assets/screenshot.png)

</div>


## Installation [![PyPi downloads](https://static.pepy.tech/badge/sv-ttk)](https://pypi.org/project/sv-ttk)
The theme is easily installable as a Python package

```
pip install sv-ttk
```


## Usage [![Documentation](https://img.shields.io/badge/-documentation-%23c368c4)](https://github.com/rdbende/Sun-Valley-ttk-theme/wiki/Usage-with-Python)
> **Note:**
> 
> The theme will only be applied to themable (`tkinter.ttk`) widgets, and not with the regular Tkinter widgets, they only benefit from the colorscheme.

For detailed documentation, visit the [wiki page](https://github.com/rdbende/Sun-Valley-ttk-theme/wiki/Usage-with-Python).

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

## Tips and tricks
Sun Valley is meant to be a simple ttk theme that is wrapped in a PyPI package for convenience. I don't want to add other dependencies, nor features that would be trival to implement if the user wants it, using third party packages. But this theme can be easily integrated with other 3rd party modules.

### Set the theme to system's theme
You can use [darkdetect](https://github.com/albertosottile/darkdetect) for that. Here's how you can do this:

<details>
  <summary>Show code</summary>
  
  ```python
  import tkinter, sv_ttk, darkdetect
  from tkinter import ttk

  root = tkinter.Tk()

  button = ttk.Button(root, text="Click me!")
  button.pack()

  sv_ttk.set_theme(darkdetect.theme())
  root.mainloop()
  ```
</details>

You have just to pass ```darkdetect.theme()``` to ```sv_ttk.set_theme()``` function. It's that easy!

### Dark Mode title bar on Windows
By default, sv_ttk doesn't change the title bar color on Windows when the theme is set to dark. But you can use [pywinstyles](https://github.com/Akascape/py-window-styles) to change the title bar color on Windows. Here's how you can do this:

<details>
  <summary>Show code</summary>
  
  ```python
  import tkinter, sv_ttk
  from tkinter import ttk

  # Function to set the title bar color
  def set_title_bar_color(root: tkinter.Tk | tkinter.Toplevel):
      theme = sv_ttk.get_theme()

      if get_windows_version() == 10:
          import pywinstyles

          if theme == "dark": pywinstyles.apply_style(root, "dark")
          else: pywinstyles.apply_style(root, "normal")

          # A hacky way to update the title bar's color on Windows 10 (it doesn't update instantly like on Windows 11)
          root.wm_attributes("-alpha", 0.99)
          root.wm_attributes("-alpha", 1)
      elif get_windows_version() == 11:
          import pywinstyles

          # Set the title bar color to the background color on Windows 11 for better appearance
          if theme == "dark": pywinstyles.change_header_color(root, "#1c1c1c")
          elif theme == "light": pywinstyles.change_header_color(root, "#fafafa")


  # Function to get Windows version			
  def get_windows_version() -> int:
      import sys

      if sys.platform == "win32":
         # Running on Windows
          version = sys.getwindowsversion()

          if version.major == 10 and version.build >= 22000:
              # Windows 11
              return 11
          elif version.major == 10:
              # Windows 10
              return 10
          else:
              # Other Windows version (like 7, 8, 8.1, etc...)
              return version.major
      else:
          # Not running on Windows
          return 0
        
        
  root = tkinter.Tk()

  button = ttk.Button(root, text="Click me!")
  button.pack()

  sv_ttk.set_theme("dark")
  set_title_bar_color(root)
  root.mainloop()
```
</details>

Note that on Windows 10, due to its limitations, you can only set the title bar's color to black for dark mode and white for light mode. On Windows 11 the title bar can be set to any color.

## Wanna see more?
Check out my other ttk themes!
- The [Azure ttk theme](https://github.com/rdbende/Azure-ttk-theme)
- The [Forest ttk theme](https://github.com/rdbende/Forest-ttk-theme)
