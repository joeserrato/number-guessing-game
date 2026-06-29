import random
print('''Welcome to the Number Guessing!
You have 7 chances to guess the number. Let's start!''')

low = int(input("Enter the Lower Bound: ")) 
high = int(input("Enter the Upper Bound: "))

computer = random.randint(low,high) 
guesses = 0
x = 0
chanches = 7

while (x < chanches):
    guesses +=1
    user = int(input("Enter your guess: "))
    if (user == computer):
        print("Your Correct")
        break
    elif (user > computer):
        print("Too HIGH")
    elif (user < computer):
        print("Too LOW")
    x += 1


print(f'Total Guesses: {guesses}')
print(f'Computer: {computer}, You: {user}')