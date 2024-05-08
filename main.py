print("Welcome to my first game!")
name = input("What is your name? ")
print("Hello", name, "Let's play a game...")
age = input("But first, tell me, what is your age? ")
if int(age) >= 18:
    print("You are old enough to play this game.")
    want_to_play = input("Do you want to play? ").lower()
    if want_to_play == "yes":
        print("Let's play!")
        left_or_right = input("First choice... Left or Right (left/right)? ").lower()
        if left_or_right == "left":
            print("It seems you chose the left!")
        else: 
            print("It seems you chose the right!")
    else:
        print("Okay, maybe next time.")