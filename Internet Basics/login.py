import tkinter as tk
from tkinter import messagebox


class LoginWindow:

    def __init__(self, parent, on_login):

        self.parent = parent
        self.on_login = on_login

        self.window = tk.Toplevel(parent)
        self.window.title("Learner Login")
        self.window.geometry("600x550")
        self.window.configure(bg="#F3E5F5")

        # ================= HEADER =================

        header = tk.Frame(
            self.window,
            bg="#6A1B9A",
            height=90
        )

        header.pack(fill="x")
        header.pack_propagate(False)

        title = tk.Label(
            header,
            text="👤 Learner Login",
            font=("Arial", 25, "bold"),
            bg="#6A1B9A",
            fg="white"
        )

        title.pack(pady=25)

        # ================= WELCOME =================

        welcome = tk.Label(
            self.window,
            text="Welcome to Internet Basics! 🌐",
            font=("Arial", 18, "bold"),
            bg="#F3E5F5",
            fg="#6A1B9A"
        )

        welcome.pack(pady=25)

        # ================= NAME =================

        name_label = tk.Label(
            self.window,
            text="👤 Student Name",
            font=("Arial", 13, "bold"),
            bg="#F3E5F5",
            fg="#333333"
        )

        name_label.pack(anchor="w", padx=80)

        self.name_entry = tk.Entry(
            self.window,
            font=("Arial", 13),
            width=35,
            relief="solid"
        )

        self.name_entry.pack(pady=8)

        # ================= EMAIL =================

        email_label = tk.Label(
            self.window,
            text="📧 Email ID",
            font=("Arial", 13, "bold"),
            bg="#F3E5F5",
            fg="#333333"
        )

        email_label.pack(anchor="w", padx=80, pady=(15, 0))

        self.email_entry = tk.Entry(
            self.window,
            font=("Arial", 13),
            width=35,
            relief="solid"
        )

        self.email_entry.pack(pady=8)

        # ================= LOGIN BUTTON =================

        login_button = tk.Button(
            self.window,
            text="🚀 Start Learning",
            font=("Arial", 14, "bold"),
            bg="#00A896",
            fg="white",
            activebackground="#00796B",
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            width=20,
            height=2,
            command=self.login
        )

        login_button.pack(pady=30)

        # ================= FOOTER =================

        footer = tk.Label(
            self.window,
            text="Your details are used for learning records.",
            font=("Arial", 10),
            bg="#F3E5F5",
            fg="#777777"
        )

        footer.pack(pady=5)

    # ================= LOGIN FUNCTION =================

    def login(self):

        name = self.name_entry.get().strip()
        email = self.email_entry.get().strip()

        if name == "":
            messagebox.showwarning(
                "Missing Name",
                "Please enter your name."
            )
            return

        if email == "":
            messagebox.showwarning(
                "Missing Email",
                "Please enter your email ID."
            )
            return

        if "@" not in email or "." not in email:
            messagebox.showwarning(
                "Invalid Email",
                "Please enter a valid email ID."
            )
            return

        # Send student information to main application

        self.window.destroy()

        self.on_login(
            name,
            email
        )