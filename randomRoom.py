# Room Escape Room Manager
# Generates a random room
# Will eventually be able to manage rooms here as well
# Start Date 23/10/2018

# imports
import random
import time
import math
import os


# This is for base level asking. Is frame for knowing what I need to get out of code
# It will also have no incorrect typing checks

# Room dimensions
askRoomDimension = input("What are the dimensions? [NxN]\n>>> ")
roomDimension = int(askRoomDimension.split("x")[0])

#Room name
askRoomName = input("What is the room name? [Only lowercase and numbers]\n>>> ")
roomName = askRoomName

# Room description
askRoomDescription = input("What is the room description?\n>>> ")
roomDescription = "[" + roomName + "]" + " - " + askRoomDescription

# Room theme
askRoomTheme = input("What is the starting room text?\n>>> ")
roomTheme = roomName + "#" + askRoomTheme

# Random Room generator - does it based on size
if roomDimension < 6: # for 2x2 - 5x5 rooms
    fillSize = roomDimension ** 2
    roomArray = ["S", "F"]
    wallCount = round(fillSize/2 - 2) # calculate wall amount 
    spaceCount = fillSize - wallCount - 2 #  fill rest with moveable spaces
    for i in range(wallCount):
        roomArray.append("#")
    for x in range(spaceCount):
        roomArray.append("0")
else: # for 6x6+ rooms
    fillSize = roomDimension ** 2
    roomArray = ["S", "F"]
    wallCount = round(fillSize/2.4 - 2) # calculate wall amount 
    spaceCount = fillSize - wallCount - 2 #  fill rest with moveable spaces
    for i in range(wallCount):
        roomArray.append("#")
    for i in range(spaceCount):
        roomArray.append("0")

# make file system
os.mkdir("rooms/" + roomName)
time.sleep(1)
with open("rooms/" + roomName + "/" + roomName + ".txt", "w+") as room:
    for x in range(roomDimension):
        for y in range(roomDimension):
            roomIndex = round(random.random()*len(roomArray) - 1)
            room.write(str(roomArray[roomIndex]))
            roomArray.pop(roomIndex)
            room.write(" ")
        room.write("\n")
    room.write(str(roomDimension))

# Add room name in roomName text file
with open("resources/roomNames.txt", "a") as room:
    room.write(roomName + "\n")

# Add room theme
with open("resources/roomTheme.txt", "a") as room:
    room.write(roomTheme + "\n")

# Add room description
with open("resources/roomDescriptions.txt", "a") as room:
    room.write(roomDescription + "\n")

print("Generating...")
time.sleep(3)
print("Done!")
    


    
