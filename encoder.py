#!/usr/bin/python3
from termcolor import colored
print(colored("""
________$$$$
_______$$__$
_______$___$$
_______$___$$
_______$$___$$
________$____$$
________$$____$$$
_________$$_____$$
_________$$______$$
__________$_______$$
____$$$$$$$________$$
__$$$_______________$$$$$$
_$$____$$$$____________$$$
_$___$$$__$$$____________$$
_$$________$$$____________$
__$$____$$$$$$____________$
__$$$$$$$____$$___________$
__$$_______$$$$___________$
___$$$$$$$$$__$$_________$$
____$________$$$$_____$$$$
____$$____$$$$$$____$$$$$$
_____$$$$$$____$$__$$
_______$_____$$$_$$$
________$$$$$$$$$$ ""","green"))
print(colored("𝓋ℯ𝓇𝓈𝒾ℴ𝓃 1.1","red"))
print(colored("""
Ⲇⲉ𝓿ⲉ𝓵ⲟⲣⲉⲇ Ⲃⲩ Ⲛⲁꞅⲉ𝛓ⲏ    
""","yellow"))
dir={'a':'2000','b':'0200','c':'0020','d':'3000','e':'0300',
'f':'0030','g':'4000','h':'0400','i':'0040','j':'5000',
'k':'5000','l':'0050','m':'6000','n':'0600','o':'0060',
'p':'7000','q':'0700','r':'0070','s':'0007','t':'8000',
'u':'0800','v':'0080','w':'9000','x':'0900','y':'0090',
'z':'0009', ' ':'1000','?':'x000','!':'y000'}
print(
colored("""
1) For Encoding:
2) For Decoding:
Choose the right option from the above :""","red"))
operation = int(input())
if(operation==1):
    string=input(colored("enter the plain text that you want to encode :","yellow"))
    string=string.lower()
    for char in string:
         print(dir[char],end='')
elif(operation==2):
    newstr=[]
    key_list = list(dir.keys())
    val_list = list(dir.values())
    str=input(colored("enter the cipher text that you want to decode :","yellow"))
    print(colored("the plain text of that cipher is :","blue"))
    length = len(str)
    chars = 4
    equalStr = []
    for i in range(0, length, chars):
        part = str[ i : i+chars]
        equalStr.append(part)
    for i in equalStr:
        print(key_list[val_list.index(i)],end="")
else:
    print("you have enter the wrong option")
