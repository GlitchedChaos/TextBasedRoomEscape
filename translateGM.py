# Letter Translator for Room Escape!
def translateDesc(letter):
    if letter == "#":
        return "You walk into a solid wood wall"
    elif letter == "0":
        return "You walk into a dark corridor with creaky floor boards"
    elif letter == "F":
        return "You find the exit!! At last!!"
    elif letter == "S":
        return "You walk on the spot you began this journey on"
    elif letter == "g":
        return "You found a Green key! \nYou hear a soft click from somewhere..."
    elif letter == "G":
        return "A green, locked door. Wonder what unlocks it?"

def translateMove(letter):
    if letter == "#":
        return 1
    elif letter == "0":
        return 0
    elif letter == "F":
        return 0
    elif letter == "S":
        return 0
    elif letter == "g":
        return 0
    elif letter == "G":
        return 1
