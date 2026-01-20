import random
print("Hello my name is bobby and I'm going to guess your age.")
name_input = input("What is your name?")

while True:
    guess = random.randint(15, 30)
    guess_input = input("Is your age " + str(guess) + " ")
    if guess_input == "y":
        print(name_input + " is " + str(guess) + "!!!")
        print("Goodbye.")
        break
    elif guess_input == "n":
        print("Rats!")