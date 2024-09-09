import tkinter as tk
from tkinter import messagebox, simpledialog

class ContactBook:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")

       
        self.contacts = {}

        
        self.create_widgets()

    def create_widgets(self):
        
        tk.Label(self.root, text="Name:").grid(row=0, column=0, padx=5, pady=5)
        tk.Label(self.root, text="Phone Number:").grid(row=1, column=0, padx=5, pady=5)
        tk.Label(self.root, text="Email:").grid(row=2, column=0, padx=5, pady=5)
        tk.Label(self.root, text="Address:").grid(row=3, column=0, padx=5, pady=5)

        self.name_entry = tk.Entry(self.root)
        self.phone_entry = tk.Entry(self.root)
        self.email_entry = tk.Entry(self.root)
        self.address_entry = tk.Entry(self.root)

        self.name_entry.grid(row=0, column=1, padx=5, pady=5)
        self.phone_entry.grid(row=1, column=1, padx=5, pady=5)
        self.email_entry.grid(row=2, column=1, padx=5, pady=5)
        self.address_entry.grid(row=3, column=1, padx=5, pady=5)

        tk.Button(self.root, text="Add Contact", command=self.add_contact).grid(row=4, column=0, columnspan=2, pady=10)

        
        tk.Button(self.root, text="View Contacts", command=self.view_contacts).grid(row=5, column=0, columnspan=2, pady=5)

       
        tk.Button(self.root, text="Search Contact", command=self.search_contact).grid(row=6, column=0, columnspan=2, pady=5)

       
        tk.Button(self.root, text="Update Contact", command=self.update_contact).grid(row=7, column=0, columnspan=2, pady=5)

        
        tk.Button(self.root, text="Delete Contact", command=self.delete_contact).grid(row=8, column=0, columnspan=2, pady=5)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        if not name or not phone:
            messagebox.showerror("Error", "Name and Phone Number are required.")
            return

        self.contacts[name] = {"Phone": phone, "Email": email, "Address": address}
        messagebox.showinfo("Success", "Contact added successfully!")

       
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)

    def view_contacts(self):
        contacts_str = ""
        for name, info in self.contacts.items():
            contacts_str += f"Name: {name}\nPhone: {info['Phone']}\nEmail: {info['Email']}\nAddress: {info['Address']}\n\n"
        if contacts_str:
            messagebox.showinfo("Contact List", contacts_str)
        else:
            messagebox.showinfo("Contact List", "No contacts available.")

    def search_contact(self):
        search_term = simpledialog.askstring("Search Contact", "Enter name or phone number:")
        if search_term:
            results = [f"Name: {name}\nPhone: {info['Phone']}\nEmail: {info['Email']}\nAddress: {info['Address']}\n"
                       for name, info in self.contacts.items()
                       if search_term.lower() in name.lower() or search_term in info['Phone']]
            if results:
                messagebox.showinfo("Search Results", "\n\n".join(results))
            else:
                messagebox.showinfo("Search Results", "No contacts found.")

    def update_contact(self):
        name = simpledialog.askstring("Update Contact", "Enter the name of the contact to update:")
        if name in self.contacts:
            new_phone = simpledialog.askstring("Update Contact", "Enter new phone number (leave blank to keep current):")
            new_email = simpledialog.askstring("Update Contact", "Enter new email (leave blank to keep current):")
            new_address = simpledialog.askstring("Update Contact", "Enter new address (leave blank to keep current):")

            if new_phone:
                self.contacts[name]["Phone"] = new_phone
            if new_email:
                self.contacts[name]["Email"] = new_email
            if new_address:
                self.contacts[name]["Address"] = new_address

            messagebox.showinfo("Success", "Contact updated successfully!")
        else:
            messagebox.showerror("Error", "Contact not found.")

    def delete_contact(self):
        name = simpledialog.askstring("Delete Contact", "Enter the name of the contact to delete:")
        if name in self.contacts:
            del self.contacts[name]
            messagebox.showinfo("Success", "Contact deleted successfully!")
        else:
            messagebox.showerror("Error", "Contact not found.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBook(root)
    root.mainloop()
