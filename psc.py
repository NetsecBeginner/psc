#!/usr/bin/env python
#Netsec Beginner - 3/29/17
#psc - Password Strength Checker; Checks Strength of Entered Passwords

#Import argparse to parse command line arguments; math for calculation of bit entropy
import argparse
import math

#Global Variables
BitEntropy = 0
SecondsToCrack = 0
MinutesToCrack = 0
HoursToCrack = 0
DaysToCrack = 0
WeeksToCrack = 0
MonthsToCrack = 0
YearsToCrack = 0
Dictionary = []

#Main Function
def main():
	#Use Global Dictionary, BitEntropy, and HoursToCrack Variables
	global Dictionary, BitEntropy, HoursToCrack
	
	#Create Argument Parser, and Add Options for Mutate and Dictionary
	Parser = argparse.ArgumentParser()
	Parser.add_argument("Password", type=str, help="Password Strength Testing Program")
	Parser.add_argument("-d", "--dictionary", type=str, help="Test Against Dictionary Attacks")
	arguments = Parser.parse_args()
	
	#Interpret Arguments
	if arguments.dictionary:
		Dict = open(arguments.dictionary, "r")
		print("Reading Dictionary...")
		for line in Dict:
			Dictionary.append(line[:-2])
			
	#Calculate Password Strength
	print("Testing Brute Force Strength...")
	Brute(arguments.Password)
	if arguments.dictionary:
		SecureAgainstDict = DictionaryAttack(arguments.Password, Dictionary)
		print("Testing Against Dictionary...")
	
	#Output
	print("\n\nEntropy: " + str(BitEntropy))
	print("\nSeconds To Crack: " + str(SecondsToCrack))
	print("Minutes To Crack: " + str(MinutesToCrack))
	print("Hours To Crack: " + str(HoursToCrack))
	print("Days To Crack: " + str(DaysToCrack))
	print("Weeks To Crack: " + str(WeeksToCrack))
	print("Months To Crack: " + str(MonthsToCrack))
	print("Years To Crack: " + str(YearsToCrack))
	if arguments.dictionary:
		print("\nSecure Against Dictionary Attacks: " + SecureAgainstDict + "\n")
	

#Check Strength Against Brute Force Attacks
def Brute(password):
	#Use Global BitEntropy and Time To Crack Variables
	global BitEntropy, SecondsToCrack, MinutesToCrack, HoursToCrack, DaysToCrack, WeeksToCrack, MonthsToCrack, YearsToCrack
	
	#List of Symbols
	Symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "`", "~", "-", "_", "+", "=",".", ",", ":", ";", "'", '"']
	
	#Determine Character Pool, Set Used Values To False, Escape Password String
	CharPool = 0
	LowerUsed = False
	UpperUsed = False
	NumUsed = False
	SymUsed = False
	Pass = password.encode('string-escape') #Escape String So Special Characters Don't Affect Length
	
	for i in range(len(password)):
		if Pass[i] == Pass[i].lower() and Pass[i] not in Symbols and LowerUsed == False:
			CharPool = CharPool + 26
			LowerUsed = True
		elif Pass[i] == Pass[i].upper() and Pass[i] not in Symbols and UpperUsed == False:
			CharPool = CharPool + 26
			UpperUsed = True
		elif Pass[i].isdigit() and NumUsed == False:
			CharPool = CharPool + 10
			NumUsed = True
		elif Pass[i] in Symbols and SymUsed == False:
			CharPool = CharPool + len(Symbols)
			SymUsed = True
		else:
			if Pass[i].isalpha() == False and Pass[i].isdigit() == False and Pass[i] not in Symbols:
				Errors(3)

	#Get Entropy of Each Bit and Calculate Password Entropy
	BitEntropy = math.log(CharPool, 2) * len(password)
	
	#Get Total Number of Combinations and Divivde by Estimated Cracking Speed in various measurements of time(taken from https://hashcat.net/wiki/doku.php?id=mask_attack)
	SecondsToCrack = math.pow(2, BitEntropy) / 100000000
	MinutesToCrack = math.pow(2, BitEntropy) / 100000000 / 60
	HoursToCrack = math.pow(2, BitEntropy) / 100000000 / 3600
	DaysToCrack = math.pow(2, BitEntropy) / 100000000 / 86400
	WeeksToCrack = math.pow(2, BitEntropy) / 100000000 / 604800
	MonthsToCrack = math.pow(2, BitEntropy) / 100000000 / 2628000
	YearsToCrack = math.pow(2, BitEntropy) / 100000000 / 31536000

#Check Strength Against Dictionary Attacks
def DictionaryAttack(password, dictionary):
	if password in dictionary:
		return "Insecure"
	else:
		return "Secure"

                 
#Returns Errors(Easier to handle it all in one place)
def Errors(code):
	if code == 1: #File Does Not Exist
		print("ERROR: Unable to locate File")
		exit(1)
	elif code == 2: #Not Running as Root(Probably Won't Ever Come up, but you Never Know)
		print("Please Say The Magic Word\nHint: The Magic Word Is Sudo")
		exit(2)
	elif code == 3: #Password Contains Character not in Character Set
		print("ERROR: Password Contains Unknown Character; Reliable Results Can Not Be Obtained")
		exit(3)
	elif code == 4: #No Dictionary Specified
		print("ERROR: No Dictionary Specified")
		exit(4)

#Call Main
main()
