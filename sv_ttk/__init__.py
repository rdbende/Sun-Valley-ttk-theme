from __future__ import annotations

import tkinter
from functools import partial
from pathlib import Path
from tkinter import ttk

TCL_THEME_FILE_PATH = Path(__file__).with_name("sv.tcl").absolute()


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

    style.theme_use(f"sun-valley-{theme}")


def toggle_theme(root: tkinter.Tk | None = None) -> None:
    style = ttk.Style(master=root)
    _load_theme(style)

    set_theme("light" if style.theme_use() == "sun-valley-dark" else "dark")


use_dark_theme = partial(set_theme, "dark")
use_light_theme = partial(set_theme, "light")
