# Responses
answer_Noord = ["Noord", "noord", "N", "n"]
answer_Zuid = ["Zuid", "zuid", "Z", "z"]
answer_West = ["West", "west", "W", "w"]
answer_Oost = ["Oost", "oost", "O", "o"]
yes = ["J", "j", "ja", "Ja", "JA", "jA"]
no = ["N", "n", "nee", "Nee", "NEE", "NEe", "NeE"]

# imports
from replit import db
import time

# Menu Naam
def return1():
  naam()

def naam():
  nvalue = db["naam"]
  snaam = nvalue
  if nvalue == False:
    print ("˃ Hallo avonturier wat is uw naam?")
    naam = input("► ")
    db["naam"] = naam
    snaam = naam
    return
  else :
    print("˃ Wil je je huidige naam houden " + nvalue + "?")
    anwstart = input("► ")
    if anwstart in no :
      print("˃ Geef je nieuwe naam op:")
      niewstart = input("► ")
      db["naam"] = niewstart
      return
    if anwstart in yes :
      print("˃ Welkom terug succes hopelijk overleef je het avontuur " + nvalue)
      return
    else :
      print("˃ Verkeerde input probeer het opnieuw")
      time.sleep(2)
      return1()

naam()

# Start Game
def start(): 
  naam = db["naam"]
  time.sleep(1)
  print("˃ Gegroet, " + naam + " Klaar voor een avontuur?")
  klaar = input("► ")
  if klaar in yes :
    return
  if klaar in no :
    print("Goodby Daddy!")
    exit()
  else :
    print("Verkeerde Input!!")
    start()

start()

room_list = []
inventory = []

# -- First Room (0)
room = ["Twilight wakes up in the canterlot catacombs with a acking headache. \n there are crystalized paths leading North, East, South, or West.", 6, 3, 1, 4]
room_list.append(room)
# -- Flower Garden (1)
room = ["You stumble across a flower garden. Admiring their lavasting beauty, you pick one up, just for keeps. \n you can go North, East, or West", 0, 5, None, 2]
room_list.append(room)
# -- Icy Hallway (2)
room = ["Hallway, cold, freezing, must find cadence, leave, quick. \n Go North or East", 4, 1, None, None]
room_list.append(room)
# -- Cadence! (3)
room = ["It's Cadence!. Cadence joins you on your quest to escape the Canterlot Catacombs. \n You can go South or West from here", None, None, 5, 0]
room_list.append(room)
# -- Hallway 2 (4)
room =["You come across a hallway with green orbs attached to the ceiling. It appears to have ponies inside of them, but without magic, you are unable to save them. \n go East or South", None, 0, 2, None]
room_list.append(room)
# -- Challenging room (5)
room = ["As you walk across to the next room, you start to notice the light to darken. you find a challenging devouring the love of another pony. You leave it undistrubed and continue fourth. You can go North or West", 3, None, None, 1]
room_list.append(room)
# -- Railroad(6)
room = ["You and Cadence Both leave the catacombs safely and make it to the wedding on time. You may go south!", None, None, 0, None]
room_list.append(room)



# -- Starting Point
current_room = 0

# -- Main Loop
done = False
while not done:
		print(room_list[current_room][0])
		userinput = input("Which way? ")
		# -- Quit
		if userinput.upper() == "Q":
			exit()
		# -- Go North
		elif userinput.upper() == "N":
			next_room = room_list[current_room][1]
			if next_room == None:
				print ("You can't go that way!")
			else:
				current_room = next_room
		# -- Go East
		elif userinput.upper() == "E":
			next_room = room_list[current_room][2]
			if next_room == None:
				print ("You can't go that way!")
			else:
				current_room = next_room
		# - Go South
		elif userinput.upper() == "S":
			next_room = room_list[current_room][3]
			if next_room == None:
				print ("You can't go that way!")
			else:
				current_room = next_room
		# - Go West
		elif userinput.upper() == "W":
			next_room = room_list[current_room][4]
			if next_room == None:
				print ("You can't go that way!")
			else:
				current_room = next_room