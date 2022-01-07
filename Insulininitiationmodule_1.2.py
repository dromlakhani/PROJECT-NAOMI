#!/usr/bin/env python3

print("Welcome to PROJECT NAOMI: THE COMPLETE INSULIN MODULE FOR NON-PREGNANT, INSULIN NAIVE, ADULT PATIENTS with TYPE 2 DIABETES by Dr. Om J Lakhani version 1.2")

next = input("This program is not for patients with End stage renal disease, patients on glucocorticoids and those having ketosis or ketoacidosis. PRESS ANY KEY TO CONTINUE:")

#Enter baseline patient details

name = input("Enter name of the patient:")
age = int(input("Enter age of the patient:"))

if age <= 18:
	print("This program is only for adult patients.")
	quit()

else:
	hba1c = float(input("Enter HbA1c of patient. THIS IS COMPULSORY:"))
	fbs = float(input("Enter FBS of patient. THIS IS COMPULSORY:"))
	pp2bs = float(input("Enter PP2BS / RBS of patient. Type 0 if PP2BS / RBS not available:"))
	oad = int(input("Enter the number of different type of Oral antidiabetics which the patient is taking. Type 0 if the patient is NOT on any oral antidiabetics:"))
	osmotic = input("Does your patient currently have any symptoms of unexplained weight loss/polyuria/polydipsia/polyphagia ? 1 for Yes and 0 for No:")
	afford = int(input("On Scale of 1 to 10, how much according to you is the patient's affordability (1 for very poor and 10 for very rich):"))
	
	
	
	
	#Module 1
	print("Module 1 :Does your patient need insulin ?")
	
	if osmotic == 1 or pp2bs >=400:
		next = input("\nYour patient needs insulin. Enter any key to continue\n")
	elif hba1c >= 10:
		next = input("\nYour patient needs insulin. Enter any key to continue\n")
	elif hba1c >= 8.5 and oad >= 3:
		next = input("\nYour patient needs insulin. Enter any key to continue\n")
	elif hba1c >= 9 and oad >= 2:
		next = input("\nYour patient needs insulin. Enter any key to continue\n")
	elif fbs >200 and pp2bs >= 300:
		next = input("\nYour patient needs insulin. Enter any key to continue\n")
	else :
		next = input("Your patient may not require insulin initiation at present. Enter any key to continue")
		print("End of program for this patient, run again for another patient")
		quit()
	
		
	
	
	
	print("\nModule 2 : Which insulin should you use ?\n")
	ratio = fbs / hba1c 
	delta = pp2bs - fbs
	
	
	if ratio > 25 or delta > 100:
		if afford <= 3 :
			next = input("\nIt is better to give this patient a premixed insulin. Looking at the affordability of the patient, a MIXTARD or HUMINSULIN 30/70 is a good choice. Press any key to go to the module for the starting dose insulin\n")
		elif afford > 3 and afford <= 6:
			ext = input("\nIt is better to give this patient a premixed insulin. Looking at the affordability of the patient, a NOVOMIX 30/70 or an EGLUCENT MIX 25/75 is a good choice. Press any key to go to the module for the starting dose insulin\n")
		elif afford > 6 :
			ext = input("\nIt is better to give this patient a co-forumulation insulin. Looking at the affordability of the patient, a RYZODEG 30/70 is a good choice. Press any key to go to the module for the starting dose insulin\n")
	else:
		if afford <= 4 :
			next = input("\nIt is better to give this patient a BASAL insulin. Looking at the affordability of the patient, a INSULATARD, HUMINSULIN-N or BASALOG is a good choice. Press any key to go to the module for the starting dose insulin\n")
		elif afford > 4 and afford <= 8:
			ext = input("\nIt is better to give this patient a BASAL INSULIN. Looking at the affordability of the patient, a LANTUS or a BASAGLAR is a good choice. Press any key to go to the module for the starting dose insulin\n")
		elif afford > 8 :
			ext = input("\nIt is better to give this patient a BASAL INSULIN. Looking at the affordability of the patient, a TRESIBA or a TOUJEO is a good choice. Press any key to go to the module for the starting dose insulin\n")
	
	
			
				
	#Module 3- Insulin dose
	
	
	print("\nModule 3 : 'What dose of insulin should I start ?\n")
	
	insulin_type = input("\nEnter the name of the insulin that you have chosen to start:")
	bid = round(((fbs-50))/10)
	bid_s = str(bid)
	output = "\nThe starting dose of %s suggested is: %s units. Press any key to continue:" %(insulin_type,bid_s)
	next = input(output)
	





	