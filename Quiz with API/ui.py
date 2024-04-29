from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)

        self.score = Label(text="Score: 0", bg=THEME_COLOR)
        self.score.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, font=("Arial", 20, "italic"),
                                                     text="Hello this is a sample text", fill=THEME_COLOR, width=280)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        true_img = PhotoImage(file="images/true.png")
        self.true = Button(image=true_img, highlightthickness=0, command=self.true_pressed)
        self.true.grid(column=1, row=2)

        false_img = PhotoImage(file="images/false.png")
        self.false = Button(image=false_img, highlightthickness=0, command=self.false_pressed)
        self.false.grid(column=0, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        self.score.config(text=f"Score: {self.quiz.score}")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've successfully completed the quiz!")
            self.true.config(state="disabled")
            self.false.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, func=self.get_next_question)
