#man fügt 10 in den string ein
x = "There are %d types of people." % 10
#def der variablen binary und do_not
binary = "binary"
do_not = "don't"
#einfügen der variablen in string
y = "Those who know %s and those who %s." % (binary, do_not)

#drucken der variablen
print x
print y

#einfügen und drucken der variablen
print "I said: %r." % x
print "I also said: '%s'" % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

#ausdrucken beider strings
print w + e
