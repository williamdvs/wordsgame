import random

def create_word():
    cwords=["avocado", "blackberry", "cheesecake", "doughnut","eggplant"]
    cword=(cwords[random.randint(0,4)])
    cword=list(cword)
    return cword

def create_puzzle(size):
    puzzle=[]
    for i in range (0, size):
        puzzle.append('_')
    return list(puzzle)

def play_game():
    playing = True
    strikes = 0
    print ("welcome to the game", )

def compare(word,puzzle,letter):
    for i in range(0,len(word)):
        if word[i]==letter:
            puzzle[i]=letter
    return puzzle

def striker(word,letter):
    is_strike = 1
    for i in range(0,len(word)):
        if word[i]==letter:
            is_strike=0
    return is_strike

def get_letter():
    letter=input()
    return letter

def solved(puzzle):
    is_solved= False
    r=0
    a=0
    for i in range(0,len(puzzle)):
        if puzzle[i] != "_":
            r+=1
    a=len(puzzle)-r
    if a==0:
        is_solved = True
    return is_solved

def play_game():
        print("Welcome to the game")
        word=create_word()
        puzzle=create_puzzle(len(word))
        playing = True
        strikes=0
        while(playing):
            #print(word)
            print("strikes=",strikes)
            print(puzzle)
            letter = get_letter()
            puzzle = compare(word,puzzle,letter)
            is_strike = striker(word,letter)
            strikes = strikes+is_strike

            if strikes>=3:
                print("strikes=",strikes)
                print(word)
                print("game over, you lose")
                playing = False

            is_solved = solved(puzzle)

            if is_solved == True:
                print(puzzle)
                print("game over, you win")
                playing = False

play_game()
