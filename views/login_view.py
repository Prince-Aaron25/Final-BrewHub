import customtkinter as ctk
import theme
from views.common import Page
from services.auth_service import AuthService


class LoginView(Page):
    def __init__(self, master, app):
        super().__init__(master,app)
        self.configure(fg_color=theme.BLACK)
        box = ctk.CTkFrame(self,width=460,corner_radius=10,fg_color=theme.PANEL,border_width=1,border_color=theme.BORDER)
        box.pack(pady=(80,10),padx=30)
        theme.Logo(box,44).pack(padx=90,pady=(36,6))
        ctk.CTkLabel(box,text="Cafe ordering and inventory",text_color=theme.MUTED).pack()
        ctk.CTkLabel(box,text="Sign in using your email address",font=(theme.FONT,13,"bold")).pack(pady=(22,6))
        self.email = ctk.CTkEntry(box,placeholder_text="Email",width=330,height=40)
        self.email.pack(padx=35,pady=8)
        self.password = ctk.CTkEntry(box,placeholder_text="Password",show="*",width=330,height=40)
        self.password.pack(padx=35,pady=8)
        ctk.CTkButton(box,text="Log in",width=330,height=42,font=(theme.FONT,14,"bold"),
                      command=lambda:app.run_action(self.login)).pack(pady=(14,8))
        ctk.CTkButton(box,text="Create customer account",width=330,height=38,fg_color="transparent",border_width=2,
                      text_color=theme.ORANGE,hover_color=theme.PANEL_HI,font=(theme.FONT,12,"bold"),
                      command=app.show_register).pack(pady=(0,30))
        self.password.bind("<Return>",lambda event:app.run_action(self.login))
        self.note("First use: run setup_db.py to prepare the database and create your admin account.")

    def login(self):
        user = AuthService().login(self.email.get(),self.password.get())
        self.app.signed_in(user)
