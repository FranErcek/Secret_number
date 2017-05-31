secret_number = 18

guess = int(raw_input("Guess the secret number between 1 and 36: "))

if guess == secret_number:
    print "YOU WIN, it's number 18! "
else:
    print "You Lose! Better luck next time!!! "