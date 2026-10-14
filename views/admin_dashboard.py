import customtkinter as ctk
import theme
from views.common import Page, header
from views.product_view import ProductView
from views.recipe_view import RecipeView
from views.inventory_view import InventoryView
from views.order_view import OrderView
from views.report_view import ReportView
from views.user_view import UserView
from views.profile_view import ProfileView
from services.report_service import ReportService


class Overview(Page):
    def __init__(self,master,app):
        super().__init__(master,app)
        self.button(self.toolbar(),"Refresh",self.refresh)
        self.cards = ctk.CTkFrame(self,fg_color="transparent")
        self.cards.pack(fill="x",padx=12,pady=20)
        self.note("First setup: Categories -> Ingredients + stock -> Products -> Recipes. Then test a customer order.")

    def refresh(self):
        summary = ReportService(self.app.user).summary()
        for child in self.cards.winfo_children():
            child.destroy()
        columns = 3
        for index,(key,value) in enumerate(summary.items()):
            self.cards.grid_columnconfigure(index%columns,weight=1,uniform="stat")
            card = ctk.CTkFrame(self.cards,fg_color=theme.PANEL,border_width=1,border_color=theme.BORDER,corner_radius=8)
            card.grid(row=index//columns,column=index%columns,padx=8,pady=8,sticky="nsew")
            ctk.CTkFrame(card,fg_color=theme.ORANGE,height=3,corner_radius=0).pack(fill="x")
            ctk.CTkLabel(card,text=str(value),font=(theme.FONT,30,"bold"),text_color=theme.ORANGE).pack(pady=(18,2),padx=16)
            ctk.CTkLabel(card,text=str(key),text_color=theme.MUTED,font=(theme.FONT,12)).pack(pady=(0,18),padx=16)


class AdminDashboard(Page):
    def __init__(self,master,app):
        super().__init__(master,app)
        header(self,app,role="Admin")
        self.tabs = ctk.CTkTabview(self,command=self.on_tab)
        self.tabs.pack(fill="both",expand=True,padx=10,pady=10)
        self.pages = {}
        for label,cls in [("Overview",Overview),("Products",ProductView),("Recipes",RecipeView),("Inventory",InventoryView),
                          ("Orders & payments",OrderView),("Reports",ReportView),("Users",UserView),("Profile",ProfileView)]:
            tab = self.tabs.add(label)
            page = cls(tab,app)
            page.pack(fill="both",expand=True)
            self.pages[label] = page
        theme.style_tabs(self.tabs)
        self.after(50,self.refresh_current)

    def on_tab(self):
        theme.style_tabs(self.tabs)
        self.refresh_current()

    def refresh_current(self):
        self.app.run_action(self.pages[self.tabs.get()].refresh)
