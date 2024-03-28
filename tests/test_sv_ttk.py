import tkinter
from tkinter import ttk

import pytest
import nativesvttk


def test_set_theme():
    nativesvttk.set_theme("dark")
    assert nativesvttk.get_theme() == "dark"

    nativesvttk.set_theme("light")
    assert nativesvttk.get_theme() == "light"


def test_set_theme_using_ttk_dot_style_dot_theme_use():
    # theme is already loaded for the default root
    ttk.Style().theme_use("sun-valley-dark")
    assert nativesvttk.get_theme() == "dark"

    nativesvttk.set_theme("light")
    assert ttk.Style().theme_use() == "sun-valley-light"


def test_use_xxx_theme():
    nativesvttk.use_dark_theme()
    assert nativesvttk.get_theme() == "dark"

    nativesvttk.use_light_theme()
    assert nativesvttk.get_theme() == "light"


def test_toggle_theme():
    nativesvttk.set_theme("dark")
    assert nativesvttk.get_theme() == "dark"

    nativesvttk.toggle_theme()
    assert nativesvttk.get_theme() == "light"


def test_no_default_root():
    tkinter.NoDefaultRoot()
    with pytest.raises(RuntimeError):
        nativesvttk.get_theme()


def test_explicit_root():
    root = tkinter.Tk()
    assert nativesvttk.get_theme(root=root) == ttk.Style(root).theme_use()

    nativesvttk.set_theme("dark", root=root)
    assert nativesvttk.get_theme(root=root) == "dark"
