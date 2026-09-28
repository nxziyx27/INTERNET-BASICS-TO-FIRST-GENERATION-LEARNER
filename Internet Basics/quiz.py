
import tkinter as tk
from tkinter import messagebox

from certificate import CertificateWindow
import database


class QuizWindow:

    def __init__(self, parent, student_name="Student", learner_id=None):

        self.student_name = student_name
        self.learner_id = learner_id

        self.window = tk.Toplevel(parent)
        self.window.title("Internet Basics Quiz")
        self.window.geometry("1000x700")
        self.window.minsize(800, 600)
        self.window.configure(bg="#F5F0FF")

        # ================= QUESTIONS =================

        self.questions = [

            {
                "question": "1. 🌐 What is the Internet?",
                "options": [
                    "A worldwide network connecting computers",
                    "A computer game",
                    "A type of printer",
                    "A mobile application"
                ],
                "answer": "A worldwide network connecting computers"
            },

            {
                "question": "2. 🌍 Which application is used to browse websites?",
                "options": [
                    "Google Chrome",
                    "Calculator",
                    "Camera",
                    "Notepad"
                ],
                "answer": "Google Chrome"
            },

            {
                "question": "3. 🔍 You want to find information about Mumbai. What should you use?",
                "options": [
                    "Search Engine",
                    "Calculator",
                    "Paint",
                    "Music Player"
                ],
                "answer": "Search Engine"
            },

            {
                "question": "4. 📧 What is Email mainly used for?",
                "options": [
                    "Sending and receiving messages online",
                    "Taking photographs",
                    "Playing offline games",
                    "Editing videos"
                ],
                "answer": "Sending and receiving messages online"
            },

            {
                "question": "5. 📩 In an email, where do you enter the receiver's email address?",
                "options": [
                    "To",
                    "Subject",
                    "Message",
                    "Attachment"
                ],
                "answer": "To"
            },

            {
                "question": "6. 📝 What should you write in the Subject of an email?",
                "options": [
                    "The main topic of the email",
                    "Your password",
                    "Your OTP",
                    "Your phone PIN"
                ],
                "answer": "The main topic of the email"
            },

            {
                "question": "7. 📎 You want to send a photo with an email. What can you use?",
                "options": [
                    "Attachment",
                    "Subject",
                    "Search Bar",
                    "Browser History"
                ],
                "answer": "Attachment"
            },

            {
                "question": "8. 🔐 Which action is safest while using the Internet?",
                "options": [
                    "Never share your OTP or password",
                    "Click every unknown link",
                    "Share your password with friends",
                    "Use the same password everywhere"
                ],
                "answer": "Never share your OTP or password"
            },

            {
                "question": "9. ⚠️ You receive a message saying 'You won a prize! Click this unknown link.' What should you do?",
                "options": [
                    "Avoid clicking the link",
                    "Click immediately",
                    "Share it with friends",
                    "Give your OTP"
                ],
                "answer": "Avoid clicking the link"
            },

            {
                "question": "10. 🔑 Which password is the strongest?",
                "options": [
                    "123456",
                    "password",
                    "N@ziya123!",
                    "abcdef"
                ],
                "answer": "N@ziya123!"
            }

        ]

        # ================= COLORS =================

        self.colors = [
            "#2196F3",
            "#00A896",
            "#FF9800",
            "#E91E63",
            "#673AB7",
            "#009688",
            "#3F51B5",
            "#4CAF50",
            "#F44336",
            "#9C27B0"
        ]

        # Stores learner's selected answers
        self.vars = []

        # Stores the answer option buttons
        self.option_buttons = []

        self.create_header()
        self.create_quiz_area()

        # Handle window close
        self.window.protocol(
            "WM_DELETE_WINDOW",
            self.close_window
        )

    # ==================================================
    # HEADER
    # ==================================================

    def create_header(self):

        header = tk.Frame(
            self.window,
            bg="#542C85",
            height=85
        )

        header.pack(fill="x")
        header.pack_propagate(False)

        title = tk.Label(
            header,
            text="❓ Internet Basics Quiz",
            font=("Arial", 25, "bold"),
            bg="#542C85",
            fg="white"
        )

        title.pack(pady=22)

    # ==================================================
    # QUIZ AREA
    # ==================================================

    def create_quiz_area(self):

        # Welcome message

        welcome = tk.Label(
            self.window,
            text=f"Good luck, {self.student_name}! 🍀",
            font=("Arial", 18, "bold"),
            bg="#F5F0FF",
            fg="#542C85"
        )

        welcome.pack(pady=(12, 3))

        # Instructions

        instruction = tk.Label(
            self.window,
            text="Answer all questions and score 60% or more to pass.",
            font=("Arial", 12),
            bg="#F5F0FF",
            fg="#666666"
        )

        instruction.pack(pady=(0, 10))

        # ================= SCROLL CONTAINER =================

        container = tk.Frame(
            self.window,
            bg="#F5F0FF"
        )

        container.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=5
        )

        # Canvas

        self.canvas = tk.Canvas(
            container,
            bg="#F5F0FF",
            highlightthickness=0
        )

        # Scrollbar

        scrollbar = tk.Scrollbar(
            container,
            orient="vertical",
            command=self.canvas.yview
        )

        # Frame containing all questions

        self.quiz_frame = tk.Frame(
            self.canvas,
            bg="#F5F0FF"
        )

        # Put question frame inside canvas

        self.canvas_window = self.canvas.create_window(
            (0, 0),
            window=self.quiz_frame,
            anchor="nw"
        )

        # Update scroll area when questions change

        self.quiz_frame.bind(
            "<Configure>",
            self.update_scroll_region
        )

        # Resize question frame with canvas

        self.canvas.bind(
            "<Configure>",
            self.resize_frame
        )

        self.canvas.configure(
            yscrollcommand=scrollbar.set
        )

        self.canvas.pack(
            side="left",
            fill="both",
            expand=True
        )

        scrollbar.pack(
            side="right",
            fill="y"
        )

        # Mouse wheel scrolling

        self.canvas.bind_all(
            "<MouseWheel>",
            self.mouse_scroll
        )

        # ================= CREATE QUESTIONS =================

        for i, question in enumerate(self.questions):

            self.create_question_card(
                i,
                question
            )

        # ================= BUTTON FRAME =================

        button_frame = tk.Frame(
            self.window,
            bg="#F5F0FF"
        )

        button_frame.pack(
            fill="x",
            pady=10
        )

        # Submit button

        submit_button = tk.Button(
            button_frame,
            text="✅ Submit Quiz",
            font=("Arial", 13, "bold"),
            bg="#00A896",
            fg="white",
            activebackground="#00796B",
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            width=18,
            height=2,
            command=self.submit_quiz
        )

        submit_button.pack(
            side="left",
            padx=15
        )

        # Restart button

        restart_button = tk.Button(
            button_frame,
            text="🔄 Restart",
            font=("Arial", 13, "bold"),
            bg="#FF9800",
            fg="white",
            activebackground="#EF6C00",
            relief="flat",
            cursor="hand2",
            width=15,
            height=2,
            command=self.restart_quiz
        )

        restart_button.pack(
            side="left",
            padx=15
        )

        # Close button

        close_button = tk.Button(
            button_frame,
            text="❌ Close",
            font=("Arial", 13, "bold"),
            bg="#E53935",
            fg="white",
            activebackground="#B71C1C",
            relief="flat",
            cursor="hand2",
            width=15,
            height=2,
            command=self.close_window
        )

        close_button.pack(
            side="right",
            padx=15
        )

    # ==================================================
    # QUESTION CARD
    # ==================================================

    def create_question_card(self, index, question):

        color = self.colors[index]

        # Question card

        card = tk.Frame(
            self.quiz_frame,
            bg="white",
            highlightbackground=color,
            highlightthickness=3
        )

        card.pack(
            fill="x",
            padx=10,
            pady=8
        )

        # Question heading

        question_label = tk.Label(
            card,
            text=question["question"],
            font=("Arial", 14, "bold"),
            bg=color,
            fg="white",
            anchor="w",
            padx=15,
            pady=10
        )

        question_label.pack(fill="x")

        # IMPORTANT:
        # Use a unique variable for every question.
        # The special value means no answer is selected.

        var = tk.StringVar(
            master=self.window,
            value="__NONE__"
        )

        self.vars.append(var)

        # Store this question's buttons

        buttons_for_question = []

        self.option_buttons.append(
            buttons_for_question
        )

        # Create options as normal clickable buttons.
        # No radio button or checkbox indicators.

        for option in question["options"]:

            option_button = tk.Button(
                card,
                text="     " + option,
                font=("Arial", 12),
                bg="white",
                fg="#333333",
                activebackground="#E0F2F1",
                activeforeground="#004D40",
                relief="flat",
                anchor="w",
                cursor="hand2",
                bd=0,
                highlightthickness=1,
                highlightbackground="white",
                padx=10,
                pady=8,

                command=lambda opt=option, q_index=index:
                    self.select_option(q_index, opt)
            )

            option_button.pack(
                fill="x",
                padx=20,
                pady=3
            )

            buttons_for_question.append(
                (option_button, option)
            )

        # Bottom spacing

        tk.Frame(
            card,
            bg="white",
            height=8
        ).pack()

    # ==================================================
    # SELECT ANSWER
    # ==================================================

    def select_option(self, question_index, selected_option):

        # Save selected answer

        self.vars[question_index].set(
            selected_option
        )

        # Get buttons belonging to this question

        buttons = self.option_buttons[question_index]

        # Reset all options for this question

        for button, option in buttons:

            if option == selected_option:

                # Highlight selected answer

                button.configure(
                    bg="#B2DFDB",
                    fg="#004D40",
                    relief="solid",
                    highlightbackground="#00A896"
                )

            else:

                # Keep unselected answers blank

                button.configure(
                    bg="white",
                    fg="#333333",
                    relief="flat",
                    highlightbackground="white"
                )

    # ==================================================
    # SCROLL
    # ==================================================

    def update_scroll_region(self, event=None):

        self.canvas.configure(
            scrollregion=self.canvas.bbox("all")
        )

    def resize_frame(self, event):

        self.canvas.itemconfig(
            self.canvas_window,
            width=event.width
        )

    def mouse_scroll(self, event):

        self.canvas.yview_scroll(
            int(-1 * (event.delta / 120)),
            "units"
        )

    # ==================================================
    # SUBMIT QUIZ
    # ==================================================

    def submit_quiz(self):

        score = 0

        # Check every answer

        for i, question in enumerate(self.questions):

            selected_answer = self.vars[i].get()

            if selected_answer == question["answer"]:

                score += 1

        total_questions = len(self.questions)

        percentage = (
            score / total_questions
        ) * 100

        # Determine result

        if percentage >= 60:

            result = "PASSED"

        else:

            result = "FAILED"

        # ================= SAVE QUIZ ATTEMPT =================

        if self.learner_id is not None:

            database.add_quiz_attempt(
                self.learner_id,
                score,
                total_questions,
                percentage,
                result
            )

        # ================= PASS =================

        if percentage >= 60:

            messagebox.showinfo(
                "🎉 Quiz Result",
                f"🎉 Congratulations, {self.student_name}!\n\n"
                f"🏆 Score: {score}/{total_questions}\n"
                f"📊 Percentage: {percentage:.0f}%\n\n"
                f"✅ YOU PASSED!\n\n"
                f"Your certificate will now open."
            )

            CertificateWindow(
                self.window,
                self.student_name
            )

        # ================= FAIL =================

        else:

            messagebox.showwarning(
                "📚 Quiz Result",
                f"Keep learning, {self.student_name}!\n\n"
                f"📝 Score: {score}/{total_questions}\n"
                f"📊 Percentage: {percentage:.0f}%\n\n"
                f"❌ YOU DID NOT PASS.\n\n"
                f"Please review the course and try again!"
            )

    # ==================================================
    # RESTART QUIZ
    # ==================================================

    def restart_quiz(self):

        # Clear every selected answer

        for i, var in enumerate(self.vars):

            var.set("__NONE__")

            # Reset all buttons to blank

            for button, option in self.option_buttons[i]:

                button.configure(
                    bg="white",
                    fg="#333333",
                    relief="flat",
                    highlightbackground="white"
                )

        # Return to the first question

        self.canvas.yview_moveto(0)

        messagebox.showinfo(
            "🔄 Quiz Restarted",
            "All answers have been cleared.\n\n"
            "Good luck! 🍀"
        )

    # ==================================================
    # CLOSE
    # ==================================================

    def close_window(self):

        # Remove mouse wheel binding

        self.canvas.unbind_all(
            "<MouseWheel>"
        )

        # Close quiz window

        self.window.destroy()