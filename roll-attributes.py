import random
def roll_d6():
	return random.randint(1, 6)

def roll_3d6():
	result = roll_d6() + roll_d6() + roll_d6()
	return str(result)

STR = roll_3d6()
INT = roll_3d6()
WIS = roll_3d6()
DEX = roll_3d6()
CON = roll_3d6()
CHA = roll_3d6()


print ("STR: " + STR);
print ("INT: " + INT);
print ("WIS: " + WIS);
print ("DEX: " + DEX);
print ("CON: " + CON);
print ("CHA: " + CHA);
