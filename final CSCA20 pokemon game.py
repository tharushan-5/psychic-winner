import random


begin=input("Welcome to our game. Our project is a turn-based strategy game where the \nplayer must battle through different opponents of different strengths to win. \nThe player and opponent will have different elemental moves that will be \nstronger depending on the opposing type. The player will fight through \ndifferent bosses(gyms), level up their Pokemon and choose to learn new moves \nto help them succeed. \nPress any key to continue or type cheat sheet for battle strats\n")
if begin == 'cheat sheet':
	print('\n(Fire > Grass, Grass > Water, Water > Fire, Ground > Electric)\n')

	

Pokemon = ["Charmander", "Bulbasaur", "Squirtle"]
Start_stats = {"Health": 100}

print(Pokemon)

Start_stats['Name'] = input("Choose your Pokemon: ")

while Start_stats['Name'] not in Pokemon:
	print("\nThat is not a valid Pokemon")
	print(Pokemon)
	Start_stats['Name'] = input("Choose a Pokemon from the options above: ")
	

eff = 1.3
non_eff = 0.7
att_multi = 1.0
moves = {"tackle": range(20,23), "heal": range(15,20)}

if Start_stats['Name'] == "Charmander":
        	Start_stats['Element'] = 'Fire'
if Start_stats['Name'] == 'Bulbasaur':
        	Start_stats['Element'] = "Grass"
if Start_stats['Name'] == "Squirtle":
        	Start_stats['Element'] = "Water"


