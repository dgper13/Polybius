import math
from typing import MutableSet


def createTable(alphabet):
    alphabetSize = len(alphabet)
    rowSize = int(math.sqrt(nearestPerfectSquare(alphabetSize)))
    table = ()
    numberOfRows = alphabetSize // rowSize
    if alphabetSize % rowSize != 0:
        numberOfRows += 1
    for i in range(numberOfRows):
        table += (alphabet[i*rowSize : min((i+1)*rowSize, alphabetSize)],)
    return table


def nearestPerfectSquare(number):
    ceiling = number
    floor = number
    while math.sqrt(ceiling) % 1 != 0:
        ceiling += 1
    while math.sqrt(floor) % 1 != 0:
        floor -= 1
    if abs(ceiling - number) > abs(floor - number):
        return floor
    return ceiling


def getCoordinates(character, table):
    for ln in range(len(table)):
        for cl in range(len(table[ln])):
            if character == table[ln][cl]:
                return str(ln) + str(cl)
    return "XX"


def encrypt(message, table):
    encrypted = ""
    for character in message:
        encrypted += getCoordinates(character, table)
    return encrypted


def getCharacter(coordinates, table):
    if coordinates == "XX":
        return "?"
    return table[eval(coordinates[0])][eval(coordinates[1])]


def decrypt(encrypted, table):
    decrypted = ""
    for i in range(0, len(encrypted), 2):
        decrypted += getCharacter(encrypted[i:i+2], table)
    return decrypted


alphabet = ('A','B','C','D','E','F','G','H','I','J',' ','L','M','N','O','P','Q','R','S','T','U','V','X','Z','.')

table = createTable(alphabet)
message = "NOT A LOT GOING ON AT THE MOMENT"
print(f"message: {message}")

encrypted = encrypt(message, table)
print(f"encrypted: {encrypted}")

decrypted = decrypt(encrypted, table)
print(f"decrypted: {decrypted}")