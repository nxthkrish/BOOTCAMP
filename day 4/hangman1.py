import tkinter as tk
from random import choice

# List of words for the game
word_list = ["python", "hangman", "programming", "computer", "code"]

class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Game")

        # Initialize the game variables
        self.word_to_guess = choice(word_list)
        self.guesses = []
        self.max_attempts = 6

        # Create and display the word to guess
        self.word_display = tk.Label(root, text=self.display_word(), font="Helvetica 24")
        self.word_display.pack()

        # Create buttons for letters
        self.letter_buttons = []
        for letter in "abcdefghijklmnopqrstuvwxyz":
            button = tk.Button(root, text=letter, font="Helvetica 16", command=lambda l=letter: self.guess_letter(l))
            self.letter_buttons.append(button)
            button.pack(side=tk.LEFT)

    def display_word(self):
        # Display the word with guessed letters, hiding unguessed letters with underscores
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
                self.max_attempts -= 1
                self.update_attempts()

            if self.max_attempts == 0:
                self.end_game(False)
            elif set(self.word_to_guess) <= set(self.guesses):
                self.end_game(True)

    def update_display(self):
        self.word_display.config(text=self.display_word())

    def update_attempts(self):
        attempts_label.config(text=f"Attempts left: {self.max_attempts}")

    def end_game(self, is_winner):
        for button in self.letter_buttons:
            button.config(state=tk.DISABLED)
        if is_winner:
            result_label.config(text="You win! The word was: " + self.word_to_guess)
        else:
            result_label.config(text="You lose. The word was: " + self.word_to_guess)

root = tk.Tk()
hangman_game = HangmanGame(root)

# Create a label to display attempts left
attempts_label = tk.Label(root, text=f"Attempts left: {hangman_game.max_attempts}", font="Helvetica 16")
attempts_label.pack()

# Create a label to display game result
result_label = tk.Label(root, text="", font="Helvetica 16")
result_label.pack()

root.mainloop()
