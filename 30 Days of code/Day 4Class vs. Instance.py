class Person:
    def __init__(self,initialAge):
        global age
        # Add some more code to run some checks on initialAge
        assert 1 <= t <= 4
        assert -5 <= initialAge <= 30
        if initialAge >= 0:
            age = initialAge
        else:
            age = 0
            print("Age is not valid, setting age to 0.")

    def amIOld(self):
        global age
        # Do some computations in here and print out the correct statement to the console
        if age < 13:
            print("You are young.")
            pass
        elif 13 <= age < 18:
            print("You are a teenager.")
            pass
        else:
            print("You are old.")
            pass


    def yearPasses(self):
        global age
        age += 1 

        # Increment the age of the person in here

t = int(input())
for i in range(0, t):
    age = int(input())         
    p = Person(age)  
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()       
    p.amIOld()
    print("")