def battles(start_stats, opp_stats):
	'''
	(dict, dict)
	basic fight sequence
	'''
	#As long as both Pokemon are above 0 Health continue the battle
	while opp_stats['Health'] > 0 and start_stats['Health'] > 0:
		#Ask the player to choose a move from the move set
		choice = input("Choose a move:\n" + str(list(moves.keys())))
		#If the move choosen is not in moves choose again
		while choice not in moves:
			print('\nThat is not a valid move')
			choice = input("Choose a move:\n" + str(list(moves.keys())))
		#Run through each move
		if choice == 'tackle':
			opp_stats["Health"] = opp_stats["Health"] - round(random.choice(moves["tackle"])*att_multi)
			if opp_stats["Health"] <= 0:
				print("\n" + opp_stats['Name'] + "'s Health: " + str(0))
			else:
				print("\n" + opp_stats['Name'] + "'s Health: " +  str(opp_stats['Health']))
		
		if choice == 'bodyslam':
			opp_stats["Health"] = opp_stats["Health"] - round(random.choice(moves["bodyslam"])*att_multi)
			if opp_stats["Health"] <= 0:
				print("\n" + opp_stats['Name'] + "'s Health: " + str(0))
			else:
				print("\n" + opp_stats['Name'] + "'s Health: " +  str(opp_stats['Health']))       	 
				
		if choice == 'vinewhip':
			if opp_stats['Element'] is 'Water':
				opp_stats["Health"] = opp_stats["Health"] - round((random.choice(moves["vinewhip"])*att_multi)*eff)
				if opp_stats["Health"] <= 0:
					print("\n" + opp_stats['Name'] + "'s Health: " + str(0))
				else:
					print("\n" + opp_stats['Name'] + "'s Health: " +  str(opp_stats['Health']))
			
			elif opp_stats['Element'] is 'Fire':
				opp_stats["Health"] = opp_stats["Health"] - round((random.choice(moves["vinewhip"])*att_multi)*non_eff)
				if opp_stats["Health"] <= 0:
					print("\n" + opp_stats['Name'] + "'s Health: " + str(0))
				else:
					print("\n" + opp_stats['Name'] + "'s Health: " +  str(opp_stats['Health']))		
			else:
				opp_stats["Health"] = opp_stats["Health"] - round(random.choice(moves["vinewhip"])*att_multi)
				if opp_stats["Health"] <= 0:
					print("\n" + opp_stats['Name'] + "'s Health: " + str(0))
				else:
					print("\n" + opp_stats['Name'] + "'s Health: " +  str(opp_stats['Health']))		
       	 
		if choice ==  'ember':
			if opp_stats['Element'] is 'Water':
				opp_stats["Health"] = opp_stats["Health"] - round((random.choice(moves["ember"])*att_multi)*non_eff)
				if opp_stats["Health"] <= 0:
					print("\n" + opp_stats['Name'] + "'s Health: " + str(0))
				else:
					print("\n" + opp_stats['Name'] + "'s Health: " +  str(opp_stats['Health']))		
			elif opp_stats['Element'] is 'Grass':
				opp_stats["Health"] = opp_stats["Health"] - round((random.choice(moves["ember"])*att_multi)*eff)
				if opp_stats["Health"] <= 0:
					print("\n" + opp_stats['Name'] + "'s Health: " + str(0))
				else:
					print("\n" + opp_stats['Name'] + "'s Health: " +  str(opp_stats['Health']))		
			else:
				opp_stats["Health"] = opp_stats["Health"] - round((random.choice(moves["ember"])*att_multi))
				if opp_stats["Health"] <= 0:
					print("\n" + opp_stats['Name'] + "'s Health: " + str(0))
				else:
					print("\n" + opp_stats['Name'] + "'s Health: " +  str(opp_stats['Health']))		
		
		if choice == 'watergun':
			if opp_stats['Element'] is 'Water':
				opp_stats["Health"] = opp_stats["Health"] - round((random.choice(moves["watergun"])*att_multi)*eff)
				if opp_stats["Health"] <= 0:
					print("\n" + opp_stats['Name'] + "'s Health: " + str(0))
				else:
					print("\n" + opp_stats['Name'] + "'s Health: " +  str(opp_stats['Health']))		
			elif opp_stats['Element'] is 'Grass':
				opp_stats["Health"] = opp_stats["Health"] - round((random.choice(moves["watergun"])*att_multi)*non_eff)
				if opp_stats["Health"] <= 0:
					print("\n" + opp_stats['Name'] + "'s Health: " + str(0))
				else:
					print("\n" + opp_stats['Name'] + "'s Health: " +  str(opp_stats['Health']))		
			else:
				opp_stats["Health"] = opp_stats["Health"] - round((random.choice(moves["watergun"])*att_multi))
				if opp_stats["Health"] <= 0:
					print("\n" + opp_stats['Name'] + "'s Health: " + str(0))
				else:
					print("\n" + opp_stats['Name'] + "'s Health: " +  str(opp_stats['Health']))		

		if choice == 'solarbeam':
			if opp_stats['Element'] is 'Water':
				opp_stats["Health"] = opp_stats["Health"] - round((random.choice(moves["solarbeam"])*att_multi)*eff)
				if opp_stats["Health"] <= 0:
					print("\n" + opp_stats['Name'] + "'s Health: " + str(0))
				else:
					print("\n" + opp_stats['Name'] + "'s Health: " +  str(opp_stats['Health']))		
			elif opp_stats['Element'] is 'Fire':
				opp_stats["Health"] = opp_stats["Health"] - round((random.choice(moves["solarbeam"])*att_multi)*non_eff)
				if opp_stats["Health"] <= 0:
					print("\n" + opp_stats['Name'] + "'s Health: " + str(0))
				else:
					print("\n" + opp_stats['Name'] + "'s Health: " +  str(opp_stats['Health']))		
			else:
				opp_stats["Health"] = opp_stats["Health"] - round((random.choice(moves["solarbeam"])*att_multi))
				if opp_stats["Health"] <= 0:
					print("\n" + opp_stats['Name'] + "'s Health: " + str(0))
				else:
					print("\n" + opp_stats['Name'] + "'s Health: " +  str(opp_stats['Health']))		

		if choice == 'hydropump':
			if opp_stats['Element'] is 'Fire':
				opp_stats["Health"] = opp_stats["Health"] - round((random.choice(moves["hydropump"])*att_multi)*eff)
				if opp_stats["Health"] <= 0:
					print("\n" + opp_stats['Name'] + "'s Health: " + str(0))	
				else:
					print("\n" + opp_stats['Name'] + "'s Health: " +  str(opp_stats['Health']))

			elif opp_stats['Element'] is 'Grass':
				opp_stats["Health"] = opp_stats["Health"] - round((random.choice(moves["hydropump"])*att_multi)*non_eff)
				if opp_stats["Health"] <= 0:
					print("\n" + opp_stats['Name'] + "'s Health: " + str(0))	
				else:
					print("\n" + opp_stats['Name'] + "'s Health: " +  str(opp_stats['Health']))			
			else:
				opp_stats["Health"] = opp_stats["Health"] - round((random.choice(moves["hydropump"])*att_multi))
				if opp_stats["Health"] <= 0:
					print("\n" + opp_stats['Name'] + "'s Health: " + str(0))	
				else:
					print("\n" + opp_stats['Name'] + "'s Health: " +  str(opp_stats['Health']))			

		if choice == 'firefang':
			if opp_stats['Element'] is 'Water':
				opp_stats["Health"] = opp_stats["Health"] - round((random.choice(moves["firefang"])*att_multi)*non_eff)
				if opp_stats["Health"] <= 0:
					print("\n" + opp_stats['Name'] + "'s Health: " + str(0))	
				else:
					print("\n" + opp_stats['Name'] + "'s Health: " +  str(opp_stats['Health']))			
			elif opp_stats['Element'] is 'Grass':
				opp_stats["Health"] = opp_stats["Health"] - round((random.choice(moves["firefang"])*att_multi)*eff)
				if opp_stats["Health"] <= 0:
					print("\n" + opp_stats['Name'] + "'s Health: " + str(0))	
				else:
					print("\n" + opp_stats['Name'] + "'s Health: " +  str(opp_stats['Health']))			
			else:
				opp_stats["Health"] = opp_stats["Health"] - round((random.choice(moves["firefang"])*att_multi))
				if opp_stats["Health"] <= 0:
					print("\n" + opp_stats['Name'] + "'s Health: " + str(0))	
				else:
					print("\n" + opp_stats['Name'] + "'s Health: " +  str(opp_stats['Health']))			

		if choice == 'EARFQUAKE':
			if opp_stats['Element'] is 'Electric':
				opp_stats["Health"] = opp_stats["Health"] - round((random.choice(moves["EARFQUAKE"])*att_multi)*eff)
				if opp_stats["Health"] <= 0:
					print("\n" + opp_stats['Name'] + "'s Health: " + str(0))	
				else:
					print("\n" + opp_stats['Name'] + "'s Health: " +  str(opp_stats['Health']))			
			else:
				opp_stats["Health"] = opp_stats["Health"] - round((random.choice(moves["EARFQUAKE"])*att_multi))
				if opp_stats["Health"] <= 0:
					print("\n" + opp_stats['Name'] + "'s Health: " + str(0))	
				else:
					print("\n" + opp_stats['Name'] + "'s Health: " +  str(opp_stats['Health']))			

		if choice == 'heal':
			start_stats['Health'] = start_stats['Health'] + round((random.choice(moves['heal'])*att_multi))
			print("\n" + start_stats['Name'] + "'s Health: " +  str(start_stats['Health']))
			print(opp_stats['Name'] + "'s Health:" + str(opp_stats["Health"]))
		#Choose a random move for the opponent
		opp_choice = random.choice(list(opp_moves))
		#Run through each move
		if opp_stats['Health'] > 0:
			if opp_choice == 'tackle':
				start_stats['Health'] = start_stats['Health'] - round((random.choice(opp_moves['tackle'])))
				print('\n' + opp_stats['Name'] + ' used tackle')
				if start_stats['Health'] <= 0:
					print('\n' + start_stats['Name'] + 's Health: ' + str(0))
				else:
					print('\n' + start_stats['Name'] + 's Health: ' + str(start_stats['Health']))
			if opp_choice == 'headbutt':
				start_stats['Health'] = start_stats['Health'] - round((random.choice(opp_moves['headbutt'])))
				print('\n' + opp_stats['Name'] + ' used headbutt')
				if start_stats['Health'] <= 0:
					print('\n' + start_stats['Name'] + 's Health: ' + str(0))
				else:		
					print('\n' + start_stats['Name'] + 's Health: ' + str(start_stats['Health']))				
			if opp_choice == 'takedown':
				start_stats['Health'] = start_stats['Health'] - round((random.choice(opp_moves['takedown'])))
				print('\n' + opp_stats['Name'] + ' used takedown')
				if start_stats['Health'] <= 0:
					print('\n' + start_stats['Name'] + 's Health: ' + str(0))
				else:		
					print('\n' + start_stats['Name'] + 's Health: ' + str(start_stats['Health']))				
			if opp_choice == 'heal':
				opp_stats['Health'] = opp_stats['Health'] + round((random.choice(opp_moves['heal'])))
				print('\n' + opp_stats['Name'] + ' used heal\n')
				print(start_stats['Name'] + 's Health: ' + str(start_stats['Health']))
				if start_stats['Health'] <= 0:
					print(opp_stats['Name'] + 's Health: ' + str(0) + '\n')
				else:		
					print(opp_stats['Name'] + 's Health: ' + str(opp_stats['Health']) + '\n')

			if opp_choice == 'surf':
				if start_stats['Element'] == 'Fire':
					start_stats['Health'] = start_stats['Health'] - round((random.choice(opp_moves['surf'])*eff))
					print('\n' + opp_stats['Name'] + ' used surf')
					if start_stats['Health'] <= 0:
						print('\n' + start_stats['Name'] + 's Health: ' + str(0))
					else:		
						print('\n' + start_stats['Name'] + 's Health: ' + str(start_stats['Health']))
				elif start_stats['Element'] == 'Grass':
					start_stats['Health'] = start_stats['Health'] - round((random.choice(opp_moves['surf'])*non_eff))
					print('\n' + opp_stats['Name'] + ' used surf')
					if start_stats['Health'] <= 0:
						print('\n' + start_stats['Name'] + 's Health: ' + str(0))
					else:		
						print('\n' + start_stats['Name'] + 's Health: ' + str(start_stats['Health']))
				else:
						start_stats['Health'] = start_stats['Health'] - round((random.choice(opp_moves['surf'])))
						print('\n' + opp_stats['Name'] + ' used surf')
						if start_stats['Health'] <= 0:
							print('\n' + start_stats['Name'] + 's Health: ' + str(0))
						else:		
							print('\n' + start_stats['Name'] + 's Health: ' + str(start_stats['Health']))
			if opp_choice == 'waterpulse':
				if start_stats['Element'] == 'Fire':
					start_stats['Health'] = start_stats['Health'] - round((random.choice(opp_moves['waterpulse'])*eff))
					print('\n' + opp_stats['Name'] + ' used waterpulse')
					if start_stats['Health'] <= 0:
						print('\n' + start_stats['Name'] + 's Health: ' + str(0))
					else:		
						print('\n' + start_stats['Name'] + 's Health: ' + str(start_stats['Health']))
				elif start_stats['Element'] == 'Grass':
					start_stats['Health'] = start_stats['Health'] - round((random.choice(opp_moves['waterpulse'])*non_eff))
					print('\n' + opp_stats['Name'] + ' used waterpulse')
					if start_stats['Health'] <= 0:
						print('\n' + start_stats['Name'] + 's Health: ' + str(0))
					else:		
						print('\n' + start_stats['Name'] + 's Health: ' + str(start_stats['Health']))
				else:
					start_stats['Health'] = start_stats['Health'] - round((random.choice(opp_moves['waterpulse'])))
					print('\n' + opp_stats['Name'] + ' used waterpulse')
					if start_stats['Health'] <= 0:
						print('\n' + start_stats['Name'] + 's Health: ' + str(0))
					else:	
						print('\n' + start_stats['Name'] + 's Health: ' + str(start_stats['Health']))					
			if opp_choice == 'flamethrower':
				if start_stats['Element'] == 'Grass':
					start_stats['Health'] = start_stats['Health'] - round((random.choice(opp_moves['flamethrower'])*eff))
					print('\n' + opp_stats['Name'] + ' used flamethrower')
					if start_stats['Health'] <= 0:
						print('\n' + start_stats['Name'] + 's Health: ' + str(0))
					else:
						print('\n' + start_stats['Name'] + 's Health: ' + str(start_stats['Health']))
				elif start_stats['Element'] == 'Water':
					start_stats['Health'] = start_stats['Health'] - round((random.choice(opp_moves['flamethrower'])*non_eff))
					print('\n' + opp_stats['Name'] + ' used flamethrower')
					if start_stats['Health'] <= 0:
						print('\n' + start_stats['Name'] + 's Health: ' + str(0))
					else:
						print('\n' + start_stats['Name'] + 's Health: ' + str(start_stats['Health']))
				else:
					start_stats['Health'] = start_stats['Health'] - round((random.choice(opp_moves['flamethrower'])))
					print('\n' + opp_stats['Name'] + ' used flamethrower')
					if start_stats['Health'] <= 0:
						print('\n' + start_stats['Name'] + 's Health: ' + str(0))
					else:
						print('\n' + start_stats['Name'] + 's Health: ' + str(start_stats['Health']))
			if opp_choice == 'fireblast':
				if start_stats['Element'] == 'Grass':
					start_stats['Health'] = start_stats['Health'] - round((random.choice(opp_moves['fireblast'])*eff))
					print('\n' + opp_stats['Name'] + ' used fireblast')
					if start_stats['Health'] <= 0:
						print('\n' + start_stats['Name'] + 's Health: ' + str(0))
					else:
						print('\n' + start_stats['Name'] + 's Health: ' + str(start_stats['Health']))						
				elif start_stats['Element'] == 'Water':
					start_stats['Health'] = start_stats['Health'] - round((random.choice(opp_moves['fireblast'])*non_eff))
					print('\n' + opp_stats['Name'] + ' used fireblast')
					if start_stats['Health'] <= 0:
						print('\n' + start_stats['Name'] + 's Health: ' + str(0))
					else:
						print('\n' + start_stats['Name'] + 's Health: ' + str(start_stats['Health']))
				else:
					start_stats['Health'] = start_stats['Health'] - round((random.choice(opp_moves['fireblast'])))
					print('\n' + opp_stats['Name'] + ' used fireblast')
					if start_stats['Health'] <= 0:
						print('\n' + start_stats['Name'] + 's Health: ' + str(0))
					else:
						print('\n' + start_stats['Name'] + 's Health: ' + str(start_stats['Health']))
			if opp_choice == 'razorleaf':
				if start_stats['Element'] == 'Water':
					start_stats['Health'] = start_stats['Health'] - round((random.choice(opp_moves['razorleaf'])*eff))
					print('\n' + opp_stats['Name'] + ' used razorleaf')
					if start_stats['Health'] <= 0:
						print('\n' + start_stats['Name'] + 's Health: ' + str(0))
					else:
						print('\n' + start_stats['Name'] + 's Health: ' + str(start_stats['Health']))
				elif start_stats['Element'] == 'Fire':
					start_stats['Health'] = start_stats['Health'] - round((random.choice(opp_moves['razorleaf'])*non_eff))
					print('\n' + opp_stats['Name'] + ' used razorleaf')
					if start_stats['Health'] <= 0:
						print('\n' + start_stats['Name'] + 's Health: ' + str(0))
					else:
						print('\n' + start_stats['Name'] + 's Health: ' + str(start_stats['Health']))
				else:
					start_stats['Health'] = start_stats['Health'] - round((random.choice(opp_moves['razorleaf'])))
					print('\n' + opp_stats['Name'] + ' used razorleaf')
					if start_stats['Health'] <= 0:
						print('\n' + start_stats['Name'] + 's Health: ' + str(0))
					else:
						print('\n' + start_stats['Name'] + 's Health: ' + str(start_stats['Health']))
			if opp_choice == 'absorb':
				if start_stats['Element'] == 'Water':
					start_stats['Health'] = start_stats['Health'] - round((random.choice(opp_moves['absorb'])*eff))
					print('\n' + opp_stats['Name'] + ' used absorb')
					if start_stats['Health'] <= 0:
						print('\n' + start_stats['Name'] + 's Health: ' + str(0))
					else:
						print('\n' + start_stats['Name'] + 's Health: ' + str(start_stats['Health']))
				elif start_stats['Element'] == 'Fire':
					start_stats['Health'] = start_stats['Health'] - round((random.choice(opp_moves['absorb'])*eff))
					print('\n' + opp_stats['Name'] + ' used absorb')
					if start_stats['Health'] <= 0:
						print('\n' + start_stats['Name'] + 's Health: ' + str(0))
					else:
						print('\n' + start_stats['Name'] + 's Health: ' + str(start_stats['Health']))
				else:
					start_stats['Health'] = start_stats['Health'] - round((random.choice(opp_moves['absorb'])))
					print('\n' + opp_stats['Name'] + ' used absorb')
					if start_stats['Health'] <= 0:
						print('\n' + start_stats['Name'] + 's Health: ' + str(0))
					else:
						print('\n' + start_stats['Name'] + 's Health: ' + str(start_stats['Health']))
			if opp_choice == 'thunderbolt':
				if start_stats['Element'] == 'Water':
					start_stats['Health'] = start_stats['Health'] - round((random.choice(opp_moves['thunderbolt'])*eff))
					print('\n' + opp_stats['Name'] + ' used thunderbolt')
					if start_stats['Health'] <= 0:
						print('\n' + start_stats['Name'] + 's Health: ' + str(0))
					else:
						print('\n' + start_stats['Name'] + 's Health: ' + str(start_stats['Health']))
				else:
					start_stats['Health'] = start_stats['Health'] - round((random.choice(opp_moves['thunderbolt'])))
					print('\n' + opp_stats['Name'] + ' used thunderbolt')
					if start_stats['Health'] <= 0:
						print('\n' + start_stats['Name'] + 's Health: ' + str(0))
					else:
						print('\n' + start_stats['Name'] + 's Health: ' + str(start_stats['Health']))
			if opp_choice == 'thunder':
				if start_stats['Element'] == 'Water':
					start_stats['Health'] = start_stats['Health'] - round((random.choice(opp_moves['thunder'])*eff))
					print('\n' + opp_stats['Name'] + ' used thunder')
					if start_stats['Health'] <= 0:
						print('\n' + start_stats['Name'] + 's Health: ' + str(0))
					else:
						print('\n' + start_stats['Name'] + 's Health: ' + str(start_stats['Health']))
				else:
					start_stats['Health'] = start_stats['Health'] - round((random.choice(opp_moves['thunder'])))
					print('\n' + opp_stats['Name'] + ' used thunder')
					if start_stats['Health'] <= 0:
						print('\n' + start_stats['Name'] + 's Health: ' + str(0))
					else:
						print('\n' + start_stats['Name'] + 's Health: ' + str(start_stats['Health']))					
	#If the players Pokemon runs out of hp tell the player to restart the game					
	while start_stats['Health'] <= 0:
		print(Start_stats['Name'] + ' has fainted' +'\nYou Pokemon has fainted and is no longer able to fight')
		input('Restart the game')
		

