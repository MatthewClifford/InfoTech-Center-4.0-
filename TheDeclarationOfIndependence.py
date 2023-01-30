# Programmer: Matthew Clifford
# Date: 1.20.23
# Program: InfoTech center upgrades

"""
Our Welcome Screen will start our program letting
drivers know that the InfoTech Center 4.0 OS is loading
"""

# Import Libraries Here
import time, sys, colorama
from time import sleep
import colorama
from colorama import Fore


print(Fore.RED + "\n\nWelcome - InfoTech Center 4.0")
sleep(2)

x = 0
a = 0

print('')

while x != 20:
    x += 1
    b = (Fore.BLUE + "InfoTech Center 4.0 OS is Loading" + "." * a)
    a = a + 1
# so `b` is printed on top of the previous line.
    sys.stdout.write('\r'+b)

    time.sleep(0.5)
    if a == 4:
        a = 0
    if x == 20:
        print(Fore.GREEN + '\n\nAccess Granted!')