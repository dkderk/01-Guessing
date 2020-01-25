import sys, random

assert sys.version_info >= (3,7), "This script requires at least Python 3.7"

quit = False
range = 50

while not quit:
    random_number = random.randint(1,range)
    count = 0
    number = -1
    while number != random_number:
        number = input("Please guess a number between 1 and {}: ".format(range))
        if not number.isdigit():
            print("Please guess a number!")
        else:
            number = int(number)
            print("Sorry that's not correct!")
            if number > random_number:
                print("Too High!")
            elif number < random_number:
                print("Too Low!")
            count = count + 1
    print("You have guessed correctly!")
    print("It took you {} attempts!".format(count))
    replay = input("Would you like to play again? (yes or no)?")
    replay = replay.lower()
    if replay == "yes" or replay == "y":
        dif = input("Would you like to increase the difficulty? (yes or no)")
        dif = dif.lower()
        if dif == "yes" or dif == "y":
            range += 50
            quit = False
        else:
            quit = False
    else:
        quit = True

print("\n\nThanks for playing my game! I hope you enjoyed it!")