#Zigzagoon name and stats for intro battle

Zigzagoon_stats = {'Name':'Zigzagoon','Health': 70}
opp_moves = {"tackle": range(20,23), "heal": range(5,10)}

print("\nYou chose " + Start_stats['Name'])
print(Start_stats['Name'] + " is a " + Start_stats['Element'] + " type")
print("\nA wild Pokemon appears...")
print("It's a wild zigzagoon!")


#import fight sequence for Zizagoon
battles(Start_stats, Zigzagoon_stats)
print('Zigzagoon has fainted\n')


#Say starter pokemon gains exp
print(Start_stats['Name'] + " has gained 100 experiences points and leveled up!")

#Say starter pokemon has upgraded to a stronger move!
print(Start_stats['Name'] + " has upgraded tackle to bodyslam!")
del moves["tackle"]
moves["bodyslam"] = (range(24,28))

#Say starter pokemon has learned a new move!
print(Start_stats['Name'] + " has learned a new move!")
if Start_stats['Name'] == 'Squirtle':
	moves["watergun"] = range(22,25)
if Start_stats['Name'] == 'Bulbasaur':	
	moves["vinewhip"] = range(22,25)
if Start_stats['Name'] == 'Charmander':	
	moves["ember"] = range(22,25)
if  Start_stats["Element"] == 'Fire':
	print(Start_stats['Name'] + " has learned Ember!")
