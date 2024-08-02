import tkinter as tk
from tkinter import ttk
import json
import os 
import time
from datetime import datetime
from tkinter import messagebox 


class RestaurantManagementSystem:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Restaurant Management System")
        self.root.geometry("1280x720")
        self.current_user = None

        self.style = ttk.Style()
        self.style.configure("TLabel", font=("Arial", 18))
        self.style.configure("TButton", font=("Arial", 14), relief="raised", background="#87CEEB", foreground="#87CEEB", padding=10)
        self.style.configure("Error.TLabel", font=("Arial", 12), foreground="red")

        # Load menu items from a file
        self.menu_file = "menu.json"
        self.load_menu()

        # Order details
        self.order_items = []

    def run(self):
        self.show_login_screen()
        self.root.mainloop()

    def load_menu(self):
        try:
            with open(self.menu_file, "r") as file:
                self.menu_items = json.load(file)
        except FileNotFoundError:
            self.menu_items = []

    def save_menu(self):
        with open(self.menu_file, "w") as file:
            json.dump(self.menu_items, file)

    def show_login_screen(self):
        self.clear_screen()
        label = ttk.Label(self.root, text="Login Screen")
        label.pack(pady=20)

        username_label = ttk.Label(self.root, text="Username:")
        username_label.pack()
        self.username_entry = ttk.Entry(self.root, width=30)
        self.username_entry.pack()

        password_label = ttk.Label(self.root, text="Password:")
        password_label.pack()
        self.password_entry = ttk.Entry(self.root, show="*", width=30)
        self.password_entry.pack()

        login_button = ttk.Button(self.root, text="Login", command=self.login)
        login_button.pack(pady=20)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Check if username and password are valid
        # Replace this with your own authentication logic
        if username == "sid" and password == "sid":
            self.current_user = username
            self.show_menu_screen()
        else:
            self.show_error_message("Invalid credentials")

    def show_menu_screen(self):
        self.clear_screen()
        label = ttk.Label(self.root, text="Menu Screen")
        label.pack(pady=20)

        edit_menu_button = ttk.Button(self.root, text="Edit Menu", command=self.show_edit_menu_screen)
        edit_menu_button.pack()

        view_menu_button = ttk.Button(self.root, text="View Menu", command=self.show_view_menu_screen)
        view_menu_button.pack()

        place_order_button = ttk.Button(self.root, text="Place Order", command=self.show_place_order_screen)
        place_order_button.pack()

        logout_button = ttk.Button(self.root, text="Logout", command=self.logout)
        logout_button.pack()

    def show_edit_menu_screen(self):
        self.clear_screen()
        label = ttk.Label(self.root, text="Edit Menu Screen")
        label.pack(pady=20)

        # Display current menu items
        

        add_item_label = ttk.Label(self.root, text="Add New Item:")
        add_item_label.pack()

        new_item_label = ttk.Label(self.root, text="Item Name:")
        new_item_label.pack()
        self.new_item_entry = ttk.Entry(self.root, width=30)
        self.new_item_entry.pack()

        new_price_label = ttk.Label(self.root, text="Price:")
        new_price_label.pack()
        self.new_price_entry = ttk.Entry(self.root, width=30)
        self.new_price_entry.pack()

        add_item_button = ttk.Button(self.root, text="Add Item", command=self.add_item_to_menu)
        add_item_button.pack(pady=10)

        remove_item_label = ttk.Label(self.root, text="Remove Item:")
        remove_item_label.pack()

        remove_item_combobox = ttk.Combobox(self.root, values=[item["name"] for item in self.menu_items], state="readonly")
        remove_item_combobox.pack()

        remove_item_button = ttk.Button(self.root, text="Remove Item", command=lambda: self.remove_item_from_menu(remove_item_combobox.get()))
        remove_item_button.pack(pady=10)

        back_button = ttk.Button(self.root, text="Back", command=self.show_menu_screen)
        back_button.pack(pady=20)

    def add_item_to_menu(self):
        new_item = self.new_item_entry.get()
        new_price = self.new_price_entry.get()

        # Validate input
        if not new_item or not new_price:
            self.show_error_message("Invalid item name or price")
            return

        try:
            new_price = float(new_price)
        except ValueError:
            self.show_error_message("Invalid price")
            return

        self.menu_items.append({"name": new_item, "price": new_price})
        self.save_menu()
        self.show_success_message("Item added to the menu")

    def remove_item_from_menu(self, item_name):
        for item in self.menu_items:
            if item["name"] == item_name:
                self.menu_items.remove(item)
                self.save_menu()
                self.show_success_message("Item removed from the menu")
                return

        self.show_error_message("Item not found in the menu")

    def show_view_menu_screen(self):
        self.clear_screen()
        label = ttk.Label(self.root, text="View Menu Screen")
        label.pack(pady=20)

        # Display current menu items
        for item in self.menu_items:
            menu_item_label = ttk.Label(self.root, text=f"{item['name']}: \u20B9{item['price']:.2f}")
            menu_item_label.pack(pady=5)

        back_button = ttk.Button(self.root, text="Back", command=self.show_menu_screen)
        back_button.pack(pady=20)

    def show_place_order_screen(self):
        self.clear_screen()
        label = ttk.Label(self.root, text="Place Order Screen")
        label.pack(pady=20)

        customer_name_label = ttk.Label(self.root, text="Customer Name:")
        customer_name_label.pack()
        self.customer_name_entry = ttk.Entry(self.root, width=30)
        self.customer_name_entry.pack()

        item_label = ttk.Label(self.root, text="Select Item:")
        item_label.pack()
        self.item_combobox = ttk.Combobox(self.root, values=[item["name"] for item in self.menu_items], state="readonly")
        self.item_combobox.pack()

        quantity_label = ttk.Label(self.root, text="Enter Quantity:")
        quantity_label.pack()
        self.quantity_entry = ttk.Entry(self.root, width=30)
        self.quantity_entry.pack()

        add_to_order_button = ttk.Button(self.root, text="Add to Order", command=self.add_to_order)
        add_to_order_button.pack(pady=10)

        order_details_label = ttk.Label(self.root, text="Order Details:")
        order_details_label.pack()

        self.order_listbox = tk.Listbox(self.root, width=50)
        self.order_listbox.pack()

        
        print_receipt_button = ttk.Button(self.root, text="Print Receipt", command=self.print_receipt)
        print_receipt_button.pack(pady=10)

        place_order_button = ttk.Button(self.root, text="Place Order", command=self.place_order)
        place_order_button.pack(pady=10)


        back_button = ttk.Button(self.root, text="Back", command=self.show_menu_screen)
        back_button.pack(pady=10)

    def show_message(self, message):
        tk.messagebox.showinfo("Message", message)

    def calculate_total(self):
        total = 0
        for item in self.order_items:
            item_name = item["item"]
            item_quantity = item["quantity"]
            item_price = next((x["price"] for x in self.menu_items if x["name"] == item_name), 0)
            item_total = item_price * item_quantity
            total += item_total
        return total

    def print_receipt(self):
        customer_name = self.customer_name_entry.get()
        if not customer_name:
            self.show_error_message("Please enter customer name")
            return

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        restaurant_name = "Sample Restaurant 1"  


        receipt = f"{restaurant_name}\n\n"
        receipt += f"Customer: {customer_name}\n"
        receipt += f"Date: {timestamp}\n\n"
        receipt += "-----------------------------\n"
        for item in self.order_items:
            item_name = item["item"]
            item_quantity = item["quantity"]
            item_price = next((x["price"] for x in self.menu_items if x["name"] == item_name), 0)
            item_total = item_price * item_quantity
            receipt += f"{item_name} x {item_quantity}: ₹{item_total:.2f}\n"

        receipt += "-----------------------------\n"
        receipt += f"Total: ₹{self.calculate_total():.2f}\n\n"
        receipt += "Thank you for dining with us!"

        self.show_message(receipt)

    def add_to_order(self):
        item = self.item_combobox.get()
        quantity = self.quantity_entry.get()

        # Validate input
        if not item or not quantity:
            self.show_error_message("Invalid item or quantity")
            return

        try:
            quantity = int(quantity)
        except ValueError:
            self.show_error_message("Invalid quantity")
            return

        self.order_items.append({"item": item, "quantity": quantity})
        self.order_listbox.insert(tk.END, f"{item}: {quantity}")

        self.item_combobox.set("")
        self.quantity_entry.delete(0, tk.END)

    def place_order(self):
        if not self.order_items:
            self.show_error_message("No items in the order")
            return

        customer_name = self.customer_name_entry.get()
        if not customer_name:
            self.show_error_message("Please enter customer name")
            return

        total = self.calculate_total_bill()
        self.show_success_message(f"Order placed successfully for {customer_name}! Total bill: \u20B9{total:.2f}")

        self.order_items = []
        self.order_listbox.delete(0, tk.END)

    def calculate_total_bill(self):
        total = 0
        for item in self.order_items:
            item_name = item["item"]
            item_quantity = item["quantity"]
            item_price = next((x["price"] for x in self.menu_items if x["name"] == item_name), 0)
            total += item_price * item_quantity
        return total

    def logout(self):
        self.current_user = None
        self.order_items = []
        self.show_login_screen()

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def show_error_message(self, message):
        error_label = ttk.Label(self.root, text=message, style="Error.TLabel")
        error_label.pack()

    def show_success_message(self, message):
        success_label = ttk.Label(self.root, text=message, foreground="green")
        success_label.pack()

# Main program
rms = RestaurantManagementSystem()
rms.run()
