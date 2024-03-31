import sys
import tkinter as tk
from functools import partial
from tkinter import ttk


def popup(parent, title, details, icon, *, buttons, aboveparent, wait):
    dialog = tk.Toplevel()

    result = None

    big_frame = ttk.Frame(dialog)
    big_frame.pack(fill="both", expand=True)
    big_frame.columnconfigure(0, weight=1)
    big_frame.rowconfigure(0, weight=1)

    info_frame = ttk.Frame(big_frame, padding=(10, 12), style="Dialog_info.TFrame")
    info_frame.grid(row=0, column=0, sticky="nsew")
    info_frame.columnconfigure(1, weight=1)
    info_frame.rowconfigure(1, weight=1)

    try:
        color = big_frame.tk.call("set", "themeColors::dialogInfoBg")
    except tk.TclError:
        color = big_frame.tk.call("ttk::style", "lookup", "TFrame", "-background")

    icon_label = ttk.Label(info_frame, image=icon, anchor="nw", background=color)
    if icon is not None:
        icon_label.grid(
            row=0, column=0, sticky="nsew", padx=(12, 0), pady=10, rowspan=2
        )

    title_label = ttk.Label(
        info_frame, text=title, anchor="nw", font=("", 14, "bold"), background=color
    )
    title_label.grid(row=0, column=1, sticky="nsew", padx=(12, 17), pady=(10, 8))

    detail_label = ttk.Label(info_frame, text=details, anchor="nw", background=color)
    detail_label.grid(row=1, column=1, sticky="nsew", padx=(12, 17), pady=(5, 10))

    button_frame = ttk.Frame(
        big_frame, padding=(22, 22, 12, 22), style="Dialog_buttons.TFrame"
    )
    button_frame.grid(row=2, column=0, sticky="nsew")

    def on_button(value):
        nonlocal result
        result = value
        dialog.destroy()

    for index, button_value in enumerate(buttons):
        style = None
        state = None
        default = False
        sticky = "nes" if len(buttons) == 1 else "nsew"

        if len(button_value) > 2:
            if button_value[2] == "accent":
                style = "Accent.TButton"
                default = True
            elif button_value[2] == "disabled":
                state = "disabled"
            elif button_value[2] == "default":
                default = True

        button = ttk.Button(
            button_frame,
            text=button_value[0],
            width=18,
            command=partial(on_button, button_value[1]),
            style=style,
            state=state,
        )
        if default:
            button.bind("<Return>", button["command"])
            button.focus()

        button.grid(row=0, column=index, sticky=sticky, padx=(0, 10))

        button_frame.columnconfigure(index, weight=1)

    dialog.overrideredirect(True)
    dialog.update_idletasks()

    dialog_width = dialog.winfo_width()
    dialog_height = dialog.winfo_height()

    if parent is None:
        parent_width = dialog.winfo_screenwidth()
        parent_height = dialog.winfo_screenheight()
        parent_x = 0
        parent_y = 0
    else:
        parent_width = parent.winfo_width()
        parent_height = parent.winfo_height()
        parent_x = parent.winfo_x()
        parent_y = parent.winfo_y()

    x_coord = int(parent_width / 2 + parent_x - dialog_width / 2)
    y_coord = int(parent_height / 2 + parent_y - dialog_height / 2)

    dialog.geometry("+{}+{}".format(x_coord, y_coord))
    dialog.minsize(320, dialog_height)

    dialog.transient(parent)
    if sys.platform == "win32": # If windows then transparentcolor
        transparent_color = big_frame.tk.call(
            "ttk::style", "lookup", "TFrame", "-background"
        )
        dialog.wm_attributes("-transparentcolor", transparent_color)
    else: # Doesn't work on windows
        dialog.wm_attributes("-type", "dialog")

    if aboveparent:
        dialog.grab_set()
    if wait:
        dialog.wait_window()
    return result


def show_message(
    title="Title",
    details="Description",
    *,
    parent=None,
    icon=None,
    aboveparent=True,
    wait=True
):
    return popup(
        parent,
        title,
        details,
        icon,
        buttons=[("Ok", None, "default")],
        aboveparent=aboveparent,
        wait=wait,
    )


def ask_ok_cancel(
    title="Title",
    details="Description",
    *,
    parent=None,
    icon=None,
    aboveparent=True,
    wait=True
):
    return popup(
        parent,
        title,
        details,
        icon,
        buttons=[("Ok", True, "accent"), ("Cancel", None)],
        aboveparent=aboveparent,
        wait=wait,
    )


def ask_yes_no(
    title="Title",
    details="Description",
    *,
    parent=None,
    icon=None,
    aboveparent=True,
    wait=True
):
    return popup(
        parent,
        title,
        details,
        icon,
        buttons=[("Yes", True, "accent"), ("No", False)],
        aboveparent=aboveparent,
        wait=wait,
    )


def ask_yes_no_cancel(
    title="Title",
    details="Description",
    *,
    parent=None,
    icon=None,
    aboveparent=True,
    wait=True
):
    return popup(
        parent,
        title,
        details,
        icon,
        buttons=[("Yes", True, "accent"), ("No", False), ("Cancel", None)],
        aboveparent=aboveparent,
        wait=wait,
    )


def ask_retry_cancel(
    title="Title",
    details="Description",
    *,
    parent=None,
    icon=None,
    aboveparent=True,
    wait=True
):
    return popup(
        parent,
        title,
        details,
        icon,
        buttons=[("Retry", True, "accent"), ("Cancel", None)],
        aboveparent=aboveparent,
        wait=wait,
    )


def ask_allow_block(
    title="Title",
    details="Description",
    *,
    parent=None,
    icon=None,
    aboveparent=True,
    wait=True
):
    return popup(
        parent,
        title,
        details,
        icon,
        buttons=[("Allow", True, "accent"), ("Block", False)],
        aboveparent=aboveparent,
        wait=wait,
    )


