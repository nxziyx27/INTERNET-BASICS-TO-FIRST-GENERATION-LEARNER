import tkinter as tk
from tkinter import messagebox
from records import RecordsWindow


class AdminLoginWindow:

    def __init__(self, parent):

        self.window = tk.Toplevel(parent)

        self.window.title("Admin Login")
        self.window.geometry("500x450")
        self.window.configure(bg="#F3E5F5")

        self.window.resizable(False, False)

        # ==============================
        # HEADER
        # ==============================

        header = tk.Frame(
            self.window,
            bg="#542C85",
            height=90
        )

        header.pack(fill="x")
        header.pack_propagate(False)

        title = tk.Label(
            header,
            text="🔐 Admin Login",
            font=("Arial", 25, "bold"),
            bg="#542C85",
            fg="white"
        )

        title.pack(pady=25)

        # ==============================
        # CONTENT
        # ==============================

        content = tk.Frame(
            self.window,
            bg="#F3E5F5"
        )

        content.pack(
            fill="both",
            expand=True,
            padx=40,
            pady=30
        )

        # Username

        tk.Label(
            content,
            text="👤 Admin Username",
            font=("Arial", 13, "bold"),
            bg="#F3E5F5",
            fg="#542C85"
        ).pack(
            anchor="w",
            pady=(10, 5)
        )

        self.username_entry = tk.Entry(
            content,
            font=("Arial", 13),
            width=30
        )

        self.username_entry.pack(
            pady=5,
            ipady=7
        )

        # Password

        tk.Label(
            content,
            text="🔑 Admin Password",
            font=("Arial", 13, "bold"),
            bg="#F3E5F5",
            fg="#542C85"
        ).pack(
            anchor="w",
            pady=(15, 5)
        )

        self.password_entry = tk.Entry(
            content,
            font=("Arial", 13),
            width=30,
            show="*"
        )

        self.password_entry.pack(
            pady=5,
            ipady=7
        )

        # Login Button

        login_button = tk.Button(
            content,
            text="🔓 Login to Dashboard",
            font=("Arial", 13, "bold"),
            bg="#673AB7",
            fg="white",
            activebackground="#4527A0",
            activeforeground="white",
            width=25,
            height=2,
            relief="flat",
            cursor="hand2",
            command=self.login
        )

        login_button.pack(
            pady=25
        )

        # Close Button

        close_button = tk.Button(
            content,
            text="❌ Close",
            font=("Arial", 11, "bold"),
            bg="#E53935",
            fg="white",
            width=15,
            relief="flat",
            cursor="hand2",
            command=self.window.destroy
        )

        close_button.pack()

        # Enter key

        self.window.bind(
            "<Return>",
            lambda event: self.login()
        )

    # ==============================
    # ADMIN LOGIN
    # ==============================

    def login(self):

        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()

        # Admin credentials

        ADMIN_USERNAME = "admin"
        ADMIN_PASSWORD = "admin123"

        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:

            messagebox.showinfo(
                "Login Successful",
                "✅ Welcome Admin!"
            )

            self.window.destroy()

            RecordsWindow(
                self.window.master
            )

        else:

            messagebox.showerror(
                "Login Failed",
                "❌ Incorrect username or password."
            )