#Dice Roll script
import random

class Dice : 
	def roll(self, numOfDice : int) : 
		rollNum = 0
		print("+===============+")
		print("")

		while numOfDice > 0 : 
			randomNum = random.choice(range(1,7))
			self.draw(randomNum)
			numOfDice -= 1
			rollNum += randomNum

		print("")
		print("YOU ROLLED: " + str(rollNum))
		print("")
		print("+===============+")
		print("")

	def draw(self, num : int) : 
		dot1=dot2=dot3=dot4=dot5=dot6=dot7=dot8=dot9 = " "
		if num == 1 : 
			dot5 = "o"
		if num == 2 : 
			dot3=dot7 = "o"
		if num == 3 : 
			dot3=dot5=dot7 = "o"
		if num == 4 : 
			dot1=dot3=dot7=dot9 = "o"
		if num == 5 : 
			dot1=dot3=dot5=dot7=dot9 = "o"
		if num == 6 : 
			dot1=dot3=dot4=dot6=dot7=dot9 = "o"

		print(".-------.")
		print("| " + dot1 + " " + dot2 + " " + dot3 + " |")
		print("| " + dot4 + " " + dot5 + " " + dot6 + " |")
		print("| " + dot7 + " " + dot8 + " " + dot9 + " |")
		print("'-------'")


#tests
"""
die = Dice()
die.draw(1)
die.draw(2)
die.draw(3)
die.draw(4)
die.draw(5)
die.draw(6)
"""

#loop for user inputs 
while(True) : 
	print("Type the number of dice you wish to roll, then hit Enter!")
	print("")
	print("To stop the script, type 'exit'")
	print("")

	numStr = input()

	if(numStr == "exit") : break

	while not(numStr.isdigit()) : 
		print("You didn't input a number, try again!")
		numStr = input()

	num = int(numStr)

	dice = Dice()
	dice.roll(num)


		