print('''Welcome to Lost in the Enchanted Forest:
88888888888                        88                                                           88    88888888888                                                  
88                                 88                                  ,d                       88    88                                                    ,d     
88                                 88                                  88                       88    88                                                    88     
88aaaaa     8b,dPPYba,   ,adPPYba, 88,dPPYba,  ,adPPYYba, 8b,dPPYba, MM88MMM ,adPPYba,  ,adPPYb,88    88aaaaa  ,adPPYba,  8b,dPPYba,  ,adPPYba, ,adPPYba, MM88MMM  
88"""""     88P'   `"8a a8"     "" 88P'    "8a ""     `Y8 88P'   `"8a  88   a8P_____88 a8"    `Y88    88""""" a8"     "8a 88P'   "Y8 a8P_____88 I8[    ""   88     
88          88       88 8b         88       88 ,adPPPPP88 88       88  88   8PP""""""" 8b       88    88      8b       d8 88         8PP"""""""  `"Y8ba,    88     
88          88       88 "8a,   ,aa 88       88 88,    ,88 88       88  88,  "8b,   ,aa "8a,   ,d88    88      "8a,   ,a8" 88         "8b,   ,aa aa    ]8I   88,    
88888888888 88       88  `"Ybbd8"' 88       88 `"8bbdP"Y8 88       88  "Y888 `"Ybbd8"'  `"8bbdP"Y8    88       `"YbbdP"'  88          `"Ybbd8"' `"YbbdP"'   "Y888   
''')
print("You find yourself deep within an enchanted forest, surrounded by towering trees and mystical creatures. As you explore, you come across a mysterious split on your path. Choose wisely!")
ready = input("Will you:\nA. Follow the winding , overgrown path .\nB. Take the dark and narrow tunnel to the right.\n").lower()
if ready == "b":
    print("\nYou are quite a brave fellow!! You go to the right dark tunnel where mysterious echoes and faint glimmers suggest hidden secrets. As you enter, the cool air sends shivers down your spine, and the tunnel seems to wind deeper into the heart of the forest.")
    ready = input("A. Attempt to cross the ancient bridge guarded by a wise old owl. \nB. Look for an alternative route to avoid the guardian.\n").lower()  
    if ready == "a":
        print("The owl  eyes you with curiosity and a hint of skepticism. The guardian nods approvingly as you approach, acknowledging your respect. Successfully crossing the bridge, you feel a surge of accomplishment.\nYou're led to the firefly crossroads.")
        ready = input("A. Follow the trail of glowing fireflies deeper into the forest. \nB. Head in the opposite direction of the fireflies' path.\n").lower()
        if ready == "a":
            print("The gentle illumination of the fireflies guiding your way through an enchanting grove. The fireflies seem to dance in harmony with the ancient trees, leading you to a magical clearing. Your intuition serves you well, and you emerge unscathed.\nYou're led to a group of singing sirens.")
            ready = input("A. Be lured by the enchanting songs of distant sirens.\nB. Plug your ears and press on, resisting the temptation.\n").lower()
            if ready == "b":
                print("The haunting melodies fade, and you emerge from the trees unscathed, realizing that the sirens' song was a treacherous illusion. However, those who succumb are drawn into a spectral realm, forever lost to the enchanted forest's enchantment.")
            else:
                print("Game over!!!\nNotes promising untold wonders beyond the veil lead you a stray.")
        else:
            print("Game over!!!\nThe eerie whispers and rustling leaves create an unsettling atmosphere. The whispers grow louder, and shadowy figures surround you. Lost and disoriented, you become a part of the forest's ghostly choir, your existence intertwined with the haunting sounds.")   
    else:
        print("Game over!!!\nThis lead to a dense thicket and ominous shadows make the journey perilous. The thicket becomes an impenetrable maze, and you find yourself entangled in magical vines. The guardian watches, disapproving, and your presence fades away as the forest claims you.")        
else: 
    print("Game over!!!\nYou find yourself lost in a labyrinthine network of passages. Unable to find your way out, the darkness overwhelms you, and your adventure comes to a mysterious end.")
