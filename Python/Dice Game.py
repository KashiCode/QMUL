import csv
import random


#Import data from a CSV file (names, usernames, passwords).

def LoginInfo():
    csvFile = open ('Credentials.csv')
    userInfo = (csvFile)
    userList = []
    heading = True
    for row in userInfo:
        if heading == False:
            user=row.strip().split(",")
            heading = ['Name','Username','Password']
            data = zip(heading,user)
            userDataDict = dict (data)
            userList.append(userDataDict)
        heading = False
    csvFile.close()
    return (userList)

def LoginInfo2():
    userList = LoginInfo()
    print(userList)
    return (userList)

#process of logging a user in.

def Login():
    loggedIn = False
    while loggedIn == False:
        userList = LoginInfo()
        username = input("What is your username?")
        password = input("What is your password?")
        username = username.lower()
        for item in userList:
            if item['Username'] == username and item['Password'] == password and username:
                name = item['Name']
                loggedIn = True
                print('------you are now logged in------')
        if loggedIn == False:
            print("the entered username or password doesn't exist.")       
    return(name,username)
    


#the actual rolling of the dice

def rollDice(name):
    diceOne = random.randint(1,6)
    print(name,"rolled a", diceOne)
    diceTwo = random.randint(1,6)
    print(name,"rolled a", diceTwo)
    if diceOne == diceTwo:
        print(name,"rolled a double, so they get to roll again")
        diceThree = random.randint(1,6)
        print(name,"rolled a", diceThree)
        total = diceOne + diceTwo + diceThree
    else:
        total = diceOne + diceTwo
    print(name,"finished this round with a total roll of", total)
    return total

# rules for the score from def diceroll 

def rules(name):
    roundScore = rollDice(name)
    if roundScore % 2 == 0:
        roundScore = roundScore + 10
    else:
        roundScore = roundScore - 5
    if roundScore < 0:
        roundScore = 0
    return roundScore

# Total scores adds up the scores and decides who wins with the highest score.
# individual names for the players are assigned.
# 'winners' variables are assigned depending on who wins.

def totalscores():
    playerOneScore = 0
    playerTwoScore = 0
    playerOne= input('please enter name of player 1')
    playerTwo= input('please enter name of player 2')
    winner = False
    for count in range(1, 6):
        playerOneScore = playerOneScore + rules(playerOne)
        print(playerOne,"has a score of", playerOneScore)
        playerTwoScore = playerTwoScore + rules(playerTwo)
        print(playerTwo,"has a score of", playerTwoScore)
    if playerOneScore != playerTwoScore:
        winner = True
        if playerOneScore > playerTwoScore:
            WinnersScore = playerOneScore
            WinnersName = playerOne
            print(playerOne,"is the winner with a final score of", playerOneScore)
        else:
            WinnersScore = playerTwoScore
            WinnersName = playerTwo
            print(playerTwo,"is the winner with a final score of", playerTwoScore)
    else:
        while winner == False:
            print("You both scored the same ammount, so the highest dice roll wins")
            dice1 = random.randint(1,6)
            print(playerOne,"rolled a", dice1)
            dice2 = random.randint(1,6)
            print(playerTwo,"rolled a", dice2)
            if dice1 != dice2:
                winner = True
                if dice1 > dice2:
                    WinnersScore = playerOneScore
                    WinnersName = playerOne
                    print(playerOne,"won with a final score of", playerOneScore)
                else:
                    WinnersScore = playerTwoScore
                    WinnersName = playerTwo
                    print(playerTwo,"won with a final score of", playerTwoScore)
    return(WinnersName,WinnersScore)
                
                

# The scores are saved to a new CSV file or Exsisting one.
# Amended so if there is a 'csv file' already present the records wont be wiped.
                                
        
def saveData():
    try:
        fileHandle = open('Leaderboard.csv', 'r+')
        fileContent = fileHandle.read()
        if fileContent.strip()=='':
            fileHandle.write('Username,Score\n')
        for item in saveScore:
            fileHandle.write('{Username},{Score}'.format(**item))
            fileHandle.write('\n')
        fileHandle.close()
    except OSError:
        print('Can\'t write to file!')



def getSortKey(item):
    return item['Score']

def showscores():
    scoresData = open ('leaderboard.csv')
    scoresInfo = (scoresData)
    scoresList = []
    heading = True
    for row in scoresInfo:
        if heading == False:
            scores = row.strip().split(",")
            heading = ['Username','Score']
            data = zip(heading,scores)
            scoresDataDict =dict (data)
            scoresList.append(scoresDataDict)
        heading = False
    scoresData.close()
    scoresList.sort(key=getSortKey,reverse=True)
    print("-----Top Five Scores-----")
    for n in range (0,5):
        player = scoresList[n]
        print(n+1, ") ",player["Score"], player['Username'])

#Main Menu System

print("-------Welcome to Dice Game------- ")
instructions = ('This is a game for two users who roll 2 dice 5 times.\n If the total is even the player gains 10 points; if it is odd, they lose 5.\n If there is a draw after five rounds then both users will have to roll again to determine the winner.')
print("""
                      1: Play Dice game
                      2: View leaderboard
                      3: Instructions
                      4: View Credentials""")
userChoice = int(input("Please choose an option: "))
if userChoice == 1:
    LoginInfo()
    Login()
    WinnersName,WinnersScore = totalscores()
    saveScore = [{'Username':WinnersName,'Score':WinnersScore}]
    saveData()
    showscores()
elif userChoice == 2:
        showscores()
elif userChoice == 3:
            print(instructions)
elif userChoice == 4:
    LoginInfo2()
                
else:
    print('Invalid choice')
    




        
        
