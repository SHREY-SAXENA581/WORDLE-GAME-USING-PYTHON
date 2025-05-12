import random

class WordleGame:
    def __init__(self, word_list_file="words.txt"):
        self.words = self.load_words(word_list_file)
        self.word = random.choice(self.words)  # Random word selection
        self.attempts = 6  # Number of attempts allowed

    # Function to load words from the words file
    def load_words(self, file_path):
        with open(file_path, "r") as file:
            words = file.readlines()
        words = [word.strip().lower() for word in words]
        return words

    # Function to check if the guessed word is valid
    def is_valid_guess(self, guess):
        return len(guess) == len(self.word) and guess.isalpha()

    # Function to give feedback for the guess
    def give_feedback(self, guess):
        feedback = []
        for i in range(len(self.word)):
            if guess[i] == self.word[i]:
                feedback.append(f"{guess[i].upper()}")  # Correct letter in correct place
            elif guess[i] in self.word:
                feedback.append(f"{guess[i].lower()}")  # Correct letter in wrong place
            else:
                feedback.append("_")  # Incorrect letter
        return " ".join(feedback)

    # Function to play the game
    def play_game(self):
        print("Welcome to Wordle!")
        print("You have 6 attempts to guess the correct word.")
        print("Feedback will be given as follows:")
        print("Uppercase letter = Correct letter in the correct position.")
        print("Lowercase letter = Correct letter in the wrong position.")
        print("Underscore = Incorrect letter.")

        while self.attempts > 0:
            guess = input(f"Attempt {7 - self.attempts}: Enter your guess: ").lower()

            # Check if the guess is valid
            if not self.is_valid_guess(guess):
                print("Invalid guess. Please enter a valid 5-letter word.")
                continue

            # Give feedback
            feedback = self.give_feedback(guess)
            print(f"Feedback: {feedback}")

            if guess == self.word:
                print(f"Congratulations! You've guessed the word '{self.word}' correctly!")
                break
            else:
                self.attempts -= 1

            if self.attempts == 0:
                print(f"Sorry, you've run out of attempts. The correct word was '{self.word}'.")

# Main function to start the game
def main():
    game = WordleGame()  # Create a game instance
    game.play_game()  # Start the game

if __name__ == "__main__":
    main()  # Run the game