if Start_stats["Element"] == 'Grass':
	print(Start_stats['Name'] + " has learned Vine Whip!")
if Start_stats["Element"] == 'Water':
	print(Start_stats['Name'] + " has learned Water Gun!")


#Change Starter Attack Multiplier to 1.2
att_multi = 1.2

#Congratulate trainer
print("\n'Congratulations trainer on your first win! You don't get a badge but maybe you'll get a cookie...'")

#Go to pokemon centre
print("\nYour pokemon went to the pokemon centre to get some rest. It will be healed for the next battle!")

continue_1 = input("\nDo you wish to continue to the next gym? Type yes to continue: ")
while continue_1 != "yes":
	continue_1 = input("\nDo you wish to continue to the next gym? Type �yes� to continue: ")
if continue_1 == "yes":
	#Change Starter Pokemon's Health to 150
	Start_stats["Health"] = 135
    
    
#Write down text for first gym battle (Normal) two pokemon
print("\nYou enter the first gym and meet the gym leader")
print("\n'Hello trainer, the names Sokka. Nice to meet cha�!'")
print("Gym leader Sokka sent out Jigglypuff\n")
    
#pokemon and moveset
Jigglypuff_stats= {'Name': 'Jigglypuff', "Health": 75, "Element": 'Normal'}
opp_moves= {"tackle": range(20,23), "heal": range(15,20), "headbutt": range(22,25), "takedown": range(24,26)}



