import cards

def ask_yes_no(question):
    """asks yes or no question
    use by calling ask_yes_no() and pass in a question
            ask_yes_no(question)
    takes a y or n input from user
    """
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
    return response

def ask_number(question, low, high):
    """asks for a number 0-8 from user
    call using ask_number()
            ask_number()
    """
    response = None
    while True:
        try:
            response = int(input(question))
            if response in range(low, high):
                return response
            else:
                print("Out of range")
        except:
            print("Thats not a number")


def roll():
    import random

    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    print('You rolled a', die1, "and", die2)
    roll = die1 + die2
    return roll

def switch_turn(num_players, turn):
    turn = turn
    if turn < num_players - 1:
        turn += 1
    else:
        turn = 0
    return turn

def winner_grats(winner):
    print("Congratulations,",winner,"is victorious!")
    print("They are the greatest player!")

def add_to_score(score, points):
    """Adds points to score"""
    new_score = score
    score += points
    return new_score

class Player(object):
    def __init__(self,name, score = 0):
        self.name = name
        self.score = score
    def __str__(self):
        rep = self.name
        rep = rep + " " + str(self.score)
        return rep

if __name__ == "__main__":
    print("You ran this module directly (not imported)")
    input("press enter to exit")
