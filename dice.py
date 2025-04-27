import random

def main():
    # Roll two dice, three times
    for i in range(3):
        die1 = random.randint(1, 6)  # Roll first die
        die2 = random.randint(1, 6)  # Roll second die
        print("Roll", i + 1, ": Die 1 =", die1, "Die 2 =", die2)

# This provided line is required at the end of the Python file
if __name__ == '__main__':
    main()
