import tkinter

import pytest
import sv_ttk


@pytest.fixture()
def root():
    sv_ttk.SunValleyTtkTheme.initialized = False
    root = tkinter.Tk()
    yield root
    try:
        sv_ttk._get_default_root().destroy()
    except (AttributeError, RuntimeError):
        pass