#import fight sequence for Jigglypuff
battles(Start_stats, Jigglypuff_stats)
#Once pokemon is dead, send out next pokemon
print("Jigglypuff fainted. Gym leader Sokka sent out Clefairy")

Clefairy_stats= {'Name': 'Clefairy',"Health": 100, "Element": 'Normal'}
opp_moves= {"tackle": range(20,23), "heal": range(15,20), "headbutt": range(22,25), "takedown": range(24,26)}


#Import fight sequence for Clefairy
battles(Start_stats, Clefairy_stats)
#Once Clefairy is dead
print("Clefairy fainted. Gym leader Sokka has run out of usable pokemons. Trainer wins!\n")

#Say starter pokemon gains exp
print(Start_stats['Name'] + " has gained 100 experiences points")



#Change Starter Attack Multiplier to 1.5
att_multi = 1.5

#Congratulate trainer
print("Congratulations trainer! Wow I lost, just like I lost my girl to the moon. Here's your first badge!\n")

#Go to pokemon centre
print("Your pokemon went to the pokemon centre to get some rest. It will be healed for the next battle!")

#ask if you trainer wants to move to next gym
continue_2 = input("Do you wish to continue to the next gym? Type yes to continue: ")
while continue_2 != "yes":
	continue_2 = input("Do you wish to continue to the next gym? Type �yes� to continue: ")
