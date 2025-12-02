import random

words = ['python', 'javascript', 'java', 'automation', 'pytest', 'guvi', 'selenium']

# Pick a random word
word = random.choice(words)

# Scramble the word
scrambled = ''.join(random.sample(word, len(word)))
print("Unscramble this word:", scrambled)

# Player guess
guess = input("Your guess: ")

# Check answer
if guess == word:
    print("Correct!")
else:
    print("Wrong guess. Try again!\n")
    guess = input("Your guess: ")