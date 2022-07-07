<h1 align="center">Sun Valley ttk theme</h1>

</br>

<p align="center">A stunning theme for ttk based on Microsoft's Sun Valley visual styles</p>

![Screenshot](https://raw.githubusercontent.com/rdbende/Sun-Valley-ttk-theme/master/Screenshot.png)

## Installation
The theme is easily installable as a Python package

```
pip install sv-ttk
```


### Usage

```python
import tkinter as tk
import sv_ttk

root = tk.Tk()

sv_ttk.set_theme("light")  # Set light theme
sv_ttk.set_theme("dark")  # Set dark theme

sv_ttk.use_light_theme()  # Set light theme
sv_ttk.use_dark_theme()  # Set dark theme

sv_ttk.toggle_theme()  # Toggle between dark and light theme

print(sv_ttk.get_theme())  # Get what theme the app uses (either 'light' or 'dark')

root.mainloop()
```

## Usage with Tcl/Tk
To make setting the theme and the right colours as easy as possible, there is a separate script that handles all this.
This way whether you want to use a dark or light theme, you need to import just a single file, and the colors will be
configured even for non-ttk widgets for a consistent look.

```tcl
source sun-valley.tcl

set_theme light  ;# Set light theme
# or
set_theme dark  ;# Set dark theme
```

### Switching themes
Normally changing between themes isn't that easy, because then the colors doesn't get configured correctly. See this [SO question](https://stackoverflow.com/questions/66576662/how-to-switch-between-dark-and-light-ttk-theme).
However, with my current solution, you can change theme at any time, without any color issues.

```tcl
package require Tk 8.6
source "sun-valley.tcl"

set_theme light

# Pack a big frame so, it behaves like the window background
ttk::frame .big_frame
pack .big_frame -fill both -expand 1

proc changeTheme {} {
    # NOTE: The theme's real name is sun-valley-<mode>
    if {[ttk::style theme use] == "sun-valley-dark"} {
        # Set light theme
        set_theme light
    } else {
        # Set dark theme
        set_theme dark
    }
}

ttk::button .big_frame.button -text "Change theme!" -command changeTheme
pack .big_frame.button
```

## Bugs
- Tk isn't really good at displaying `png` images, so if your program is laggy with the theme, please check out the [gif-based branch!](https://github.com/rdbende/Sun-Valley-ttk-theme/tree/gif-based/) (hasn't been updated for a while)
- When you change the theme, and your app has a `treeview`, the window resizes. This is a quite strange bug that applies to other ttk themes too. 

## Examples
I made a separate repo for the examples: [Sun-Valley-ttk-examples](https://github.com/rdbende/Sun-Valley-ttk-examples). 
Be sure to **star** and **watch** it because I might make some more examples, with awesome tips and tricks!

## What's next?
Check out my other ttk themes!
- [Azure ttk theme](https://github.com/rdbende/Azure-ttk-theme)
- [Forest ttk theme](https://github.com/rdbende/Forest-ttk-theme)
