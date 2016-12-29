#argv is the argument variable, die haelt alle Werte die man
#beim Aufrufen des Skripts uebergibt
#dieses skript ruft man zB auf mit python Ex_13.py first 2nd 3rd
#dann heisst das skript Ex_13.py
#die zweite Variable 2nd usw
from sys import argv

script, first, second, third = argv

print "The script is called:", script
print "The first variable is:", first
print "The second variable is:", second
print "The third variable is:", third

#man wird nach namen gefragt und dieser wird dann auch gleich zurückgegeben
print raw_input("what is your name?" )
