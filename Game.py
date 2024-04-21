import random
RPS = ['r', 'p', 's']
def points():
    value = int(input("Enter for how many points you want to play this game: "))
    return value
def user():
    choice = input("Enter your choice rock, paper, scissors: ").lower()
    while choice not in RPS:
        print("You chosed an invalid option")
        choice = input("Enter you choice in rock or paper or scissors: ").lower()
    
    return choice

def computer():
    choice = random.choice(RPS)
    return choice

def play():
    print("Instructions to play this game: ")
    print("Enter 'R' or 'r' to choose Rock")
    print("Enter 'P' or 'p' to choose Paper")
    print("Enter 'S' or 's' to choose Scissors")
    Up = 0
    Cp = 0
    P = points()
    while Up!=P and Cp != P:
        U = user()
        C = computer()
        print('Computer choosen: ', C)
        if (
        (U == 'r' and C == 's') or
        (U == 'p' and C == 'r') or
        (U == 's' and C == 'p')
        ):
            Up += 1
            print('You won a point')
        elif (U==C):
            print('No one got a point')
        else:
            Cp += 1
            print('Computer won a point')
        print(f"points - Computer: {Cp}, Your points: {Up}")
    if Up == P:
        print('You Won!..')
    else:
        print('Computer Won')


if __name__ == "__main__":
    play()