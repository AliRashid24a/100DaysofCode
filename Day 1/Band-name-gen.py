# Day 1 - Band name generator
# Goal is to create a simple console application which asks the user a couple questions and then turns the answer of
# those questions into a band name.
# Proficencies: String manipluaiton, user input,

name_generated = False
while (name_generated != True):
    ans1 = input("Welcome to the Band Name Generator.\nWhat is your favorite fruit?\n")
    ans2 = input("If you could pick one thing to take to an island what would it be?\n")
    print("Here is your new band name!\n" + ans1 + " " + ans2)
    cont = input("\nWould you like to generate another band name?\n").lower()
    if cont == "no":
        print("Thank you!")
        name_generated = True
    else:
        pass

