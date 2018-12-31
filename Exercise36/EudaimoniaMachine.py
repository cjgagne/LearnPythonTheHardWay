from sys import exit

class EudaimoniaMachine:

    def __init__(self):
        print("""Welcome to the Eudaimonia Machine!
        Please enter the password to enter: """)

        enter = False
        while not enter:
            password = input("> ")

            if password.capitalize()  == "Please":
                self.gallery()
                enter = True
            else:
                print("Wrong, try again.")


    def gallery(self):
        print("""Welcome to the gallery.  On the walls
        you will find examples of great work.  Name
        a great physicist to move to the next room.""")

        enter = False
        while not enter:
            physicist = input("> ")
     
            great_physicists = ["Einstein", "Newton", "Heisenberg", "Maxwell"]

            if physicist in great_physicists:
                print("Good choice!")
                self.salon()
            elif physicist == "Carmen Gagne":
                print("Suck up!  Ok, you are in.")
                self.salon()
            else:
               print("Wrong, try again.  Maybe you should read a book.")
            
    def salon(self):
        print("""Welcome to the salon.  Help yourself to some
        coffee.  To proceed, how does the captain like his coffee?""")

        enter = False
        while not enter:
            coffee = input("> ")
     
            if "bold" in coffee:
                print("Of course!")
                self.library()
            elif "sassy" == coffee:
                print("Right you are!")
                self.library()
            else:
               print("Wrong, try again.  What a terrible suck up!")
            
    def library(self):
        print("""Welcome to the library.  Here's where you read that book.  
        To proceed, what is Carmen's favorite book?""")

        book = input("> ")

        if "Atlas" in book and "Shrugged" in book:
            print("You got that right!")
            self.office()
        else:
            print("Wrong, try again.  What a terrible suck up!")
            self.library()

    def office(self):
        print("""Welcome to the office.  Here's where tedious work like
        this is done.  To proceed, name this book?""")

        book = input("> ")

        if book == "Learn Python the Hard Way":
            print("Yep. Now you get to do some real work!")
            self.chambers()
        else:
            print("Wrong, try again.  Aren't you paying attention at all?")
            self.office()

    def chambers(self):
        print("You won!!!!")
        exit(0)


if __name__ == "__main__":
    EudaimoniaMachine()
