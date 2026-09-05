# Hangman Game 
import random
lists= ["apple","cricket","sachin","robot","ai"]
list= random.choice(lists)

Guess_letter = []

wrong_guess = 0
Max_wrong_guess = 6

print("Welcome to Hangman Game")
print("guess the word one letter at a time")
print("maximum 6 incorrect guess")

display = ["_"]*len(list)

while wrong_guess < Max_wrong_guess and "_" in display: 
    print("\nWord:", " ".join(display))
    print("Guessed letters:", " ".join(Guess_letter))
    print("Incorrect guesses:", wrong_guess, "/", Max_wrong_guess)

    guess=input("enter a letter: ").lower()

    if len(guess) !=1 or not guess.isalpha:
        print("Enter only one letter") 
        continue
    if guess in Guess_letter:
        print("this is a correct guess")
        continue
    Guess_letter.append(guess)

    if guess in list:
        print("correct guess ")

        for i in range(len(list)):
            if list[i]==guess:
                display[i]=guess
    else:
        wrong_guess+=1
        print("wrong guess") 


if "_" not in display:
    print("\nCongratulations! You guessed the word:", list)
else:
    print("\n Game Over!")
    print("The word was:", list)          