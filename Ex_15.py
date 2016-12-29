from sys import argv

#man uebergibt den Dateinamen beim Aufrufen des Skripts
script, filename = argv

# man oeffnet die datei als variable txt
txt = open(filename)

# datei wird genannt und der inhalt gelesen
print "Here's your file %r:" % filename
print txt.read()

# hier kann man nur wieder die gleiche Datei oeffnen!
print "Type the filename again:"
file_again = raw_input("> ")

# erneutes oeffnen der datei
txt_again = open(file_again)

#die wird hier einfach nochmal vorgelesen
print txt_again.read()

txt.close()
txt_again.close()
