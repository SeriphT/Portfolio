import random

win = 0
mHealth = 100
pHealth = 100
choice = input("Attack or Run: ")

while choice == "attack":
    print("Input player attack quote")
    pDamage = random.randrange(0, 50)
    mDamage = random.randrange(0,55)
    mHealth -= pDamage
    if mHealth > 0:
        print("Input monster attack quote")
        pHealth -=  mDamage
    if pHealth <= 0:
        print("You have died.")
        win = 0
        break
    elif mHealth <= 0:
        print("The monster died")
        win += 1
        break
    else:
        print("Player HP:",pHealth)
        print("Monster HP:",mHealth)
        choice = input("Attack or Run: ")

if choice == "run":
    print("You ran away safely")
if win == 0:
    print("game over")
else:
    print("You defeated the monster")   
    print("Player HP:",pHealth)
