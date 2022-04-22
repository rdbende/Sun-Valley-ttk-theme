# Sun-Valley-ttk-theme
A stunning theme for ttk based on Microsoft's Sun Valley visual style

![Screenshot](https://github.com/rdbende/Sun-Valley-ttk-theme/blob/master/Screenshot.png)

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
I wanted to make usage of the theme very simple, so the theme setting is handled by a separate tcl script.
This way whether you want to use a dark or light theme, you need to import just a single file. The other thing
that makes this a good solution is that normally switching between light and dark theme is not entirely perfect,
and the colors are incorrect.
```tcl
# Just simply import the sun-valley.tcl file
source sun-valley.tcl

# Then set the theme you want with the set_theme procedure
set_theme light
# or
set_theme dark
```

### Switching themes
Normally changing between themes isn't that easy, because then the colors aren't correct. See this [Stackoverflow question](https://stackoverflow.com/questions/66576662/how-to-switch-between-dark-and-light-ttk-theme). However, with my current solution, you can change theme at any time, without any color issues.

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
- Tk isn't really good at displaying `png` images, so if your program is laggy with the theme, please check out the [gif-based branch!](https://github.com/rdbende/Sun-Valley-ttk-theme/tree/gif-based/)
- When you change the theme, and your app has a `treeview`, the window resizes. This is a quite strange bug that applies to all ttk themes. 

## Examples
I made a separate repo for the examples: [Sun-Valley-ttk-examples](https://github.com/rdbende/Sun-Valley-ttk-examples). 
Be sure to **star** and **watch** it because I will make more examples, with awesome tips and tricks!!

## What's next?
Check out my other themes!
- [Azure ttk theme](https://github.com/rdbende/Azure-ttk-theme)
- [Forest ttk theme](https://github.com/rdbende/Forest-ttk-theme)
