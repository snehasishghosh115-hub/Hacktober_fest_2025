import random

print("🏴‍☠️ WELCOME TO THE TREASURE HUNT GAME 🏴‍☠️")
print("Find the hidden treasure in a 5x5 grid!")
print("You’ll get clues like Hot / Cold based on how close you are.\n")
size = 5
treasure_x = random.randint(1, size)
treasure_y = random.randint(1, size)

attempts = 0

while True:
    try:
        x = int(input("Enter row (1-5): "))
        y = int(input("Enter column (1-5): "))
    except ValueError:
        print(" Please enter valid numbers!")
        continue

    if not (1 <= x <= size and 1 <= y <= size):
        print("Stay inside the map! (1–5 only)")
        continue

    attempts += 1

    distance = abs(treasure_x - x) + abs(treasure_y - y)

    if distance == 0:
        print(f"\n You found the treasure in {attempts} attempts!")
        print(" Congratulations, Pirate! ")
        break
    elif distance == 1:
        print(" Very Hot! You're right next to it!")
    elif distance == 2:
        print(" Warm — getting closer!")
    elif distance <= 4:
        print(" Cold — still far away.")
    else:
        print(" Freezing Cold — nowhere near!")
