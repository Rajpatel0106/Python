import colorama
from colorama import Fore, Back, Style
colorama.init()
marks = int(input("ENTER THE MARKS=>"))

if marks > 20:
    print(Back.GREEN, " VERY GOOD")
else:
    print(Back.BLUE, " DO HARD WORK")
