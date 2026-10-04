import os
import tkinter as tk

import pytest

SCREEN_WIDTH = tk.Tk().winfo_screenwidth() if os.getenv("DISPLAY") is not None else 1920
SCREEN_HEIGHT = (
    tk.Tk().winfo_screenheight() if os.getenv("DISPLAY") is not None else 1080
)


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "viewport": {
            "width": SCREEN_WIDTH,
            "height": SCREEN_HEIGHT,
        },
    }
