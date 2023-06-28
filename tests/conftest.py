import tkinter

import pytest
import sv_ttk


@pytest.fixture()
def root():
    sv_ttk.SunValleyTtkTheme.initialized = False
    root = tkinter.Tk()
    yield root
    try:
        default_root = sv_ttk.get_default_root()
        if default_root:
            default_root.destroy()
    except RuntimeError:
        pass
