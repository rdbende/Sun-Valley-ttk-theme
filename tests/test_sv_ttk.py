import tkinter
from tkinter import ttk

import pytest
import sv_ttk


def test_set_theme():
    sv_ttk.set_theme("dark")
    assert sv_ttk.get_theme() == "dark"

    sv_ttk.set_theme("light")
    assert sv_ttk.get_theme() == "light"


def test_set_theme_using_ttk_dot_style_dot_theme_use():
    # theme is already loaded for the default root
    ttk.Style().theme_use("sun-valley-dark")
    assert sv_ttk.get_theme() == "dark"

    sv_ttk.set_theme("light")
    assert ttk.Style().theme_use() == "sun-valley-light"


def test_use_xxx_theme():
    sv_ttk.use_dark_theme()
    assert sv_ttk.get_theme() == "dark"

    sv_ttk.use_light_theme()
    assert sv_ttk.get_theme() == "light"


def test_toggle_theme():
    sv_ttk.set_theme("dark")
    assert sv_ttk.get_theme() == "dark"

    sv_ttk.toggle_theme()
    assert sv_ttk.get_theme() == "light"


def test_no_default_root():
    tkinter.NoDefaultRoot()
    with pytest.raises(RuntimeError):
        sv_ttk.get_theme()


def test_explicit_root():
    root = tkinter.Tk()
    assert sv_ttk.get_theme(root=root) == ttk.Style(root).theme_use()

    sv_ttk.set_theme("dark", root=root)
    assert sv_ttk.get_theme(root=root) == "dark"