if continue_2 == "yes":
	#Change Starter Pokemon's Health to 150
	Start_stats["Health"] = 170
  
#Move onto second gym battle (water) two pokemon
print("\nYou enter the next gym and meet the gym leader: Kataara ")
print("Surf's up brah, ready for a knarly battle and hit that wave?")
print("\nGym leader Kataara sent out Staryu")

#pokemon and moveset
Staryu_stats= {'Name': 'Staryu',"Health": 125, "Element": 'Water'}
opp_moves= {"tackle": range(20,23), "heal": range(15,20), "surf": range(22,25), "waterpulse": range(24,26)}


#Import fight sequence for staryu
battles(Start_stats, Staryu_stats)
#Once staryu is dead
print("Staryu fainted. Gym leader Kataara sent out Horsea")

Horsea_stats= {'Name': 'Horsea', "Health":150, "Element": 'Water'}
opp_moves= {"tackle": range(20,23), "heal": range(15,20), "surf": range(22,25), "waterpulse": range(24,26)}


#Import fight sequence for horsea
battles(Start_stats, Horsea_stats)

print("Horsea fainted. Gym leader Kataara has run out of usable pokemons. Trainer wins!\n")

#Evolve starter pokemon
print(Start_stats['Name'] + " has gained 100 experiences points")
print("Oh! " + Start_stats['Name'] + " is evolving!")

