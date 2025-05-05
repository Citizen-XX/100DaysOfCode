from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label()
        self.score_label.config(text="Score: 0", font=(
            'Arial', 12, "italic"), bg=THEME_COLOR, fg="white")
        self.score_label.grid(column=1, row=0)

        self.question_canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.question_canvas.create_text(150, 125, text="", font=(
            'Arial', 15, "italic"), width=280)
        self.question_canvas.grid(column=0, row=1, columnspan=2, pady=20)

        false_img = PhotoImage(
            file=r'Day34_GUIQuizzApp/images/false.png')
        self.false_button = Button(
            image=false_img, highlightthickness=0, command=self.false_pressed)
        self.false_button.config(border=0)
        self.false_button.grid(column=1, row=2)

        true_img = PhotoImage(
            file=r'Day34_GUIQuizzApp/images/true.png')
        self.true_button = Button(
            image=true_img, highlightthickness=0, command=self.true_pressed)
        self.true_button.config(border=0)
        self.true_button.grid(column=0, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.question_canvas.config(background="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.question_canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.question_canvas.itemconfig(
                self.question_text, text="You've reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        is_right = self.quiz.check_answer(user_answer="True")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer(user_answer="False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right: bool):

        if is_right:
            self.question_canvas.config(background="green")
            self.score_label.config(text=f"Score: {self.quiz.score}", font=(
                'Arial', 12, "italic"), bg=THEME_COLOR, fg="white")

        else:
            self.question_canvas.config(background="red")
        self.window.after(
            1000, self.get_next_question)
