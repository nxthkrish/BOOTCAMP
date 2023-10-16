import tkinter as tk
import random
import requests

class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Game")
        self.word_to_guess = ""
        self.guesses = []
        self.attempts = 6

        # Fetch a random word from the internet using an API
        self.get_random_word()

        # Load hangman images
        self.hangman_images = [tk.PhotoImage(file=f"hangman{i}.gif") for i in range(self.attempts, -1, -1)]
        self.hangman_image = tk.Label(root, image=self.hangman_images[self.attempts])
        self.hangman_image.grid(row=0, column=0, columnspan=6)

        # Create and display the word to guess
        self.word_display = tk.Label(root, text=self.display_word(), font=("Helvetica", 24))
        self.word_display.grid(row=1, column=0, columnspan=6)

        # Create buttons for letters
        self.letter_buttons = []
        for letter in "abcdefghijklmnopqrstuvwxyz":
            button = tk.Button(root, text=letter, font=("Helvetica", 16), command=lambda l=letter: self.guess_letter(l))
            self.letter_buttons.append(button)

        row, col = 2, 0
        for button in self.letter_buttons:
            button.grid(row=row, column=col)
            col += 1
            if col > 5:
                col = 0
                row += 1

    def get_random_word(self):
        try:
            response = requests.get("https://random-word-api.herokuapp.com/word?number=1")
            if response.status_code == 200:
                self.word_to_guess = random.choice(response.json())
            else:
                self.word_to_guess = "hangman"
        except Exception:
            self.word_to_guess = "hangman"

    def display_word(self):
        display = ""
        for letter in self.word_to_guess:
            if letter in self.guesses:
                display += letter
            else:
                display += "_"
        return display

    def guess_letter(self, letter):
        if letter not in self.guesses:
            self.guesses.append(letter)
            self.update_display()

            if letter not in self.word_to_guess:
                self.attempts -= 1
                self.update_attempts()

            if self.attempts == 0:
                self.end_game(False)
            elif set(self.word_to_guess) <= set(self.guesses):
                self.end_game(True)

    def update_display(self):
        self.word_display.config(text=self.display_word())

    def update_attempts(self):
        self.hangman_image.config(image=self.hangman_images[self.attempts])

    def end_game(self, is_winner):
        for button in self.letter_buttons:
            button.config(state=tk.DISABLED)
        if is_winner:
            result_label.config(text=f"You win! The word was: {self.word_to_guess}")
        else:
            result_label.config(text=f"You lose. The word was: {self.word_to_guess}")

root = tk.Tk()
hangman_game = HangmanGame(root)

# Create a label to display attempts left
result_label = tk.Label(root, text="", font=("Helvetica", 16))
result_label.grid(row=9, column=0, columnspan=6)

root.mainloop()

