import random

# set what characters or symbols we want in each password
char = "abcefghijklmnopqrstuvwyxv"

# Create a while loop and ask the user how long they would like their password and how many passwords they want to create
while 1:
    Pass_length = int(input("What length would you like the password to be?"))
    Pass_count = int(input("How many passwords would you like to generate?"))

# use the "for" to indicate that the loop will iterate until the input given as the password count and passwrod length
    for x in range (0,Pass_count):
        password = ""
        for x in range (0,Pass_length):
# use "random.choice()" to indicate that the variable password characters will be randomized in the parameters for characters we set before
            Pass_char = random.choice(char)
# if we add the password we want to be generated with the set of password characters that is randomized then we will have an outcome
            password    = password + Pass_char
        print(password)

