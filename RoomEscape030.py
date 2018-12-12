# Text based game - Room Escsape!
# Start Date 12/10/2018

# imports
import time
import random
import math
from translateGM import translateDesc, translateMove

# Initialise Variables
loopGame = True
loopIntro = True
loopRoom = True
loopPlayAgain = True


# Functions

# Simplified Sleep
def slp(amt):
    time.sleep(amt-amt)

# Room importer
def importRoom(roomName):
    roomList = []
    for roomFileLine in open("rooms/" + roomName + "/" + roomName + ".txt"):
        roomList.append(roomFileLine.strip()) # Standard text to list for loop

    # Create list of individual elements
    roomElements = []
    for roomWidth in range(len(roomList)):
        roomSplitList = roomList[roomWidth].split(" ")
        for roomHeight in roomSplitList:
            roomElements.append(roomHeight)

    # Dimensions Calculator
    dimension = int(roomElements[len(roomElements) - 1])
    roomElements.pop(len(roomElements) - 1) # remove the dimensions from list

    # Room Converter
    hauntedHouse = {}
    for roomDimensionA in range(1, dimension + 1):
        for roomDimensionB in range(1, dimension + 1):
            hauntedHouse[roomDimensionA, roomDimensionB] = roomElements[(roomDimensionA - 1)*dimension + roomDimensionB - 1]
    return hauntedHouse

# Change Log importer
def importChangeLog():
    changeLog = []
    for changeLogLine in open("resources/changelog.txt"):
        changeLog.append(changeLogLine.strip())
    return changeLog

# Room Name Checker
def checkName(name):
    roomNameList = []
    for roomName in open("resources/roomNames.txt"):
        roomNameList.append(roomName.strip())
    if name in roomNameList:
        return False
    else:
        print("Hey! That room doesn't exist!")
        slp(2)
        print("Type the name exactly as it is in the square brackets")
        slp(3)
        return True

# Theme Checker
def checkTheme(room):
    checkThemeList = []
    for roomName in open("resources/roomTheme.txt"):
        checkThemeList.append(roomName.strip())
    for roomNameSplit in checkThemeList:
        theme = roomNameSplit.split("#")
        if room == theme[0]:
            return theme[1]

# Import Room Description
roomDescriptions = []
for descriptionLine in open("resources/roomDescriptions.txt"):
    roomDescriptions.append(descriptionLine.strip())

