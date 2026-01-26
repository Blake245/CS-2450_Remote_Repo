import random
print("Hello my name is bobby and I'm going to guess your age.")
name_input = input("What is your name?")

while True:
    guess = random.randint(15, 30)
    guess_input = input("Is your age " + str(guess) + " ")
    lower_str = guess_input.lower()
    if lower_str == "y" or lower_str == "yes":
        print(name_input + " is " + str(guess) + "!!!")
        print("Goodbye.")
        break
    elif lower_str == "n" or lower_str == "no":
        print("Rats!")
    else:
        print("Please use y or n for your answer.")