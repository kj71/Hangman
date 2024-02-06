import random
import stages

words = ["anaconda", "baboon", "camel"]
chosen_word = random.choice(words)

display = ['_'] * len(chosen_word)
lives = 6

while True:
    guess = input("Enter a letter: ")
    if guess not in chosen_word:
        print(stages.stages[lives])
        lives -= 1

    else:
        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                display[i] = guess

    print(display)

    if lives == -1:
        print("You lose!")
        break

    if '_' not in display:
        print("You win!")
        break
