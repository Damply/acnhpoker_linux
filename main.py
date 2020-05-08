import socket
import time
import binascii
from os import system, name
import string

invOffset = '0xAC4723D0'
countOffset = '0xAC4723D4'

def clear():
    if name == 'nt':
        time.sleep(2)
        _ = system('cls')
        spawnItem()
    else:
        time.sleep(2)
        _ = system('clear')
        spawnItem()

def is_hex(s):
     hex_digits = set(string.hexdigits)
     return all(c in hex_digits for c in s)

def formatID(x):
    IDStr = str(x)

    if( len(IDStr) > 4):
        print("input too large.")
        clear()
    if ( len(IDStr) <= 4 ):
        n0 = "0" * ( 4 - len(IDStr) )
        #print(n0 + IDStr)
        preString = n0 + IDStr
        first, second = preString[:int(len(preString)/2)], preString[int(len(preString)/2):]
        fString = second + first
        return fString

def sendCommand(s, content):
    content += '\r\n'
    s.sendall(content.encode())
    print(content)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#change the connection info here.
s.connect(("192.168.1.51", 6000))





def spawnItem():
    user_input = input("Enter ItemID: ")
    if(is_hex(user_input)):

        invslot = input("Which Slot?: ")

        # i know there is a better way but its late and im tired.
        if (invslot) == "1":
            invOffset = '0xAC4723D0'
        elif (invslot) == "2":
            invOffset = '0xAC4723D8'
        elif (invslot) == "3":
            invOffset = '0xAC4723E0'
        elif (invslot) == "4":
            invOffset = '0xAC4723E8'
        elif (invslot) == "5":
            invOffset = '0xAC4723F0'
        elif (invslot) == "6":
            invOffset = '0xAC4723F8'
        elif (invslot) == "7":
            invOffset = '0xAC472400'
        elif (invslot) == "8":
            invOffset = '0xAC472408'
        elif (invslot) == "9":
            invOffset = '0xAC472410'
        elif (invslot) == "10":
            invOffset = '0xAC472418'
        elif (invslot) == "11":
            invOffset = '0xAC472420'
        elif (invslot) == "12":
            invOffset = '0xAC472428'
        elif (invslot) == "13":
            invOffset = '0xAC472430'
        elif (invslot) == "14":
            invOffset = '0xAC472438'
        elif (invslot) == "15":
            invOffset = '0xAC472440'
        elif (invslot) == "16":
            invOffset = '0xAC472448'
        elif (invslot) == "17":
            invOffset = '0xAC472450'
        elif (invslot) == "18":
            invOffset = '0xAC472458'
        elif (invslot) == "19":
            invOffset = '0xAC472460'
        elif (invslot) == "20":
            invOffset = '0xAC472468'

        itemString = "0x" + formatID(user_input)

        pokeString = f"poke {invOffset} {itemString}"

        sendCommand(s, pokeString.format(invOffset, itemString))

        itemCount = input("How Many?: ")

        if(is_hex(itemCount)):
            sendCommand(s, f"poke {countOffset} {hex(int(itemCount) - 1)}")
            print("Item(s) sent!")
            clear()
        else:
            print("error, sent 1")
            clear()

    else:
        print("numbers only, dunce.")
        clear()


spawnItem()
