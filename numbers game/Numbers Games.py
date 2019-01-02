import random, time
def main():
    menu()

def menu():
    choice = 0
    while choice == 0:
        print(" 1. Guess the Number\n2. Pick the Number\n3. Credits")
        choice = int(input("enter your choice"))
        if choice == 1:
            print("Guess The Number")
            guess()
            
        elif choice == 2:
            print("Pick The Number")
            Pick()
              
        elif choice == 3:
            print("Credits")
            Credits()
        else:
              print("Invalid choice.")
              menu()



#starts the program
def guess():
   	print("you are playing guess the number \n  \n  \n")
   	guessnum()
# gets random number
def guessnum():
   	num = random.randrange(1, 100)
   	num = str(num)
   	guesscheck(num)
#handles the guessing
def guesscheck(num):
    print("guess a number between 1 and 100")
    guessnumber = 0
    while guessnumber <= 5:
                    print("you are at guess",guessnumber)
                    guess = input()
                    if guess.isdigit():
                        if guess == num:
                            guessnumber += 1
                            win(guess)
                            break
                        elif guess < num:
                            print("higher")
                            guessnumber += 1
                        elif guess > num:
                            print("lower")
                            guessnumber += 1
                        else:
                            print("invalid")
                    else:
                        print("invalid")
                    
    if guessnumber == 5:
        lose()


def Pick():
    answer = int(input("Pick a number from 1 - 100.\nThe computer will guess the number"))

    attempt = 5
    x = 1
    y = 100
    guess = random.randrange(x,y)
    
    while attempt > 0:

        if guess == answer:
           win(guess)
        elif guess > answer:
            print("Lower")
            print(guess)
            time.sleep(1)
            attempt -= 1
            y = guess
            guess = random.randrange(x,y)
        elif guess < answer:
            print("Higher")
            print(guess)
            time.sleep(1)
            attempt -= 1
            x = guess
            guess = random.randrange(x,y)

    if attempt == 0 and guess != answer:
        print("You win. Computer loses. Your number:",answer, "Computer final guess:",guess)
    else:
        win(guess)
def Credits():
    print("Dreidits")

def win(guess):
    print("Guess is correct. Final Guess:",guess)
    input("Press enter to exit")
    quit()
#take you back to the menu after loss
def lose():
   	print("you lost the game hit enter to go back to the menu")
   	input()
            
main()
