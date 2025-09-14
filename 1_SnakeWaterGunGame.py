#Creating a snake water gun game in python

'''
1 --> Snake
2--> Water
3-->Gun

'''

import random

computer = random.randint(1, 3)

print("==== SNAKE WATER GUN GAME ====")

user = input("Enter your choice (s for Snake, w for Water, g for Gun): ")

youDict = {"s": 1, "w": 2, "g": 3}
reverseDict = {1: "Snake", 2: "Water", 3: "Gun"}

if user not in youDict:
    print("Invalid choice! Please enter s/w/g.")
else:
    user_choice = youDict[user]

    print(f"You choose : {reverseDict[user_choice]}")
    print(f"Computer chooses : {reverseDict[computer]}")

    match (user_choice, computer):
        case (u, c) if u == c:
            print("It's a TIE!")
        case (1, 2) | (2, 3) | (3, 1):
            print("✅ You win!!")
        case (2, 1) | (3, 2) | (1, 3):
            print("❌ Computer wins!!")
