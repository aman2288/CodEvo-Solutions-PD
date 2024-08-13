import random
n = random.randint(1,100) # you can chaange the range  to any numbers
guesses = 0
maxx_limit = 10 # you can change the limit by yourself to make it hard or easy
while(guesses < maxx_limit):
        a = int(input("Enter the number:"))
        guesses += 1
        if(a == n):
            print(f"Congratulations! you gussed the correct number {n} in {guesses} attempts")
            break;

        elif(a>n):
            print("Try Again! You guessed too high")
       
        elif(a<n):
            print("Try Again! You guessed too small")
         
else:
     a = "better luck next time!"
     print(a.title())
        
    
