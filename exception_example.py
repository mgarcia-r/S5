name=input("what is your name?")
#In a simpler way
age2=input(f"How old are you {name}?")
try:
    age2=int(age2) #here there can be a problem
    print(f"{name}, you were born in {2024-age2}")
except ValueError:
    print("please enter a valid value for age")
    print("I can also print this in case of error that I prevented")
except ZeroDivisionError:
    print("you cannot divide by 0")
except:
    print("this is another type of error")
else: #for no exceptions
    print("thank you for playing as expected")
finally: #executed no matter what at the very end
    print("thanks for playing the game")
