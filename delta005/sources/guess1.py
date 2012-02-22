#
# Βρες τον αριθμό - Απόπειρα 2
#
import random
thenumber = random.randint(1,50)
print "Έχω σκεφτεί ένα αριθμό από το 1 ως το 50."
print "Μπορείς να τον βρεις;"
guess = 0
while guess != thenumber:
    guess=input("Δώσε τον αριθμό: ")
    if guess > thenumber:
        print "Έδωσες μεγαλύτερο αριθμό!"
    if guess < thenumber:
        print "Έδωσες μικρότερο αριθμό!"
print "Τον βρήκες!!!"
