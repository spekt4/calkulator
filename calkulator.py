# клава 

from colorama import init
from colorama import Fore, Back, Style

# use Colorama to make Termcolor work on Windows too
init()

print( Back.CYAN )

what = input(" чо делать? (+, -): " )

a = float( input("Введи первое число: ") )
b = float( input("Введи второе число: ") )

print( Back.GREEN )

if what == "+":
    c = a + b
    print("Результат: " + str(c))

elif what == "-":
    c = a - b
    print("Результат: " + str(c))
    print( Back.RED )
else:
    print("Выбрана неверная опция!")