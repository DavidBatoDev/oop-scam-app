import tkinter as tk
import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox

class SearchBar(ctk.CTkFrame):
    def __init__(self, parent, search_handler=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.search_handler = search_handler
        self.setup_ui()





    def setup_ui(self):
        # Frame for the search box to add padding and style
        self.configure(corner_radius=20, border_width=0, fg_color="#222B36")
        self.pack(pady=15, padx=15, fill="x")

        # Create an entry widget for search input
        self.search_entry = ctk.CTkEntry(self,
                                         width=300,
                                         corner_radius=20,
                                         border_width=0,
                                         placeholder_text="Search",
                                         height=30,
                                         fg_color="#222B36"
                                         )
        self.search_entry.pack(fill="x", expand=True,padx=10, pady=2)

        # Create a label for the search icon inside the frame
        self.search_icon_label = ctk.CTkLabel(self, text="🔍",
                                              corner_radius=10,
                                              width=20, height=30,
                                              fg_color="#222B36"
                                              )

        # Bind focus in and focus out events to show/hide the search icon
        self.search_entry.bind("<FocusIn>", self.on_entry_click)
        self.search_entry.bind("<FocusOut>", self.on_entry_focusout)

        # Bind Enter key to trigger the search function
        self.search_entry.bind("<Return>", self.search)
        self.search_entry.bind("<BackSpace>", self.search)
        self.search_entry.bind("<KP_Enter>", self.search)

    def search(self, event=None):
        query = self.search_entry.get()
        self.search_handler(query)

    def on_entry_click(self, event):
        # Adjust the entry widget to make room for the icon
        self.search_entry.pack_configure(side="right", fill="x", expand=True,  pady=3, padx=(0,10))

        # Show the search icon label using pack instead of place
        self.search_icon_label.pack(side="right", fill="none", pady=2, padx=(6,0))

    def on_entry_focusout(self, event):
        # Hide the search icon label using pack_forget
        self.search_icon_label.pack_forget()
        self.search_entry.pack(fill="x", expand=True,padx=10, pady=2)