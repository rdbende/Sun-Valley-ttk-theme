from __future__ import annotations

import sys
import tkinter
from functools import partial
from pathlib import Path


def _get_default_root() -> tkinter.Misc:
    try:
        return tkinter._get_default_root()
    except AttributeError:
        try:
            return tkinter._default_root
        except AttributeError:
            raise RuntimeError(
                "can't set theme, because tkinter is configured to not support implicit default root,"
                + " and no explicit root was provided. Use the `root` argument."
            )
    except RuntimeError as e:
        raise RuntimeError(
            "can't set theme, because tkinter is configured to not support implicit default root,"
            + " and no explicit root was provided. Use the `root` argument."
        ) from e


class SunValleyTtkTheme:
    initialized = False

    @classmethod
    def load_theme(cls, root: tkinter.Misc | None) -> None:
        if cls.initialized:
            return

        theme_file = (Path(__file__).parent / "sv.tcl").absolute()

        if root is None:
            cls.tcl = _get_default_root()
        else:
            cls.tcl = root

        cls.tcl.call("source", str(theme_file))
        cls.initialized = True

    @classmethod
    def get_theme(cls, root: tkinter.Misc | None = None) -> str:
        cls.load_theme(root)

        theme = cls.tcl.call("ttk::style", "theme", "use")
        return {"sun-valley-dark": "dark", "sun-valley-light": "light"}.get(
            theme, theme
        )

    @classmethod
    def set_theme(cls, theme: str, root: tkinter.Misc | None = None) -> None:
        cls.load_theme(root)
        if theme not in {"dark", "light"}:
            raise RuntimeError("not a valid sv_ttk theme name: {}".format(theme))

        cls.tcl.call("set_theme", theme)

    @classmethod
    def toggle_theme(cls, root: tkinter.Misc | None = None) -> None:
        cls.load_theme(root)
        if cls.get_theme() == "light":
            cls.set_theme("dark")
        else:
            cls.set_theme("light")


set_theme = SunValleyTtkTheme.set_theme
get_theme = SunValleyTtkTheme.get_theme
use_dark_theme = partial(set_theme, "dark")
use_light_theme = partial(set_theme, "light")
toggle_theme = SunValleyTtkTheme.toggle_theme
