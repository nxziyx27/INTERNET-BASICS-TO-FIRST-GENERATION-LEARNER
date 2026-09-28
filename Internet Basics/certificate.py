import tkinter as tk
from datetime import datetime


class CertificateWindow:

    def __init__(self, parent, student_name="Student"):

        self.window = tk.Toplevel(parent)

        self.window.title("Course Completion Certificate")
        self.window.geometry("700x550")
        self.window.configure(bg="#F3E5F5")

        # Certificate title
        title = tk.Label(
            self.window,
            text="🎓 COURSE COMPLETION CERTIFICATE",
            font=("Arial", 22, "bold"),
            bg="#F3E5F5",
            fg="#6A1B9A"
        )

        title.pack(pady=35)

        # Congratulations
        congratulations = tk.Label(
            self.window,
            text=f"Congratulations, {student_name}! 🎉",
            font=("Arial", 24, "bold"),
            bg="#F3E5F5",
            fg="#E91E63"
        )

        congratulations.pack(pady=20)

        # Course information
        course = tk.Label(
            self.window,
            text="You have successfully completed",
            font=("Arial", 16),
            bg="#F3E5F5",
            fg="#333333"
        )

        course.pack(pady=5)

        # Course name
        course_name = tk.Label(
            self.window,
            text="Internet Basics Course",
            font=("Arial", 20, "bold"),
            bg="#F3E5F5",
            fg="#1565C0"
        )

        course_name.pack(pady=10)

        # Student name
        student = tk.Label(
            self.window,
            text=f"Student: {student_name}",
            font=("Arial", 15, "bold"),
            bg="#F3E5F5",
            fg="#333333"
        )

        student.pack(pady=15)

        # Completion date
        completion_date = datetime.now().strftime("%d %B %Y")

        date_label = tk.Label(
            self.window,
            text=f"Date: {completion_date}",
            font=("Arial", 14),
            bg="#F3E5F5",
            fg="#555555"
        )

        date_label.pack(pady=5)

        # Close button
        close_button = tk.Button(
            self.window,
            text="Close",
            command=self.window.destroy,
            font=("Arial", 12, "bold"),
            bg="#6A1B9A",
            fg="white",
            padx=30,
            pady=10
        )

        close_button.pack(pady=25)