import random
def roll_d6():
	return random.randint(1, 6)

def roll_4d6():
	dice_one = roll_d6()
	dice_two = roll_d6()
	dice_three = roll_d6()
	dice_four = roll_d6()
	small_dice = dice_one
	if (dice_two < small_dice):
		small_dice = dice_two
	if (dice_three < small_dice):
		small_dice = dice_three
	if (dice_four < small_dice):
		small_dice = dice_four
	
	result = dice_one + dice_two + dice_three + dice_four - small_dice
#	print(dice_one, dice_two, dice_three, dice_four, small_dice)
	return str(result)

STR = roll_4d6()
INT = roll_4d6()
WIS = roll_4d6()
DEX = roll_4d6()
CON = roll_4d6()
CHA = roll_4d6()


print ("STR: " + STR);
print ("INT: " + INT);
print ("WIS: " + WIS);
print ("DEX: " + DEX);
print ("CON: " + CON);
print ("CHA: " + CHA);
