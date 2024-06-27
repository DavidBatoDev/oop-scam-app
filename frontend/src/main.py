import customtkinter as ctk
import sys
import os

from app_gui import AppFrame
from dashboard_gui import DashboardFrame
from user_model import UserModel

# Module Frames for SCAM App Features
from auth import LoginFrame
from notes import NotesFrame
from home import HomeFrame
from templates import TemplatesFrame
from event_calendar import CalendarFrame
from tasks import TasksFrame
from flashcards import FlashcardsFrame
from progress import ProgressFrame
from collaboration import CollaborationFrame

# Append the parent directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config import APP_NAME, BACKGROUND_COLOR

class MainApp(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title(APP_NAME)
        
        width = self.winfo_screenwidth() * 100
        height = self.winfo_screenheight() * 100
        self.geometry(f"{width}x{height}")
        self.attributes('-fullscreen', True)
        self.configure(fg_color=BACKGROUND_COLOR)
        ctk.set_appearance_mode("dark")

        # Session Attributes
        self.user = UserModel()

        ### Frames ###
        # Login
        self.login_frame = LoginFrame(self, callback=self.set_session_data)

        # Main App Frame for SCAM App Features
        self.app_frame = AppFrame(self)

        # Dashboard Frame
        self.dashboard_frame = DashboardFrame(self,
            command=self.app_frame.show_frame,
            frames=self.app_frame.module_frames,
            width=200,
        )

        self.pack_login()

    def pack_mainscreen(self):
        # Dashboard Frame
        self.dashboard_frame.pack(side='left', fill='y')

        # Main App Frame for SCAM App Features
        self.app_frame.pack(side='left', expand=True, fill='both')

    def pack_login(self) -> None:
        # Add the Login Frame
        self.login_frame.pack(expand=True)
        self.dashboard_frame.pack_forget()
        

    def on_login_success(self) -> None:
        print(f'Login Successful!, Welcome {self.user.username}')
        self.login_frame.destroy()
        self.pack_mainscreen()

    def set_session_data(self, data) -> None:
        try:
            self.user = UserModel.from_json(data)
        except Exception as e: # Catch all exceptions, for now, will add when user fails login
            print(e)
            return
        self.on_login_success()

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()