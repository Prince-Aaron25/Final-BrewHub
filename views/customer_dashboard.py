import customtkinter as ctk
import theme
from views.common import Page, header
from views.menu_view import MenuView
from views.cart_view import CartView
from views.order_view import OrderView
from views.profile_view import ProfileView


class CustomerDashboard(Page):
    def __init__(self,master,app):
        super().__init__(master,app)
        header(self,app)
        self.tabs = ctk.CTkTabview(self,command=self.on_tab)
        self.tabs.pack(fill="both",expand=True,padx=10,pady=10)
        self.pages = {}
        for label,cls in [("Menu",MenuView),("Cart",CartView),("My orders",OrderView),("Profile",ProfileView)]:
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

# Older imports may refer to this name.
Customer_DashboardView = CustomerDashboard
