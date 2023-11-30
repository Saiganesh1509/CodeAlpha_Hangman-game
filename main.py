import tkinter as tk
from tkinter import messagebox
import random

class HangmanGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Hangman Game by Sai Ganesh")

        self.word_list = ["python", "hangman", "program", "computer", "Sai Ganesh", "developer", "CodeAlpha", "Internship"]
        self.word = random.choice(self.word_list).lower()
        self.guesses = set()
        self.max_attempts = 8
        self.attempts_left = self.max_attempts

        self.create_widgets()

    def create_widgets(self):
        self.word_display = tk.Label(self.master, text=self.display_word(), font=("Helvetica", 34), height=2)
        self.word_display.pack(pady=10)

        self.guess_label = tk.Label(self.master, text="Enter a letter:")
        self.guess_label.pack()

        self.guess_entry = tk.Entry(self.master, width=25,)
        self.guess_entry.pack()
        self.guess_entry.pack()

        self.guess_button = tk.Button(self.master, text="Guess", command=self.make_guess, background="#29C5F6", )
        self.guess_button.pack(pady=10)

        self.attempts_label = tk.Label(self.master, text=f"Attempts left: {self.attempts_left}")
        self.attempts_label.pack()

    def display_word(self):
        return " ".join(letter if letter in self.guesses else "_" for letter in self.word)

    def make_guess(self):
        guess = self.guess_entry.get().lower()
        if guess.isalpha() and len(guess) == 1:
            if guess in self.guesses:
                messagebox.showinfo("Hangman", "You already guessed that letter.")
            else:
                self.guesses.add(guess)
                if guess not in self.word:
                    self.attempts_left -= 1

                self.update_display()

                if "_" not in self.display_word():
                    messagebox.showinfo("Hangman", "Congratulations! You guessed the word.")
                    self.reset_game()

                elif self.attempts_left == 0:
                    messagebox.showinfo("Hangman", f"Game over. The word was '{self.word}'.")
                    self.reset_game()

        else:
            messagebox.showwarning("Hangman", "Please enter a valid single letter.")

    def update_display(self):
        self.word_display.config(text=self.display_word())
        self.attempts_label.config(text=f"Attempts left: {self.attempts_left}")

    def reset_game(self):
        self.word = random.choice(self.word_list).lower()
        self.guesses.clear()
        self.attempts_left = self.max_attempts
        self.update_display()


if __name__ == "__main__":
    root = tk.Tk()
    hangman_game = HangmanGame(root)
    root.mainloop()
