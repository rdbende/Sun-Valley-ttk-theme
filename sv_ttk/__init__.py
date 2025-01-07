from __future__ import annotations

import tkinter
from re import sub
from functools import partial
from pathlib import Path
from tkinter import ttk

TCL_THEME_FILE_PATH = Path(__file__).with_name("sv.tcl").absolute()

# Default font list
_prefer_fonts = [
    "微軟正黑體",
    "Microsoft JhengHei UI",
    "蘋方-繁",
    "Noto Sans CJK TC",
    "Segoe UI"
]

# Replace whole string's non-ascii charters to unicode encoding
def _unicode_replacement(input_text: str):
    result = ""
    for char in input_text:
        if ord(char) > 127:  # Check if the character has an ordinal value greater than 127 (ASCII range)
            result += r'\u{:04X}'.format(ord(char))  # Format the Unicode escape sequence
        else:
            result += char
    return result

# Replace whole string's non-ascii charters to unicode encoding
def _replace_fallback(style: ttk.Style):
    # Convert the Python list of preferred fonts to Tcl list format
    tcl_preferred_fonts = '{'
    for font in _prefer_fonts:
        tcl_preferred_fonts += (' \"' + _unicode_replacement(font) + "\"")
    tcl_preferred_fonts += '}'
    #print(f"Debug: font list of tcl is: {tcl_preferred_fonts}")
    # Update the `preferred_fonts` variable in Tcl
    # And execute the rest of the script to load theme
    style.tk.eval(
        f'''
        set preferred_fonts {tcl_preferred_fonts}
        start_config_theme $preferred_fonts
        ''')

def _load_theme(style: ttk.Style) -> None:
    if not isinstance(style.master, tkinter.Tk):
        raise TypeError("root must be a `tkinter.Tk` instance!")

    if not hasattr(style.master, "_sv_ttk_loaded"):
        style.tk.call("source", str(TCL_THEME_FILE_PATH))
        # Load font and rest of the style
        _replace_fallback(style)
        style.master._sv_ttk_loaded = True  # type: ignore

# Function to let user can apply the custom fallback list
def load_fallback_list(fallback_list: list):
    global _prefer_fonts
    # List not empty, setup the variable
    if fallback_list:
        _prefer_fonts = fallback_list

def get_theme(root: tkinter.Tk | None = None) -> str:
    style = ttk.Style(master=root)
    _load_theme(style)

    theme = style.theme_use()
    return {"sun-valley-dark": "dark", "sun-valley-light": "light"}.get(theme, theme)


def set_theme(theme: str, root: tkinter.Tk | None = None) -> None:
    style = ttk.Style(master=root)
    _load_theme(style)

    theme = theme.lower()

    if theme not in {"dark", "light"}:
        raise RuntimeError(f"not a valid sv_ttk theme: {theme}")

    style.theme_use(f"sun-valley-{theme}")


def toggle_theme(root: tkinter.Tk | None = None) -> None:
    style = ttk.Style(master=root)
    _load_theme(style)

    set_theme("light" if style.theme_use() == "sun-valley-dark" else "dark")


use_dark_theme = partial(set_theme, "dark")
use_light_theme = partial(set_theme, "light")