# Main Loop
while loopGame:

    # Intro and Player Room Picker
    print("Welcome to Room Escape!")
    slp(2)
    print("Navigate around the Room and try to escape!")
    slp(3.5)
    while loopIntro:
        print("Now pick a Room to play")
        slp(2)
        print("Here are the rooms available:")
        slp(1)
        for roomDescriptionLine in roomDescriptions: # Loops through and prints each room desc.
            print(roomDescriptionLine)
            slp(1)
        print("[ChangeLog] - Shows game update list (NOTE: Not a room)")
        slp(2)
        playerRoomPick = input("Pick a room: \n>>> ")
        if "changelog" in playerRoomPick.lower(): # Prints Change Log if that option selected
            printChangeLog = importChangeLog()
            for printChangeLogLine in printChangeLog:
                print(printChangeLogLine)
            print("\n\n")
            time.sleep(5)
            print("\n\n\n\n\n\n\n\n")
        else:
            loopIntro = checkName(playerRoomPick)

    # Reset Loop for when game restarts
    loopIntro = True

    # Continued Intro
    slp(2.5)
    playerName = input("Before we continue, I need your name\n>>> ")
    slp(1)
    print("Good luck, " + playerName + "!")
    slp(2)
    print("clearing screen...")
    slp(4)
    for clearScreen in range(0, 30):
        print("\n") # clears screen so intro doesn't clutter screen

    # Import Room selected by player
    GM = importRoom(playerRoomPick) # Shorthand for Game Room

    # Start Pos. Calculator
    for firstTupleValue in range(1, round(math.sqrt(len(GM))) + 1):
        for secondTupleValue in range(1, round(math.sqrt(len(GM))) + 1):
            if GM[firstTupleValue, secondTupleValue] == "S":
                playerPosition = [firstTupleValue, secondTupleValue]
                newPlayerPosition = playerPosition

    # Short Tutorial
    print("Use [W] [A] [S] [D] to move around!")
    slp(2)
    print("Wait for the >>> prompt, type a direction and hit enter!")
    slp(3)
    print("Good luck finding the exit, " + playerName + "!")
    slp(2)

    # Begin Game
    slp(3)
    print(playerName + ", " + checkTheme(playerRoomPick))

    # Begin Game Loop
    loopRoom = True
    while loopRoom:
        print("Which direction do you go?")
        slp(1)
        playerDirection = input(">>> ").upper()

        # Move Up - "W"
        if playerDirection == "W":
            newPlayerPosition[0] -= 1
            try:
                tileMove = translateMove(GM[newPlayerPosition[0], newPlayerPosition[1]])
                print(translateDesc(GM[newPlayerPosition[0], newPlayerPosition[1]]))
                newPlayerPosition[0] += tileMove
                playerPosition = newPlayerPosition
            except KeyError:
                print("You walk into a solid wood wall")
                newPlayerPosition[0] += 1
                playerPosition = newPlayerPosition

        # Move Down - "S"
        elif playerDirection == "S":
            newPlayerPosition[0] += 1
            try:
                tileMove = translateMove(GM[newPlayerPosition[0], newPlayerPosition[1]])
                print(translateDesc(GM[newPlayerPosition[0], newPlayerPosition[1]]))
                newPlayerPosition[0] -= tileMove
                playerPosition = newPlayerPosition
            except KeyError:
                print("You walk into a solid wood wall")
                newPlayerPosition[0] -= 1
                playerPosition = newPlayerPosition

        # Move Left - "A"
        elif playerDirection == "A":
            newPlayerPosition[1] -= 1
            try:
                tileMove = translateMove(GM[newPlayerPosition[0], newPlayerPosition[1]])
                print(translateDesc(GM[newPlayerPosition[0], newPlayerPosition[1]]))
                newPlayerPosition[1] += tileMove
                playerPosition = newPlayerPosition
            except KeyError:
                print("You walk into a solid wood wall")
                newPlayerPosition[1] += 1
                playerPosition = newPlayerPosition

        # Move Right - "D"
        elif playerDirection == "D":
            newPlayerPosition[1] += 1
            try:
                tileMove = translateMove(GM[newPlayerPosition[0], newPlayerPosition[1]])
                print(translateDesc(GM[newPlayerPosition[0], newPlayerPosition[1]]))
                newPlayerPosition[1] -= tileMove
                playerPosition = newPlayerPosition
            except KeyError:
                print("You walk into a solid wood wall")
                newPlayerPosition[1] -= 1
                playerPosition = newPlayerPosition

        # Direction Error
        else:
            print("You sit there, contemplating why you decided to do this Room")
            slp(3)
            print("Make sure to use the [W] [A] [S] [D] keys!")
            slp(2)

        # Player Escape Check / Finish Check
        if GM[playerPosition[0], playerPosition[1]] == "F":
            loopRoom = False
            print("You open the device and get out of the room.")
            slp(3)
            print("You made it!!")


    # Play Again Check
    slp(2)
    loopPlayAgain = True
    while loopPlayAgain:
        playAgainCheck = input("Do you want to play again? [y/n]\n>>> ").lower()
        if playAgainCheck == "y":
            print("Restarting game...")
            slp(5)
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\
                  \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            loopPlayAgain = False
        elif playAgainCheck == "n":
            print("Thanks for playing!!")
            slp(2)
            loopPlayAgain = False
            loopGame = False
        else:
            print("Please type a [y] or a [n]")
            slp(2)
