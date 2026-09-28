import tkinter as tk

from course import CourseWindow
from quiz import QuizWindow
from login import LoginWindow
from admin import AdminLoginWindow
import certificate
import database


class InternetBasicsApp:

    def __init__(self, root):

        self.root = root

        self.root.title(
            "Internet Basics Learning System"
        )

        self.root.geometry(
            "1000x750"
        )

        self.root.configure(
            bg="#F5F0FF"
        )

        # ==================================================
        # STUDENT INFORMATION
        # ==================================================

        self.student_name = ""
        self.student_email = ""
        self.learner_id = None

        # ==================================================
        # HEADER
        # ==================================================

        self.create_header()

        # ==================================================
        # LOGIN
        # ==================================================

        self.show_login()

    # ==================================================
    # HEADER
    # ==================================================

    def create_header(self):

        header = tk.Frame(
            self.root,
            bg="#542C85",
            height=80
        )

        header.pack(
            fill="x"
        )

        header.pack_propagate(False)

        title = tk.Label(
            header,
            text="🌐 Internet Basics Learning System",
            font=("Arial", 23, "bold"),
            bg="#542C85",
            fg="white"
        )

        title.pack(
            pady=20
        )

    # ==================================================
    # LOGIN
    # ==================================================

    def show_login(self):

        LoginWindow(
            self.root,
            self.login_success
        )

    # ==================================================
    # LOGIN SUCCESS
    # ==================================================

    def login_success(self, name, email):

        self.student_name = name
        self.student_email = email

        # Save learner

        database.add_learner(
            name,
            email
        )

        # Get learner ID

        learner = database.get_learner(
            name,
            email
        )

        if learner:

            self.learner_id = learner[0]

        else:

            self.learner_id = None

        # Open home

        self.create_home()

    # ==================================================
    # HOME PAGE
    # ==================================================

    def create_home(self):

        body = tk.Frame(
            self.root,
            bg="#F5F0FF"
        )

        body.pack(
            fill="both",
            expand=True
        )

        # ==================================================
        # WELCOME
        # ==================================================

        heading = tk.Label(
            body,
            text=f"Welcome, {self.student_name}! 👋",
            font=("Arial", 28, "bold"),
            bg="#F5F0FF",
            fg="#542C85"
        )

        heading.pack(
            pady=(30, 5)
        )

        # ==================================================
        # EMAIL
        # ==================================================

        email_label = tk.Label(
            body,
            text=f"📧 {self.student_email}",
            font=("Arial", 12),
            bg="#F5F0FF",
            fg="#666666"
        )

        email_label.pack(
            pady=3
        )

        # ==================================================
        # DESCRIPTION
        # ==================================================

        desc = tk.Label(
            body,
            text=(
                "Learn Internet Basics Step by Step\n"
                "Designed for First Generation Learners"
            ),
            font=("Arial", 15),
            bg="#F5F0FF",
            fg="#333333"
        )

        desc.pack(
            pady=15
        )

        # ==================================================
        # BUTTON FRAME
        # ==================================================

        button_frame = tk.Frame(
            body,
            bg="#F5F0FF"
        )

        button_frame.pack(
            pady=20
        )

        # ==================================================
        # COURSE
        # ==================================================

        course_btn = tk.Button(
            button_frame,
            text="📚 5-Day Course",
            width=22,
            height=2,
            bg="#2196F3",
            fg="white",
            activebackground="#1565C0",
            activeforeground="white",
            font=("Arial", 14, "bold"),
            relief="flat",
            cursor="hand2",
            command=self.open_course
        )

        course_btn.grid(
            row=0,
            column=0,
            padx=15,
            pady=12
        )

        # ==================================================
        # QUIZ
        # ==================================================

        quiz_btn = tk.Button(
            button_frame,
            text="❓ Take Quiz",
            width=22,
            height=2,
            bg="#00A896",
            fg="white",
            activebackground="#00796B",
            activeforeground="white",
            font=("Arial", 14, "bold"),
            relief="flat",
            cursor="hand2",
            command=self.open_quiz
        )

        quiz_btn.grid(
            row=0,
            column=1,
            padx=15,
            pady=12
        )

        # ==================================================
        # CERTIFICATE
        # ==================================================

        certificate_btn = tk.Button(
            button_frame,
            text="🏆 Certificate",
            width=22,
            height=2,
            bg="#FF9800",
            fg="white",
            activebackground="#EF6C00",
            activeforeground="white",
            font=("Arial", 14, "bold"),
            relief="flat",
            cursor="hand2",
            command=self.open_certificate
        )

        certificate_btn.grid(
            row=1,
            column=0,
            padx=15,
            pady=12
        )

        # ==================================================
        # EXIT
        # ==================================================

        exit_btn = tk.Button(
            button_frame,
            text="❌ Exit",
            width=22,
            height=2,
            bg="#E53935",
            fg="white",
            activebackground="#B71C1C",
            activeforeground="white",
            font=("Arial", 14, "bold"),
            relief="flat",
            cursor="hand2",
            command=self.root.destroy
        )

        exit_btn.grid(
            row=1,
            column=1,
            padx=15,
            pady=12
        )

        # ==================================================
        # ADMIN ACCESS
        # ==================================================

        admin_button = tk.Button(
            body,
            text="🔐 Admin Login",
            width=18,
            height=2,
            bg="#673AB7",
            fg="white",
            activebackground="#4527A0",
            activeforeground="white",
            font=("Arial", 11, "bold"),
            relief="flat",
            cursor="hand2",
            command=self.open_admin
        )

        admin_button.pack(
            pady=10
        )

        # ==================================================
        # FOOTER
        # ==================================================

        footer = tk.Label(
            body,
            text="CEP Project • Internet Basics • Digital Learning",
            bg="#F5F0FF",
            fg="#777777",
            font=("Arial", 10)
        )

        footer.pack(
            side="bottom",
            pady=12
        )

    # ==================================================
    # COURSE
    # ==================================================

    def open_course(self):

        CourseWindow(
            self.root
        )

    # ==================================================
    # QUIZ
    # ==================================================

    def open_quiz(self):

        QuizWindow(
            self.root,
            self.student_name,
            self.learner_id
        )

    # ==================================================
    # CERTIFICATE
    # ==================================================

    def open_certificate(self):

        certificate.CertificateWindow(
            self.root,
            self.student_name
        )

    # ==================================================
    # ADMIN
    # ==================================================

    def open_admin(self):

        AdminLoginWindow(
            self.root
        )


# ======================================================
# START APPLICATION
# ======================================================

root = tk.Tk()

app = InternetBasicsApp(
    root
)

root.mainloop()