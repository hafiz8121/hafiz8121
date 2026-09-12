import tkinter as tk
from tkinter import messagebox
from datetime import date

# ------------------------------------------------------------
# "Figure Out the Date" mudincha kandu pudi
# The hidden answer is 16 September 2026.DONT LOOK AT THE CODE shushhh.
# ------------------------------------------------------------

ANSWER = date(2026, 9, 16)
MAX_ATTEMPTS = 5

BG = "#eef2f7"
CARD = "#ffffff"
TEXT = "#111827"
MUTED = "#667085"
BLUE = "#2f63d8"
GREEN = "#1f9d68"
RED = "#d64545"


class DateMystery:
    def __init__(self, root):
        self.root = root
        self.root.title("✈️ Figure Out the Date")
        self.root.geometry("520x690")
        self.root.resizable(False, False)
        self.root.configure(bg=BG)

        self.attempts = 0
        self.clue_index = 0

        self.build_ui()

    def build_ui(self):
        # Header
        tk.Label(
            self.root,
            text="✈️  THE DATE MYSTERY",
            font=("Arial", 24, "bold"),
            bg=BG,
            fg=TEXT
        ).pack(pady=(28, 4))

        tk.Label(
            self.root,
            text="Someone is coming to meet you...",
            font=("Arial", 13),
            bg=BG,
            fg=MUTED
        ).pack()

        # Main card
        card = tk.Frame(self.root, bg=CARD, highlightthickness=1,
                        highlightbackground="#d8dee8")
        card.pack(padx=28, pady=24, fill="both", expand=True)

        tk.Label(
            card,
            text="🕵️ Can you figure out the date?",
            font=("Arial", 19, "bold"),
            bg=CARD,
            fg=TEXT
        ).pack(pady=(28, 8))

        tk.Label(
            card,
            text="Read the clues, then enter your best guess.",
            font=("Arial", 11),
            bg=CARD,
            fg=MUTED
        ).pack()

        self.clue_label = tk.Label(
            card,
            text="🔎 CLUE 1\nThe trip starts in September 2026.",
            font=("Arial", 13),
            bg="#f5f7fb",
            fg=TEXT,
            justify="center",
            wraplength=390,
            padx=20,
            pady=18
        )
        self.clue_label.pack(padx=28, pady=24, fill="x")

        # Date selectors
        selector = tk.Frame(card, bg=CARD)
        selector.pack(pady=4)

        tk.Label(selector, text="Day", font=("Arial", 10, "bold"),
                 bg=CARD, fg=MUTED).grid(row=0, column=0, padx=5)

        tk.Label(selector, text="Month", font=("Arial", 10, "bold"),
                 bg=CARD, fg=MUTED).grid(row=0, column=1, padx=5)

        tk.Label(selector, text="Year", font=("Arial", 10, "bold"),
                 bg=CARD, fg=MUTED).grid(row=0, column=2, padx=5)

        self.day = tk.Spinbox(selector, from_=1, to=31, width=5,
                              font=("Arial", 14), justify="center")
        self.day.grid(row=1, column=0, padx=5, pady=5)

        self.month = tk.StringVar(value="September")
        tk.OptionMenu(
            selector, self.month,
            "January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December"
        ).grid(row=1, column=1, padx=5, pady=5)

        self.year = tk.Spinbox(selector, from_=2026, to=2030, width=6,
                               font=("Arial", 14), justify="center")
        self.year.grid(row=1, column=2, padx=5, pady=5)

        self.result = tk.Label(
            card,
            text="",
            font=("Arial", 12, "bold"),
            bg=CARD,
            fg=TEXT,
            wraplength=400
        )
        self.result.pack(pady=(15, 6))

        self.attempt_label = tk.Label(
            card,
            text=f"Guesses left: {MAX_ATTEMPTS}",
            font=("Arial", 10),
            bg=CARD,
            fg=MUTED
        )
        self.attempt_label.pack()

        self.guess_button = tk.Button(
            card,
            text="🔐 LOCK IN MY GUESS",
            command=self.check_guess,
            font=("Arial", 12, "bold"),
            bg=BLUE,
            fg="white",
            activebackground="#244fae",
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            padx=22,
            pady=12
        )
        self.guess_button.pack(pady=18)

        self.clue_button = tk.Button(
            card,
            text="💡 Give me another clue",
            command=self.next_clue,
            font=("Arial", 10, "bold"),
            bg="#edf2ff",
            fg=BLUE,
            relief="flat",
            cursor="hand2",
            padx=15,
            pady=8
        )
        self.clue_button.pack()

        tk.Label(
            card,
            text="Based on the travel details in the screenshot ✈️",
            font=("Arial", 9),
            bg=CARD,
            fg="#98a2b3"
        ).pack(side="bottom", pady=18)

    def next_clue(self):
        clues = [
            "🔎 CLUE 2\nThe first flight shown leaves Malmö on Wednesday.",
            "🔎 CLUE 3\nThe trip card says: Wed, 16 Sep → Sat, 19 Sep.",
            "🔎 CLUE 4\nThe outbound flight is MMX → STN and leaves at 10:25.",
            "🔎 FINAL CLUE\nLook closely at the heading: the trip starts on 16 September 2026."
        ]

        if self.clue_index < len(clues):
            self.clue_label.config(text=clues[self.clue_index])
            self.clue_index += 1
        else:
            self.clue_label.config(text="🎯 You have all the clues!\nWhat date are you guessing?")

    def check_guess(self):
        try:
            guessed_day = int(self.day.get())
            guessed_month = list(self.month_options()).index(self.month.get()) + 1
            guessed_year = int(self.year.get())
            guess = date(guessed_year, guessed_month, guessed_day)
        except ValueError:
            messagebox.showerror("Oops!", "That isn't a valid date.")
            return

        self.attempts += 1
        left = MAX_ATTEMPTS - self.attempts
        self.attempt_label.config(text=f"Guesses left: {max(left, 0)}")

        if guess == ANSWER:
            self.result.config(
                text="🎉 YOU GOT IT!\n\n16 September 2026 ✈️\n\n"
                     "That's the date the trip starts.",
                fg=GREEN
            )
            self.guess_button.config(state="disabled")
            self.clue_button.config(state="disabled")
            return

        if self.attempts >= MAX_ATTEMPTS:
            self.result.config(
                text="✨ Mystery solved!\n\nThe date is 16 September 2026.",
                fg=BLUE
            )
            self.guess_button.config(state="disabled")
            self.clue_button.config(state="disabled")
            return

        if guess < ANSWER:
            hint = "You're a little too early 👀"
        else:
            hint = "You're a little too late 👀"

        self.result.config(
            text=f"Not quite! {hint}\nTry again...",
            fg=RED
        )

    @staticmethod
    def month_options():
        return (
            "January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December"
        )


if __name__ == "__main__":
    root = tk.Tk()
    DateMystery(root)
    root.mainloop()