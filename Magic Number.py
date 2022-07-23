
secret_number = 15

while True:
    number = int(input("Guess the magic number: "))
    if number != secret_number:
        print("Ha ha! You're stuck in my loop!")
    else:
        print("Well done, muggle! You are free now.")
        break