if Start_stats['Name'] == "Bulbasaur":
	Start_stats['Name'] = "Ivysaur"
if Start_stats['Name'] == "Charmander":
	Start_stats['Name'] = "Charmeleon"
if Start_stats['Name'] == "Squirtle":
	Start_stats['Name'] = "Wartortle"

print("Congratulations! Your starter evolved into " + Start_stats['Name'])
#Give starter pokemon a new move!
if Start_stats['Name'] == "Wartortle":
	moves["hydropump"]= range(24,28)
if Start_stats['Name'] == "Ivysaur":
	moves["solarbeam"]= range(24,28)
if Start_stats['Name'] == "Charmeleon":
	moves["firefang"]= range(24,28) 
#Say starter pokemon has learned a new move!
if Start_stats['Element'] == 'Fire':
	print(Start_stats['Name'] + " has learned a new move!: Fire Fang!")
if Start_stats['Element'] == 'Grass':
	print(Start_stats['Name'] + " has learned a new move!: Solar Beam!")
if Start_stats['Element'] == 'Water':
	print(Start_stats['Name'] + " has learned a new move!: Hydropump!")

#Once Horsea is dead
print("\nHere's your 2nd badge brah. Keep riding that high wave and you can be the champ in no time!")


#Go to pokemon centre
print("\nYour pokemon went to the pokemon centre to get some rest. It will be healed for the next battle!")

#ask trainer if they want to move onto next gym
continue_3 = input("Do you wish to continue to the next gym? Type yes to continue: ")
while continue_3 != "yes":
	continue_3 = input("Do you wish to continue to the next gym? Type �yes� to continue: ")
if continue_3 == "yes":
	#Change Starter Pokemon's Health to 175
	Start_stats["Health"] = 210

#Change Starter Attack Multiplier to 1.8
att_multi = 1.8


#Move onto third gym battle (fire) three pokemon
print("\nYou enter the third gym and meet the gym leader Fire Lord Ozai")
print("Welcome to the next gym")
print("Gym leader sent out growlithe")

#pokemon and movesets
growlithe_stats= {'Name': 'Growlithe',"Health": 125, "Element": 'Fire'}
opp_moves= {"tackle": range(20,23), "heal": range(15,20), "flamethrower": range(22,25), "fireblast": range(24,26)}  


#Import fight sequence for Growlithe
battles(Start_stats, growlithe_stats)
#Once Growlithe is dead
print("Growlithe fainted. Gym leader Fire Lord Ozai sent out Arcanine")

arcanine_stats= {'Name': 'Arcanine',"Health": 150, "Element": 'Fire'}
opp_moves= {"tackle": range(20,23), "heal": range(15,20), "flamethrower": range(22,25), "fireblast": range(24,26)}


#Import fight sequence for Arcanine
battles(Start_stats, arcanine_stats)
#Once Arcanine is dead
print("Arcanine fainted. Gym leader Fire Lord Ozai sends out Magmar")

magmar_stats= {'Name': 'Magmar',"Health": 150, "Element": 'Fire'}
opp_moves= {"tackle": range(20,23), "heal": range(15,20), "flamethrower": range(22,25), "fireblast": range(24,26)}


#Import fight sequence for Magmar
battles(Start_stats, magmar_stats)

#Once Magmar is dead
print("Magmar fainted. Gym Leader Fire Lord Ozai has run out of usable pokemons. Trainer wins!")
print(Start_stats['Name'] + " has gained 150 experiences points\n")

print("Here's your 3rd badge brah. Mans not hot...MANS NEVER HOT. Keep this up and you'll even conquer the fire nation!\n")  

#Change Starter Attack Multiplier to 2.0
att_multi = 2.0

#Go to pokemon centre
print("Your pokemon went to the pokemon centre to get some rest. It will be healed for the next battle!")

#ask trainer if they want to move onto next gym
continue_4 = input("Do you wish to continue to the next gym? Type yes to continue: ")
while continue_4 != "yes":
	continue_4 = input("Do you wish to continue to the next gym? Type �yes� to continue: ")
if continue_4 == "yes":
	#Change Starter Pokemon's Health to 200
	Start_stats["Health"] = 250

#Move onto third gym battle (grass) three pokemon
print("\nYou enter the third gym and meet the gym leader: Toph ")
print("Welcome to the next gym")
print("Gym leader Toph sent out Victreebel")

