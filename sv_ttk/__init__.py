from __future__ import annotations

import tkinter
from functools import partial
from pathlib import Path
from tkinter import ttk
import sys

TCL_THEME_FILE_PATH = Path(__file__).with_name("sv.tcl").absolute()


# A hacky way to change a Toplevel's title bar color after it's created
class ThemedToplevel(tkinter.Toplevel):
    def __init__(self, master=None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        try: set_theme(get_theme())
        except: pass

tkinter.Toplevel = ThemedToplevel


def _load_theme(style: ttk.Style) -> None:
    if not isinstance(style.master, tkinter.Tk):
        raise TypeError("root must be a `tkinter.Tk` instance!")

    if not hasattr(style.master, "_sv_ttk_loaded"):
        style.tk.call("source", str(TCL_THEME_FILE_PATH))
        style.master._sv_ttk_loaded = True  # type: ignore


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

    # Set title bar color on Windows
    def set_title_bar_color(root):
        if get_windows_version() == 10:
            import pywinstyles

            if theme == "dark": pywinstyles.apply_style(root, "dark")
            else: pywinstyles.apply_style(root, "normal")

            # A hacky way to update the title bar's color on Windows 10 (it doesn't update instantly like on Windows 11)
            root.wm_attributes("-alpha", 0.99)
            root.wm_attributes("-alpha", 1)
        elif get_windows_version() == 11:
            import pywinstyles
            
            if theme == "dark": pywinstyles.change_header_color(root, "#1c1c1c")
            elif theme == "light": pywinstyles.change_header_color(root, "#fafafa")

    def set_title_bar_color_toplevels():
        for widget in style.master.winfo_children():
            if isinstance(widget, tkinter.Toplevel): set_title_bar_color(widget)

    set_title_bar_color(style.master)
    set_title_bar_color_toplevels()

    style.theme_use(f"sun-valley-{theme}")


def toggle_theme(root: tkinter.Tk | None = None) -> None:
    style = ttk.Style(master=root)
    _load_theme(style)

    set_theme("light" if style.theme_use() == "sun-valley-dark" else "dark")


def get_windows_version() -> int:
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

use_dark_theme = partial(set_theme, "dark")
use_light_theme = partial(set_theme, "light")
