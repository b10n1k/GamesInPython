#
# Βρες τον αριθμό - Απόπειρα 3
#
import random
thenumber = random.randint(1,50)
name = raw_input("Δώσε το όνομα σου: ")
print "Έχω σκεφτεί ένα αριθμό από το 1 ως το 50."
print "Μπορείς να τον βρεις;"
guess = 0
tries = 0
while guess != thenumber:
    tries = tries + 1
    guess=input("Δώσε τον αριθμό: ")
    if guess > thenumber:
        print "Έδωσες μεγαλύτερο αριθμό!"
    if guess < thenumber:
        print "Έδωσες μικρότερο αριθμό!"
print "Συγχαρητήρια", name, "τον βρήκες σε", tries, "προσπάθειες!"
