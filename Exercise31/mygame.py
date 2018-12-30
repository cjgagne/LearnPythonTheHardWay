print("""You have Sunday afternoon off.  What will you do?
1. Study python
2. Work in garden
3. Take a nap
""")

afternoon_choice = input("> ")

if afternoon_choice == "1":
    print("""Good choice!  You get to keep your job! 
    What will you study next?
    1. Learn Python the Hard Way
    2. Data Science Visualization
    3. Pluralsigtht video
    """)
    
    study_choice = input("> ")

    if study_choice == "1":
        print("""This is tedious, but you said you would do it.  
        You get to keep your job.""")
    elif study_choice == "2":
        print("""You would like that, but then your new boss 
        will think you lied to him.  You don't get to keep your job.""")
    else:
        print("""Bad choice, but better.  You will still have to finish 
        the book.""")

elif afternoon_choice == "2":
    print("""Bad choice!  You lose your job.
    What do you work on in your garden?
    1.  Clean out tomato and basil plants and plant lettuces.
    2.  Build new garden.
    3.  Prune fruit trees.
    """)

    garden_choice = input("> ")
    
    if garden_choice == "1":
        print("Good choice!  You can still eat salad even though you don't have a job.")
    elif garden_choice == "2":
        print("Bad choice, you have no job, so you have no money for supplies.")
    else: 
        print("Good choice! At least you will have summer fruit even though you have no job.")

else:
    print("Mediocre choice, but at least you are refreshed and not a crab.")
