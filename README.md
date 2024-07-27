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
Our intention is to keep the `sv-ttk` package as simple as possible, while making it easy to integrate with other libraries.

<details>
  <summary><b>Set the theme to the system theme</b></summary>
  
  You can use [darkdetect](https://github.com/albertosottile/darkdetect) for that. Here's an example:
  
  ```python
  import darkdetect

  sv_ttk.set_theme(darkdetect.theme())
  ```

  It's only a matter of an extra import and passing the result of `darkdetect.theme()` to ```sv_ttk.set_theme()`. It's that easy!
</details>


<details>
  <summary><b>Dark Mode title bar on Windows</b></summary>

  By default, sv_ttk doesn't change the title bar color on Windows when the theme is set to dark. But you can use [pywinstyles](https://github.com/Akascape/py-window-styles) to change the title bar color on Windows. Here's an example:
  
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

          if version.major == 10 and version.build >= 22000: return 11 # Windows 11
          elif version.major == 10: return 10 # Windows 10
          else: return version.major # Other Windows version (like 7, 8, 8.1, etc...)
      else: return 0 # Not running on Windows
        
  root = tkinter.Tk()

  button = ttk.Button(root, text="Click me!", style="Accent.TButton")
  button.pack()

  sv_ttk.set_theme("dark")
  set_title_bar_color(root)
  root.mainloop()
```

  Note that on Windows 10, due to its limitations, you can only set the title bar's color to black for dark mode and white for light mode. On Windows 11 the title bar can be set to any color.

  Here's how the windows look after calling ```set_title_bar_color()```:

  <p align="center">
    <b>Windows 10</b>
    <br>
    <img src="assets/win10.png"/>
    <br><br>
    <b>Windows 11</b>
    <br>
    <img src="assets/win11.png"/>
  </p>
</details>

## Wanna see more?
Check out my other ttk themes!
- The [Azure ttk theme](https://github.com/rdbende/Azure-ttk-theme)
- The [Forest ttk theme](https://github.com/rdbende/Forest-ttk-theme)
