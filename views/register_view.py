import customtkinter as ctk
import theme
from views.common import Page, info
from services.auth_service import AuthService


class RegisterView(Page):
    def __init__(self, master, app):
        super().__init__(master,app)
        self.configure(fg_color=theme.BLACK)
        box = ctk.CTkFrame(self,corner_radius=10,fg_color=theme.PANEL,border_width=1,border_color=theme.BORDER)
        box.pack(pady=(40,10),padx=30)
        theme.Logo(box,34).pack(padx=90,pady=(26,2))
        ctk.CTkLabel(box,text="Create a customer account",font=(theme.FONT,18,"bold")).pack(pady=(6,12))
        self.inputs = {}
        for key,label in [("name","Full name"),("email","Email"),("phone","Phone (optional)"),("password","Password (8+ characters)"),("confirm","Repeat password")]:
            widget = ctk.CTkEntry(box,placeholder_text=label,width=400,height=40,show="*" if key in ("password","confirm") else "")
            widget.pack(pady=7,padx=35)
            self.inputs[key] = widget
        ctk.CTkButton(box,text="Register",width=400,height=42,font=(theme.FONT,14,"bold"),
                      command=lambda:app.run_action(self.register)).pack(pady=(14,8))
        ctk.CTkButton(box,text="Back to login",width=400,height=38,fg_color="transparent",border_width=2,
                      text_color=theme.ORANGE,hover_color=theme.PANEL_HI,font=(theme.FONT,12,"bold"),
                      command=app.show_login).pack(pady=(0,28))

    def register(self):
        values = {key:widget.get() for key,widget in self.inputs.items()}
        if values["password"] != values["confirm"]:
            raise ValueError("Passwords do not match.")
        AuthService().register(values["name"],values["email"],values["phone"],values["password"])
        info("Account created. You can now log in.")
        self.app.show_login()
