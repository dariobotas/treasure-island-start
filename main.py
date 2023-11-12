print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
print("Your ship has run into a \nstorm during the night.\nFear can be sensed in all crew members. You are capsized in the darkness, and awake the next day.")
print("You have no idea where you are, and you don't see any other land closeby, you have some choices to make...")

choice1 = input(" A) You decide to stay with the remaining part of the ship and wait to be rescued\n B) You decide to explore the island\n C) You decide to wait on the beach for help by writing S.O.S in the sand\n What's your choice? A, B or C:\n").lower()

if choice1 == "a":
  print("Since you decided to stay with the ship...")
  print("You were the only able to survive on week without water, and no help came...")
  print("Game over!")
elif choice1 == "b":
  print("Since you explored the island...")
  print("You've found a map leading you to different supplies!!!")
  print("Choose to find one of the following supplies that would help you survive...")
  choice2 = input(" A) Compass\n B) Rope\n C) Knife\n").lower()
  if choice2 == "a":
    print("Since you used the compass...")
    print("You have navigated to Isla de LaJuventud without any food and water. Explore the Isla and come up with a way to survive!")
    choice2_1 = input("Do you want to explore the Isla? Y (for Yes) or N (for No) \n").lower()
    if choice2_1 == "y":
      print("Explore was the choice you made...")
      print("As you walk island, you notice that your group is not alone.")
      print("You have the feeling that someone's eyes are on every movement you make.")
      print('"It must be the nerver," you tell yourself. But your first instincts are rigth.')
      print("There, right behind the steep hill, danger awaits. You mus decide to...")
      choice2_1_1 = input("A) Go with your gut, or\nB) Be brave and confront what is ahead\n").lower()
      if choice2_1_1 == "a":
        print("Go with your gut and retrieve")
        print("The unknown is frightening. Therefore you encourage everyone to retrieve. Unfortunately, not everyone agrees with you and the rest of the group decides do move on without you.")
        print("You are returning by yourself to the shore. Where you find the unexpected.")
        print("HELP HAS ARRIVED!")
        print("You survived the crash, built a shelter, found sutenance, and escaped Vane. You learn the importance the importance of collaboration and building positive relationships. Best of all you FOUND THE TREASURE!\nYou win!!")
      else:
        print("You have chosen to be brave and confront what is ahead...")
        print("You know that you are not alone, but staying behind is not an option for survival.")
        print("You need food and shelter.")
        print("You continue to walk cautiously...")
        print("Along the way, you see something in the ocean, two mermaids.")
        print("You greet the mermaids and, strike up a conversation.\nYou ask them about the island. You find out that there is a compass that will lead you to other inhabitants of the island.")
        choice2_1_1_1 = input("A) You choose to search for the compass\nB) You ignore the mermaids and continue on\n").lower()
        if choice2_1_1_1 == "a":
          print("You fall for a trap and die!")
          print("Game over!")
        else:
          print("After ignoring the mermaids...")
          print("You search deeper in the interior of the island. After several hours you are exhausted, and collapse on a comfortable rock.")
          print("You suddenly wake up with a knife at your throat.")
          print("Your former captain, Vane the Bastard, yells at you to get up and follow him. You can..")
          choice2_1_1_1_1 = input("A) Follow him\nB)Refuse\n").lower()
          if choice2_1_1_1_1 == "a":
            print("Following Vane the Bastard")
            print("You accept that Vane the Bastard is not a fellow to be trifled with. He leads you into the forest beyond the hills. Grumbling about his lost treasure. You know you can't trust this man, but no one who has crossed him has ever lived to tell the tal.")
            print("As time passes, you become thirsty.")
            print("Your own knife sits in your pocket, hidden from view. Do you...")
            choice2_1_1_1_1_1 = input("A) Attempt to attack Vane?\nB) Ask him to stop so you can get some water from the nearby stream?\n").lower()
            if choice2_1_1_1_1_1 == "a":
              print("Attempt to attack Vane the Bastard...")
              print("You reach into your pocket when you think Vane isn't looking, and leap onto his back.")
              print("You manage to stab him in the shoulder.")
              print("He screams, but shakes you off and kneels on your throat. His knife is out faster than you can blink.")
              print("As he stabs through your throat, you wonder if you should have made better CHOICES!")
              print("Game over!")
            else:
              print("Once you get the stream to take a drink you see an underwater cave that leads into a tunnel.")
              print('"This is exactly where i need to be!" shouts Vane, and he plunges deeper into the darkness.')
              print("He senses your hesitancy, and grabs you by the throat, his grimy hands like a vise. You have no choice but to follow him.")
              print("Once Vane has brought you into underground cavern..")
              print("You see a stash of booty, but you also see that it lies across a very frail rope bridge, underneath of which is an abyss. Vane demands that you cross the bridge, but you know that it will lead to your certain doom.")
              choice2_1_1_1_1_1_2 = input("You can...\nA) Choose to refuse him\nB) Follow his orders. Vane doesn't know you have a knife of your own, however...\n").lower()
              if choice2_1_1_1_1_1_2 == "a":
                print("Refusing Vane the Bastard")
                print("'No one refuses Vane the Bastard and lives!' He cries and stabs you in the throat before you can blink. As you lifeblood gushes onto the dark earth, you regret your life choices and ponder whether reincarnation is real, or if heaven awaits. Or Hell...")
                print("Game over!")
          else:
            print("After you cross the rope bridge...")
            print("You signal Vane to cross the bridge. You can then either choose to..")
            choice2_1_1_1_1_1_2_2 = input("A) Let him across\nB) Attempt to cut the bridge as he crosses with your own knife\n").lower()
            if choice2_1_1_1_1_1_2_2 == "a":
              print("You let Vane cross the rope bridge...")
              print("And as soon as he is across, he laughs, claps you on the back, and shoves you over the abyss. As you fall into eternity, you wonder if you should have made better choices...")
              print("Game over!")
            else:
              print("While cutting the rope...")
              print("Vane pleads with not to kill him by sending him into the abyss. You have a moment to think, you know you can't trust him and you decide to sever the ropes.")
              print("As he plunges to his doom, his screams echo throughout the cavern.\n You laugh, and turn to face the treasure.")
              print("You found the treasure and help arrives!!\nYou win!!")
    else:
      print("Since you didn't explore the Isla, you didn't came up with a way to survive and die!")
      print("Game over!")
  elif choice2 == "b":
    print("You decided to choose the rope...")
    print("Way to go!")
    print("Having the rope will be a great tool when it comes to making a shelter!")
    print("Some mermaids notice your new shelter on the shore...")
    print("Along the way you see someting in the ocean, two mermaids")
    print("You greet the mermaids and, strike up a conversation.\nYou ask them about the island. You find out that there is a compass that will lead you to other inhabitants of the island.")
    choice2_1_1_1 = input("A) You choose to search for the compass\nB) You ignore the mermaids and continue on\n").lower()
    if choice2_1_1_1 == "a":
      print("You fall for a trap and die!")
      print("Game over!")
    else:
      print("After ignoring the mermaids...")
      print("You search deeper in the interior of the island. After several hours you are exhausted, and collapse on a comfortable rock.")
      print("You suddenly wake up with a knife at your throat.")
      print("Your former captain, Vane the Bastard, yells at you to get up and follow him. You can..")
      choice2_1_1_1_1 = input("A) Follow him\nB)Refuse\n").lower()
      if choice2_1_1_1_1 == "a":
        print("Following Vane the Bastard")
        print("You accept that Vane the Bastard is not a fellow to be trifled with. He leads you into the forest beyond the hills. Grumbling about his lost treasure. You know you can't trust this man, but no one who has crossed him has ever lived to tell the tal.")
        print("As time passes, you become thirsty.")
        print("Your own knife sits in your pocket, hidden from view. Do you...")
        choice2_1_1_1_1_1 = input("A) Attempt to attack Vane?\nB) Ask him to stop so you can get some water from the nearby stream?\n").lower()
        if choice2_1_1_1_1_1 == "a":
          print("Attempt to attack Vane the Bastard...")
          print("You reach into your pocket when you think Vane isn't looking, and leap onto his back.")
          print("You manage to stab him in the shoulder.")
          print("He screams, but shakes you off and kneels on your throat. His knife is out faster than you can blink.")
          print("As he stabs through your throat, you wonder if you should have made better CHOICES!")
          print("Game over!")
        else:
          print("Once you get the stream to take a drink you see an underwater cave that leads into a tunnel.")
          print('"This is exactly where i need to be!" shouts Vane, and he plunges deeper into the darkness.')
          print("He senses your hesitancy, and grabs you by the throat, his grimy hands like a vise. You have no choice but to follow him.")
          print("Once Vane has brought you into underground cavern..")
          print("You see a stash of booty, but you also see that it lies across a very frail rope bridge, underneath of which is an abyss. Vane demands that you cross the bridge, but you know that it will lead to your certain doom.")
          choice2_1_1_1_1_1_2 = input("You can...\nA) Choose to refuse him\nB) Follow his orders. Vane doesn't know you have a knife of your own, however...\n").lower()
          if choice2_1_1_1_1_1_2 == "a":
            print("Refusing Vane the Bastard")
            print("'No one refuses Vane the Bastard and lives!' He cries and stabs you in the throat before you can blink. As you lifeblood gushes onto the dark earth, you regret your life choices and ponder whether reincarnation is real, or if heaven awaits. Or Hell...")
            print("Game over!")
          else:
            print("After you cross the rope bridge...")
            print("You signal Vane to cross the bridge. You can then either choose to..")
            choice2_1_1_1_1_1_2_2 = input("A) Let him across\nB) Attempt to cut the bridge as he crosses with your own knife\n").lower()
            if choice2_1_1_1_1_1_2_2 == "a":
              print("You let Vane cross the rope bridge...")
              print("And as soon as he is across, he laughs, claps you on the back, and shoves you over the abyss. As you fall into eternity, you wonder if you should have made better choices...")
              print("Game over!")
            else:
              print("While cutting the rope...")
              print("Vane pleads with not to kill him by sending him into the abyss. You have a moment to think, you know you can't trust him and you decide to sever the ropes.")
              print("As he plunges to his doom, his screams echo throughout the cavern.\n You laugh, and turn to face the treasure.")
              print("You found the treasure and help arrives!!\nYou win!!")
  elif choice2 == "c":
    print("You have decided to find the knife...")
    print("Very wise decision, because it will help you as you seek for food.")
    print("Since you were able to find sustenance, you survived another week.")
    print("Along the way you see someting in the ocean, two mermaids")
    print("You greet the mermaids and, strike up a conversation.\nYou ask them about the island. You find out that there is a compass that will lead you to other inhabitants of the island.")
    choice2_1_1_1 = input("A) You choose to search for the compass\nB) You ignore the mermaids and continue on\n").lower()
    if choice2_1_1_1 == "a":
      print("You fall for a trap and die!")
      print("Game over!")
    else:
      print("After ignoring the mermaids...")
      print("You search deeper in the interior of the island. After several hours you are exhausted, and collapse on a comfortable rock.")
      print("You suddenly wake up with a knife at your throat.")
      print("Your former captain, Vane the Bastard, yells at you to get up and follow him. You can..")
      choice2_1_1_1_1 = input("A) Follow him\nB)Refuse\n").lower()
      if choice2_1_1_1_1 == "a":
        print("Following Vane the Bastard")
        print("You accept that Vane the Bastard is not a fellow to be trifled with. He leads you into the forest beyond the hills. Grumbling about his lost treasure. You know you can't trust this man, but no one who has crossed him has ever lived to tell the tal.")
        print("As time passes, you become thirsty.")
        print("Your own knife sits in your pocket, hidden from view. Do you...")
        choice2_1_1_1_1_1 = input("A) Attempt to attack Vane?\nB) Ask him to stop so you can get some water from the nearby stream?\n").lower()
        if choice2_1_1_1_1_1 == "a":
          print("Attempt to attack Vane the Bastard...")
          print("You reach into your pocket when you think Vane isn't looking, and leap onto his back.")
          print("You manage to stab him in the shoulder.")
          print("He screams, but shakes you off and kneels on your throat. His knife is out faster than you can blink.")
          print("As he stabs through your throat, you wonder if you should have made better CHOICES!")
          print("Game over!")
        else:
          print("Once you get the stream to take a drink you see an underwater cave that leads into a tunnel.")
          print('"This is exactly where i need to be!" shouts Vane, and he plunges deeper into the darkness.')
          print("He senses your hesitancy, and grabs you by the throat, his grimy hands like a vise. You have no choice but to follow him.")
          print("Once Vane has brought you into underground cavern..")
          print("You see a stash of booty, but you also see that it lies across a very frail rope bridge, underneath of which is an abyss. Vane demands that you cross the bridge, but you know that it will lead to your certain doom.")
          choice2_1_1_1_1_1_2 = input("You can...\nA) Choose to refuse him\nB) Follow his orders. Vane doesn't know you have a knife of your own, however...\n").lower()
          if choice2_1_1_1_1_1_2 == "a":
            print("Refusing Vane the Bastard")
            print("'No one refuses Vane the Bastard and lives!' He cries and stabs you in the throat before you can blink. As you lifeblood gushes onto the dark earth, you regret your life choices and ponder whether reincarnation is real, or if heaven awaits. Or Hell...")
            print("Game over!")
          else:
            print("After you cross the rope bridge...")
            print("You signal Vane to cross the bridge. You can then either choose to..")
            choice2_1_1_1_1_1_2_2 = input("A) Let him across\nB) Attempt to cut the bridge as he crosses with your own knife\n").lower()
            if choice2_1_1_1_1_1_2_2 == "a":
              print("You let Vane cross the rope bridge...")
              print("And as soon as he is across, he laughs, claps you on the back, and shoves you over the abyss. As you fall into eternity, you wonder if you should have made better choices...")
              print("Game over!")
            else:
              print("While cutting the rope...")
              print("Vane pleads with not to kill him by sending him into the abyss. You have a moment to think, you know you can't trust him and you decide to sever the ropes.")
              print("As he plunges to his doom, his screams echo throughout the cavern.\n You laugh, and turn to face the treasure.")
              print("You found the treasure and help arrives!!\nYou win!!")
elif choice1 == "c":
  print("Since you decided to wait on the beach...")
  print("You were only able to use the supplies that you hauled from the ship. \nThe ship had some water and crackers that eventually became stale... You were able to live off these supplies for two weeks... you didn't have any shelter and became sadly sunburned, but were still surviving")
  print("Unfortunately help didn't come in time...")
  print("Game over!")