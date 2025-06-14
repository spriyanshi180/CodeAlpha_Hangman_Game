import random

# Predefined list of words
word_list = ["lichee", "banana", "papaya", "orange", "cherry"]

# Randomly choose a word
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Game setup
display = ["_"] * word_length
guessed_letters = []
lives = 6

print("🎮 Welcome to Hangman! 🎮")
print("Guess the word: ", " ".join(display))

# Game loop
while lives > 0 and "_" in display:
    guess = input("\nGuess a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("❌ Please enter a single alphabetic character.")
        continue

    if guess in guessed_letters:
        print(f"🔁 You already guessed '{guess}'. Try a different letter.")
        continue

    guessed_letters.append(guess)

    if guess in chosen_word:
        for i in range(word_length):
            if chosen_word[i] == guess:
                display[i] = guess
        print("✅ Good guess!")
    
    else:
        lives -= 1
        print(f"❌ Wrong guess. You have {lives} lives left.")

    print("Word: ", " ".join(display))

# End game
if "_" not in display:
    print("\n🎉 Congratulations! You guessed the word:", chosen_word)
else:
    print("\n💀 Game Over! The correct word was:", chosen_word)