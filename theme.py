"""BrewHub visual theme: black surfaces, white text, signature orange accent.

Colours live here (and in theme/brewhub_dark.json for CustomTkinter widgets).
Change ORANGE in both places to re-brand the whole app.
"""
from pathlib import Path
from tkinter import ttk
import customtkinter as ctk

THEME_FILE = Path(__file__).resolve().parent / "theme" / "brewhub_dark.json"

BLACK = "#000000"
SURFACE = "#0F0F0F"
PANEL = "#1A1A1A"
PANEL_HI = "#262626"
BORDER = "#2E2E2E"
ORANGE = "#FF9900"
ORANGE_HOVER = "#FFB340"
ORANGE_DIM = "#B36B00"
WHITE = "#FFFFFF"
MUTED = "#9B9B9B"
FONT = "Arial"


def setup():
    """Call once, before the main window is created."""
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme(str(THEME_FILE))


def style_ttk(root):
    """Dark, orange-highlighted tables and scrollbars (tkinter ttk widgets)."""
    style = ttk.Style(root)
    style.theme_use("clam")
    style.layout("Treeview", [("Treeview.treearea", {"sticky": "nswe"})])
    style.configure("Treeview", background=SURFACE, fieldbackground=SURFACE, foreground=WHITE,
                    rowheight=32, borderwidth=0, relief="flat", font=(FONT, 11))
    style.map("Treeview", background=[("selected", ORANGE)], foreground=[("selected", BLACK)])
    style.configure("Treeview.Heading", background=PANEL_HI, foreground=ORANGE, relief="flat",
                    borderwidth=0, padding=(8, 8), font=(FONT, 11, "bold"))
    style.map("Treeview.Heading", background=[("active", BORDER)], foreground=[("active", ORANGE_HOVER)])
    for orient in ("Vertical", "Horizontal"):
        name = f"{orient}.TScrollbar"
        style.configure(name, background=PANEL_HI, troughcolor=SURFACE, bordercolor=SURFACE,
                        lightcolor=PANEL_HI, darkcolor=PANEL_HI, arrowcolor=ORANGE, relief="flat")
        style.map(name, background=[("active", ORANGE_DIM)])


def style_tabs(tabview):
    """Selected tab = orange with black text; other tabs = white text on dark."""
    try:
        active = tabview.get()
        for name, button in tabview._segmented_button._buttons_dict.items():
            button.configure(text_color=BLACK if name == active else WHITE, font=(FONT, 13, "bold"))
    except (AttributeError, KeyError):
        pass  # purely cosmetic; never break the app over tab colours


class Logo(ctk.CTkFrame):
    """White 'Brew' followed by 'Hub' in a rounded orange badge."""
    def __init__(self, master, size=24):
        super().__init__(master, fg_color="transparent")
        ctk.CTkLabel(self, text="Brew", font=(FONT, size, "bold"), text_color=WHITE).pack(side="left")
        badge = ctk.CTkFrame(self, fg_color=ORANGE, corner_radius=max(4, size // 4))
        badge.pack(side="left", padx=(4, 0))
        ctk.CTkLabel(badge, text="Hub", font=(FONT, size, "bold"), text_color=BLACK).pack(
            padx=max(6, size // 3), pady=(0, max(1, size // 12)))
