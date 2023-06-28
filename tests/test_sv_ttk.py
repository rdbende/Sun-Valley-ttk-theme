import tkinter
from tkinter import ttk

import pytest
import sv_ttk


def test_with_explicit_root(root):
    sv_ttk.set_theme("dark", root=root)
    assert sv_ttk.SunValleyTtkTheme.tcl is root


def test_with_default_root(root):
    sv_ttk.set_theme("dark")
    assert sv_ttk.SunValleyTtkTheme.tcl is root


def test_with_no_default_root(root):
    tkinter.NoDefaultRoot()
    with pytest.raises(RuntimeError):
        sv_ttk.set_theme("dark")


def test_set_theme(root):
    sv_ttk.set_theme("dark", root=root)
    assert sv_ttk.get_theme() == "dark"

    sv_ttk.set_theme("light", root=root)
    assert sv_ttk.get_theme() == "light"


def test_use_theme(root):
    sv_ttk.use_dark_theme(root=root)
    assert sv_ttk.get_theme() == "dark"

    sv_ttk.use_light_theme(root=root)
    assert sv_ttk.get_theme() == "light"


def test_toggle_theme(root):
    sv_ttk.set_theme("dark", root=root)
    assert sv_ttk.get_theme() == "dark"

    sv_ttk.toggle_theme()
    assert sv_ttk.get_theme() == "light"