#pokemon and movesets
victreebel_stats= {'Name': 'Victreebel',"Health": 150, 'Element': 'Grass'}
opp_moves= {"tackle": range(20,23), "heal": range(15,20), "razorleaf": range(24,26), "absorb": range(22,25)}  



#Import fight sequence for Victreebel
battles(Start_stats, victreebel_stats)
#Once Victreebel is dead
print("Victreebel fainted. Gym leader Toph sent out Vileplume")

vileplume_stats= {'Name': 'Vileplume',"Health": 150, 'Element': 'Grass'}
opp_moves= {"tackle": range(20,23), "heal": range(15,20), "razorleaf": range(24,26), "absorb": range(22,25)}  


#Import fight sequence for Vileplume
battles(Start_stats, vileplume_stats)
#Once Vileplume is dead
print("Vileplume fainted. Gym leader Toph sent out Tangela")

tangela_stats= {'Name': 'Tangela',"Health": 175, 'Element': 'Grass'}
opp_moves= {"tackle": range(20,23), "heal": range(15,20), "razorleaf": range(24,26), "absorb": range(22,25)}  


#Import fight sequence for Tangela
battles(Start_stats, tangela_stats)

#Once Tangela is dead
print("Tangela fainted. Gym Leader Toph has run out of usable pokemons. Trainer wins!\n")
print(Start_stats['Name'] + " has gained 200 experience points\n")

#Change Starter Attack Multiplier to 2.2
att_multi = 2.5

#Evolve starter pokemon
print("Oh! " + Start_stats['Name'] + " is evolving!")

if Start_stats['Name'] == "Ivysaur":
	Start_stats['Name'] = "Venusaur"
if Start_stats['Name'] == "Charmeleon":
	Start_stats['Name'] = "Charizard"
if Start_stats['Name'] == "Wartortle":
	Start_stats['Name'] = "Blastoise"

#Give starter pokemon a new move!
moves["EARFQUAKE"]= range(24,28)

#Say starter pokemon has learned a new move!
print(Start_stats['Name'] + " has learned a new move!: EARFQUAKE!\n")

#Give trainer their badge
print("Nice win...I think. I dunno I can't see. But I can feel your vibrations so take this badge!")

#Go to pokemon centre
print("\nYour pokemon went to the pokemon centre to get some rest. It will be healed for the next battle!")

#ask trainer if they want to move onto next gym
continue_5 = input("Do you wish to continue to the next gym? Type yes to continue: ")
while continue_5 != "yes":
	continue_5 = input("Do you wish to continue to the next gym? Type �yes� to continue: ")
if continue_5 == "yes":
	#Change Starter Pokemon's Health to 300
	Start_stats["Health"] = 300

#Move onto fourth gym battle (electric) four pokemon
print("\nYou enter the fifth gym and meet the gym leader: Azula ")
print("Welcome to the next gym")
print("Gym leader Azula sent out pikachu\n")

#pokemon and movesets
pikachu_stats= {"Name": 'Pikachu', "Health": 250, 'Element': 'Electric'}
opp_moves= {"tackle": range(20,23), "heal": range(15,20), "thunderbolt": range(22,25), "thunder": range(24,26)}  


electabuzz_stats= {"Name": 'Electabuzz',"Health": 250, 'Element': 'Electric'}
opp_moves= {"tackle": range(20,23), "heal": range(15,20), "thunderbolt": range(22,25), "thunder": range(24,26)}  


electrode_stats= {"Name": 'Electrode', "Health": 250, 'Element': 'Electric'}
opp_moves= {"tackle": range(20,23), "heal": range(15,20), "thunderbolt": range(22,25), "thunder": range(24,26)}  


    
raichu_stats= {"Name": 'Raichu',"Health": 300, 'Element': 'Electric'}
opp_moves= {"tackle": range(20,23), "heal": range(15,20), "thunderbolt": range(22,25), "thunder": range(24,26)}


#Import fight sequence for Pikachu
battles(Start_stats, pikachu_stats)

#Once Pikachu is dead
print("Pikachu fainted. Gym leader Azula sent out electabuzz")

#Import fight sequence for electabuzz
battles(Start_stats, electabuzz_stats)

#Once electabuzz is dead
print("Electabuzz fainted. Gym leader Azula sent out Electrode")

#Import fight sequence for electrode
battles(Start_stats, electrode_stats)

#Once electrode is dead
print("Electrode fainted. Gym leader Azula sent out Raichu")

#Import fight sequence for Raichu
battles(Start_stats, raichu_stats)

#Once Raichu is dead
print("Raichu fainted. Gym leader Azula has run out of usable pokemons. Trainer wins!")
print(Start_stats['Name'] + " has gained 9999 experiences points")
print("Here's your 5th badge brah. Such an electrifying win! Shocking to see you become the champion!!!")
print('\nYOU WON THE GAME CONGRATULATION')