__author__= "Victor K. Chan"
import random
import copy
running = True
def get_store_item(list):
    menu_loop = True
    potion = None
    while menu_loop:
        for counter in range(0, len(list)):
            print(counter + 1, ")" , list[counter]["item_name"])
        print("X) Leave this useless store department")
        choice = input("Please enter item number you wish to purchase: ")
        choice = choice.lower()
        if choice == "x":
            menu_loop = False
        if choice.isdigit():
            index = int(choice - 1)
            if index >= 0 and index < len(list):
                potion = list[index]
        return potion
    return None

def buy_item(item, character):
    if item != None:
        if character["cash"] >= item["cost"]:
            character["cash"] -= item["cost"]
            print("You bought a(n) ", item, " ; OuO have fun with it!")
        else:
            print("Too poor!")

character = {
    "name" : "I didn't pick a name. Shame on me!",
    "level" : 1,
    "cash" : 20,
    "bcash" : 0,
    "exp" : 0,
    "exp_to_lvl" : 15,
    "statpoints" : 0,
    "hp" : 50,
    "maxhp" : 50,
    "mp" : 50,
    "atk" : 10,
    "magicAtk" : 1,
    "def" : 10,
}

inv = {

}

is_knife_bought = False
hasGrandmaster = False
hasNoobSword = False
hasSpear = False
hasShield = False
golden_knife_bought = False

weapon ={
    "name" : "none",
    "atk" : 0,
    "magicboost" : 0,
    "type" : "none"
}

def print_store_list(list):
    for counter in range(0, len(list)):
        print(counter + 1, ")" , list[counter]['item_name'])
    print("X) Leave this useless store")
owner_angery = 0
HowMuchPot = 0
ThundaStormLearned = True
IceThornLearned = False
CombustLearned = False
monster_dict = []
monster_dict.append({
    "name": "( S O M E W H A T )  L A R G E  R A T ",
    "lvl" : 1,
    "hp" : 20,
    "xp" : 5,
    "atk" : 1,
    "reward" : 3,
})

monster_dict.append({
    "name": " N O R M A L  M O N S T E R  I R L  ",
    "lvl" : 5,
    "hp" : 60,
    "xp" : 15,
    "atk" : 5,
    "reward" : 5,
})


monster_dict.append({
    "name": "( S O M E H O W  B E C A M E  A  B O S S ) A  S T U F F E D  A N I M A L ",
    "lvl" : 9001,
    "hp" : 500,
    "xp" : 500,
    "atk" : 15,
    "reward" : 20,
})

enemy_wizard = []

enemy_wizard.append({
    "name" : "Jake ",
    "lvl" : 15,
    "hp" : 250,
    "atk" : 7,
    "matk" : 30,
    "mp" : 50,
    "def" : 80,
    "stage" : 1,
})

enemy_wizard.append({
    "name" : "Hideyoshi",
    "lvl" : 22,
    "hp" : 400,
    "atk" : 20,
    "matk" : 350,
    "mp" : 5,
    "def" : 45,
    "stage" : 2,
})

enemy_wizard.append({
    "name" : "IHitLikeATruck",
    "lvl" : 30,
    "hp" : 300,
    "atk" : 75,
    "matk" : 375,
    "mp" : 20,
    "def" : 410,
    "stage" : 3,
})

store_items = [
        {
            "item_name": "Smol Health Potion",
            "item_effect": "hp",
            "effect:value": 25,
            "item_type" : "Potion"
        },
        {
            "item_name": "Smol Mana Potion",
            "item_effect": "mp",
            "effect:value": 17,
            "item_type" : "Potion"
        },
        {
            "item_name": "Smol Awakening Crystal",
            "item_effect": "atk",
            "effect:value": 1,
            "item_type": "Potion"
        },
        {
            "item_name": "Smol Vitality Potion",
            "item_effect": "max hp",
            "effect:value": 10,
            "item_type" : "Potion",
        },
        {
           "item_name" : "Smol Golden Dirk",
            "item_effect" : "boosts G earned",
            "effect:value": 10,
            "item_type" : "Weapon",
        },
        {

        }
]
rand_pot = [
        {
            "item_name": "Smol Health Potion",
            "item_effect": "hp",
            "effect:value": 25,
        },
        {
            "item_name": "Smol Mana Potion",
            "item_effect": "mp",
            "effect:value": 17,
        },
        {
            "item_name": "Smol Awakening Crystal",
            "item_effect": "atk",
            "effect:value": 1,
        },
        {
            "item_name": "Smol Vitality Potion",
            "item_effect": "max hp",
            "effect:value": 10,
        }
]

store_spells = [
    {
        "item_name" : "Combust",
        "item_effect" : "spell",
        "effect:value" : 30,
        "mp_cost" : 25,
        "cost" : 250
    },
    {
        "item_name" : "Frost Thorns",
        "item_effect" : "spell",
        "effect:value" : 30,
        "dot:value" : 5,
        "dot:duration" : 6,
        "mp_cost" : 30,
        "cost" : 265
    }
]
while running:
    # Printing main menu kappa,
    print("\n      S U P E R  W I Z A R D  B A T T L E  G A M E")
    print(" I---------------------------------------------------I")
    print("\n                     A)New game")
    print("                     B)Load game")
    print("                     C)Credits")
    print("                     X)Exit game")
    #gets user's choice kappa
    Choice = input("\t\t\tP I C K  Y O U R  C H O I C E ")
    #decide what to run based on choice kappa
    if Choice.capitalize() == "A":
        # Create the character kappa
        print(" E X C E L L E N T  C H O I C E ,  N E W  W I Z A R D !")
        character["name"] = input("           I N S E R T  Y O U R  N A M E : ")
        if character["name"] == "kappa" :
            character["cash"] += 9999999999999999999999999999999
            character["maxhp"] = 9999999999999999999
            character["statpoints"] += 16000
            character["hp"] = character["maxhp"]
            character["level"] += 200
        input("W E L C O M E ,  " + character["name"] + " ,  T O  T H E  G A M E , ")
        print("   Wizard Menu")
        print(" I------------I")
        print("A) Train")
        print("B) Duel other wizards")
        print("C) Buy / Sell stuff")
        print("D) In Progress; Don't attempt to enter!")
        print("E) Character Profile")
        print("S) Save")
        print("X) Exit")
        choice = input("Please enter choice: ").lower()
        kappa = True
        while kappa:
            if character["hp"] > character["maxhp"]:
                character["hp"] = character["maxhp"]
            if choice == "x":
                kappa = False
            elif choice == "a":
                input("You are looking very hard for a monster right now.....")
                monster = monster_dict[random.randrange(0, len(monster_dict))].copy()
                battle = True
                DOT_turns_left = 0
                DOT_dmg = 12 * character["magicAtk"]
                while battle:
                    #Display to user option for attacking [kappa]
                    print("Name: ", monster["name"])
                    print("Health: ", monster["hp"])
                    print("1: Give it the S M A C C")
                    print("2: Cast Spell")
                    print("3: Consume a HP pot")
                    option = input("Please select action: ")
                    if option == "1":
                        print("Whack! You dealt " , character["atk"], "damage to ", monster["name"], "!!!!!!1!!!ONE!!!!!!")
                        monster["hp"] -= character["atk"]
                        print("It has ", monster["hp"], " Health left.")
                    elif option == "2":
                        print("Learned Spells: ")
                        if ThundaStormLearned:
                            print("1) Thunda Storm || Cost: 20 MP")
                        if IceThornLearned:
                            print("2) Ice Thorns || Cost:  30 MP")
                        if CombustLearned:
                            print("3) Combust || Cost: 100 MP")
                        option = input("Which Spell?")
                        if option == '1':
                            if character["mp"] >= 20:
                                print("Your T H U N D A  S T O R M  R O F L S T O M P E D ", monster["name"],
                                      "for", 25 * character["magicAtk"], " damage! What a  { [ ("
                                                                         "T H U N D A  S T O R M) ] }  indeed!")
                                monster["hp"] -= 25 * character["magicAtk"]
                                character["mp"] -= 20
                            else:
                                print("Too little mana (=o>_<)=o *~*~*~*~*")
                        elif option == '2':
                            if character["mp"] >= 30 and IceThornLearned:
                                print("Your ICE THORNS pierced ", monster["name"],
                                      "for", 15 * character["magicAtk"], " damage, and left DOT damage! What a spell"
                                                                         " indeed!")
                                DOT_turns_left = 5
                                monster["hp"] -= 15 * character["magicAtk"]
                                character["mp"] -= 30
                            elif not IceThornLearned:
                                print("Didn't learn this spell, dummy!")
                            else:
                                print("No mana! :(")
                        elif option == '3':
                            if character["mp"] >= 100 and CombustLearned:
                                print("You flamed ", monster["name"], " with Combust for",(150+20*character["magicAtk"]),
                                      " damage! What a powerful spell!")
                                monster["hp"] -= 150 * character["magicAtk"]
                                character["mp"] -= 100
                            elif not CombustLearned:
                                print("You were about to cast a spell, then remembered you didn't know the spell!")
                            else:
                                print("No mana! (=o>_<)=o *~*~*~*~*")
                        else:
                            print("Wrong Choice!")
                        choice = "XD LMAO"
                    elif option == "3":
                        if HowMuchPot != 0:
                            HowMuchPot-= 1
                            character["hp"] += 25
                            print("You Consumed a Potion. You are weak, y'know?")
                        else:
                            print("You don't have a Potion!")
                    else:
                        print(" S T O P  D A W D L I N G  A N D  A T T A C K !")
                    if DOT_turns_left >= 1:
                        print(monster["name"], " received damage from Ice Thorns!")
                        monster["hp"] -= round(DOT_dmg)
                        DOT_turns_left -= 1
                    if monster["hp"] > 0:
                        truedef = character["def"] / 5
                        truedmg = round(monster["atk"] - truedef)
                        if truedmg < 1:
                            truedmg = 1
                        print("Kapow! You received ", truedmg,
                              " damage!!!!!!1!!!ONE!!!!!!")
                        character["hp"] -= truedmg
                        print("Your HP: ", character["hp"])
                        print("It's HP: ", monster["hp"])
                    elif monster["hp"] <= 0:
                        print("You murdered a poor ", monster["name"], "! How could you!")
                        character["exp"] += monster["xp"]
                        print("B O O Y A H ! You gained ", monster["xp"] , " Experience Points! :^)")
                        while character["exp"] >= character["exp_to_lvl"]:
                            if character["exp"] >= character["exp_to_lvl"]:
                                character["level"] += 1
                                character["exp"] -= character["exp_to_lvl"]
                                character["exp_to_lvl"] += character["level"]
                                character["atk"] += 2
                                character["mp"] += 50
                                character["hp"] = character["maxhp"]
                                character["statpoints"] += 1
                                print("I===========================I \n B O O Y A H !  Y O U  L E V E L E D  U P ! You are level ", character["level"],
                                      " ! Congratulations :^)\n I=============================I")
                        character["cash"] += monster["reward"]
                        character["cash"] += character["bcash"]
                        truecash = monster["reward"] + character["bcash"]
                        character["mp"] += 25
                        print("You got some *insert cashmoney song* !! To be exact, ", truecash)
                        input("Press Enter to continue...")
                        battle = False
                    if character["hp"] <= 0:
                        input("You were hit too many times and you see the skies blacking out.....")
                        character["hp"] = character["maxhp"]
                        input("You woke up, discovering that you were saved by villagers from a nearby village. How nice of them!")
                        battle = False

            elif choice == "c":
                #Too lazy to fix up this portion of code :P
                store_special = ["Grandmaster Wand", "Noob Sword","Noob Sword","Noob Sword","Noob Sword","Noob Sword","Noob Sword", "The Spear of Pokey-Pokes", "Shield of Ordinary Wood","Shield of Ordinary Wood","Shield of Ordinary Wood","Shield of Ordinary Wood","Shield of Ordinary Wood","Shield of Ordinary Wood","Shield of Ordinary Wood","Shield of Ordinary Wood", "The Spear of Pokey-Pokes", "The Spear of Pokey-Pokes", "The Spear of Pokey-Pokes", "The Spear of Pokey-Pokes", "The Spear of Pokey-Pokes", "The Spear of Pokey-Pokes", "The Spear of Pokey-Pokes", "The Spear of Pokey-Pokes", "The Spear of Pokey-Pokes", "The Spear of Pokey-Pokes", "The Spear of Pokey-Pokes", "The Spear of Pokey-Pokes", "The Spear of Pokey-Pokes", "The Spear of Pokey-Pokes", "The Spear of Pokey-Pokes"]
                special = store_special[random.randrange(0, len(store_special))]

                print("The Store's special item is: " + special + "! How lucky!")
                print("What would you like to do?: ")
                print("A) Buy")
                print("B) Sell")
                print("(Anything else): Exit store")
                Choice = input("Pick your choice: ").lower()
                owner_angery = 0
                if Choice == "a":
                    store_name = ["S W O R D S  A N D  S H I E L D S ( T M )", "W I Z A R D R Y  V E N D O R", "S O M E  R A N D O M  M A R K E T P L A C E ", "S T I C K S  A N D  S T O C K S ( C ) ( T M )"]
                    name = store_name[random.randrange(0, len(store_name))]
                    print(name)
                    print(" What's available:")
                    print("I-----------------I")
                    print("S) Store special: " + special + "--- 250G")
                    Pot = rand_pot[random.randrange(0,len(rand_pot))]
                    randprice = random.randrange(10,50)
                    print("A) ", Pot["item_name"] , " : ", randprice, "G")
                    print("B) Winner's Lootbox Key: 20G")
                    print("C) Smol Golden Dirk: 175G")
                    if not is_knife_bought:
                        print("D) N00b knife : 20G")
                    else:
                        print("D) S O L D  O U T")
                    print("E) Spells OuO")
                    print("F) Try Bargaining")
                    print("X) Back")
                    print("You have " , character["cash"] , " G. Spend it wisely!")
                    NoPurchase = True
                    HowMuchBargained = 0
                    while NoPurchase:
                        WhatPurchase = input("Pick something to buy: ").lower()
                        HowMuchOff = HowMuchBargained
                        if WhatPurchase == "s":
                            price = 150
                            discounted = price - HowMuchOff
                            if character["cash"] >= discounted:
                                print("You Purchased a(n) " + special)
                                character["cash"] -= discounted
                                if special == "Grandmaster Wand":
                                    print("You automatically got the stats of the weapon.")
                                    hasGrandmaster = True
                                    '''character["atk"] += 999999999
                                    character["magicboost"] += 150'''
                                elif special == "Noob Sword" :
                                    print("You automatically got the stats of the weapon.")
                                    hasNoobSword = True
                                    '''character["atk"] += 10'''
                                elif special == "The Spear of Pokey-Pokes":
                                    print("You automatically got the stats of the weapon.")
                                    hasSpear = True
                                    '''character["atk"] += 25'''
                                elif special == "Shield of Ordinary Wood" :
                                    print("You automatically got the stats of the shield.")
                                    hasShield = True
                                    '''character["def"] += 30'''

                                NoPurchase = False
                            else:
                                print("You Need More Munny! Git workin' !")
                                NoPurchase = False
                        elif WhatPurchase == "a":
                            discounted = randprice - HowMuchOff
                            if character["cash"] >= discounted:
                                print("You bought a Potion. Real men don't need Potions!!!!!1!!1!!!1!!!ONE!!!!")
                                if Pot["item_name"] == "Smol Health Potion" :
                                    HowMuchPot += 1
                                    print("*INSERT ITEM GET! MUSIC*")
                                elif Pot["item_name"] == "Smol Mana Potion" :
                                    character["mp"] += 17
                                    print("Also, you drank the potion right after buying the Potion. LOL.")
                                elif Pot["item_name"] == "Smol Vitality Potion":
                                    character["maxhp"] += 10
                                    character["hp"] = character["maxhp"]
                                    print("Also, you drank the potion right after buying the Potion. LOL.")
                                elif Pot['item_name'] == "Smol Awakening Crystal":
                                    character["atk"] += 1
                                    print("The Crystal bound itself to you, infusing you with its power. You didn't feel"
                                          "any changes. Eh.")
                                if HowMuchBargained < randprice:
                                    character["cash"] -= discounted
                                else:
                                    discounted = 1
                                    character["cash"] -= discounted
                            else:
                                print("You Need More Munny. What a noob!")
                        elif WhatPurchase == "b":
                            if character["cash"] >= 20:
                                print("You bought a Winner Lootbox Key! Hope it opens your heart ;D")
                                character["inv"].append("Winner Lootbox Key")
                                character["cash"] -= 20
                            else:
                                print("You too poor to buy Winner Lootbox Key! Go get money!")
                        elif WhatPurchase == "c":
                            if character["cash"] >= 175 - HowMuchOff:
                                print("You bought a Smol Golden Dirk. Now you just need to encase yourself in gold.....\n"
                                 "You also automatically equipped it. It's Golden aura gave you the effects without using it at all o3o")
                                 golden_knife_bought = True
                                character["bcash"] += 10
                                character["cash"] -= 175 - HowMuchOff
                                NoPurchase = False
                            else:
                                print("Too poor, my boi. We couldn't demonetize you.... ; -;")
                        elif WhatPurchase == "d":
                            if not is_knife_bought:
                                if character["cash"] >= 20 - HowMuchOff:
                                    print("You bought a N00b knife. It looks like a plastic knife.... Oh wait. Sorry, wrong E. R. A.")
                                    character["cash"] -= 20 - HowMuchOff
                                    NoPurchase = False
                                    is_knife_bought = True
                                else:
                                    print("Too poor, my boi.............")

                            else:
                                print("It's sold out. What did you expect?")
                        elif WhatPurchase == "f" :
                            HowMuchBargained = random.randrange(0, 4)
                            if owner_angery >= 5:
                                input("The owner got angry with you and used \'I KICK THEE\' upon you!")
                                input("You were sent flying to your oblivion. Well, at least you tried (too many times)!")
                                exit("I==========G A M E  O V E R==========I")
                            elif HowMuchBargained == 0:
                                print("You weren't able to bargain with The Cashier OuO")
                                owner_angery += 1
                                HowMuchBargained = 0
                            elif HowMuchBargained == 1:
                                print("You got a 10G discount! How lucky!")
                                owner_angery += 1
                                HowMuchBargained = 10
                            elif HowMuchBargained == 2:
                                print("You got a 15G discount! What a smooth talking!")
                                owner_angery += 1
                                HowMuchBargained = 15
                            elif HowMuchBargained == 3:
                                print("You got a 20G discount! What a master Bargainer!")
                                owner_angery += 1
                                HowMuchBargained = 20
                            else:
                                print("ERRROR")
                        elif WhatPurchase == "e":
                            spells_menu = True
                            while spells_menu:
                                print("Available Spells: ")
                                if not CombustLearned:
                                    print("1) Combust || Cost: 250 G")
                                if not IceThornLearned:
                                    print("2) Ice Thorns || Cost: 265 G")
                                if CombustLearned and IceThornLearned:
                                    print(">> You bought everything, you rich twat!")
                                choice = 0
                                choice = input('Please enter item number you wish to throw money at: ')
                                if choice == '1':
                                    if character["cash"] >= 250 - HowMuchBargained:
                                        character["cash"] -= 250 - HowMuchBargained
                                        input("Some random dude came in once you bought the spell. He taught you how to use it!")
                                        input("You learned Combust!")
                                        input("Combust is useful for dealing basic damage. Watch out, though, as it "
                                              "will consume lots\n"
                                              "of MP!")
                                        CombustLearned = True
                                    else:
                                        print("Too poor!")
                                        spells_menu = False
                                elif choice == '2':
                                    if character["cash"] >= 265 - HowMuchBargained:
                                        character["cash"] -= 265 - HowMuchBargained
                                        input("Some random Teletubbie started singing a song about how to use the spell. \n"
                                              "The song's still stuck in your head.")
                                        input("You learned Ice Thorns!")
                                        input("Ice Thorns deals DOT damage, with an initial small burst of damage!")
                                        IceThornLearned = True
                                    else:
                                        print("Too Poor!")
                                        spells_menu = False
                                elif choice == "x" or "X":
                                    spells_menu = False
                                    print("You left the spells portion of the store...")
                                else:
                                    print("BAD CHOICE!!")
                            else:
                                print("BAD CHOICE!! :C")
                        elif WhatPurchase == "x":
                            NoPurchase = False
            elif choice == "b" and character["level"] >= 15:
                input("Welcome to the Grandmaster Arena! >> ")
                mychoice = input("Do you want to enter the Tournament? (y/n) >> ").lower()
                if mychoice == 'y':
                    stagewin = False
                    input("Great! Please head to Arena " + random.randrange(0o1, 99).__str__() + " >> ")
                    input("... >> ")
                    input("... >> ")
                    input("... >> ")
                    input("W E L C O M E  T O  T H E  G R A N D M A S T E R  T O U R N A M E N T! >> ")
                    input("I N  T H I S  T O U R N A M E N T,  C O N T E S T A N T S  B A T T L E  I T  O U T  F O R "
                          " F I R S T  P L A C E! >> ")
                    input("Y O U R  F I R S T  M A T C H  I S  W I T H  A  C O N T E S T A N T  C A L L E D  J A K E! "
                          ">> ")
                    wager = random.randrange(60, 200)
                    input("T H E  S P E C T A T O R S  H A V E  W A G E R E D  O N  Y O U  B O T H,  A N D  T H E Y "
                          "H A V E  B E T  "+ wager.__str__() +"G  O N  J A K E! >> ")
                    input("L E T  T H E  F I R S T  M A T C H  O F  T H I S  S E A S O N  B E G I N! >> ")
                    monster = enemy_wizard[0].copy()
                    battle = True
                    print("Name: ", monster["name"])
                    DOT_turns_left = 0
                    DOT_dmg = 12 * character["magicAtk"]
                    if monster["hp"] / 250 <= 0.5:
                        print("Health: ", monster["hp"])
                    while battle:
                        monster["mp"] += 5
                        monster["hp"] += 7
                        #Display to user option for attacking [kappa]
                        print("1: Give it the S M A C C")
                        print("2: Cast Spell")
                        option = input("Please select action: ")
                        if option == "1":
                            truemdef = round(monster["def"] / 5)
                            truemdmg = character["atk"] - truemdef
                            print("Whack! You dealt " , truemdmg.__str__(), "damage to ", monster["name"], "!!!!!!1!!!ONE!!!!!!")
                            monster["hp"] -= truemdmg
                        elif option == "2":
                            print("Learned Spells: ")
                            if ThundaStormLearned:
                                print("1) Thunda Storm || Cost: 20 MP")
                            if IceThornLearned:
                                print("2) Ice Thorns || Cost:  30 MP")
                            if CombustLearned:
                                print("3) Combust || Cost: 100 MP")
                            option = input("Which Spell?")
                            if option == '1':
                                if character["mp"] >= 20:
                                    print("Your T H U N D A  S T O R M  R O F L S T O M P E D ", monster["name"],
                                          "for", 25 * character["magicAtk"], " damage! What a  { [ ("
                                                                             "T H U N D A  S T O R M) ] }  indeed!")
                                    monster["hp"] -= 25 * character["magicAtk"]
                                    character["mp"] -= 20
                                else:
                                    print("Too little mana (=o>_<)=o *~*~*~*~*")
                            elif option == '2':
                                if character["mp"] >= 30 and IceThornLearned:
                                    print("Your ICE THORNS pierced ", monster["name"],
                                          "for", 15 * character["magicAtk"],
                                          " damage, and left DOT damage! What a spell"
                                          " indeed!")
                                    DOT_turns_left = 5
                                    monster["hp"] -= 15 * character["magicAtk"]
                                    character["mp"] -= 30
                                elif not IceThornLearned:
                                    print("Didn't learn this spell, dummy!")
                                else:
                                    print("No mana! :(")
                            elif option == '3':
                                if character["mp"] >= 100 and CombustLearned:
                                    print("You flamed ", monster["name"], " with Combust for",
                                          (150 + 20 * character["magicAtk"]),
                                          " damage! What a powerful spell!")
                                    monster["hp"] -= 150 * character["magicAtk"]
                                    character["mp"] -= 100
                                elif not CombustLearned:
                                    print("You were about to cast a spell, then remembered you didn't know the spell!")
                                else:
                                    print("No mana! (=o>_<)=o *~*~*~*~*")
                            else:
                                print("Wrong Choice!")
                        else:
                            print(" S T O P  D A W D L I N G  A N D  A T T A C K !")
                        if DOT_turns_left >= 1:
                            print(monster["name"], " received damage from Ice Thorns!")
                            monster["hp"] -= round(DOT_dmg)
                            DOT_turns_left -= 1
                        if monster["hp"] > 0 and monster["mp"] >= 20:
                            truedmg = monster["matk"]
                            monster["mp"] -= 20
                            print("Jake casted Rolling Typhoon! You were thrown around in the squall, and was hit for"
                                  , truedmg,
                              " damage!!!!!!1!!!ONE!!!!!!")
                            character["hp"] -= truedmg
                            print("Your HP: ", character["hp"])
                            if character["hp"] <= 0:
                                input("You were knocked out... And lost the tournament... >> ")
                                input("Your stats must be inadequate! Try upgrading your gear, or boosting your stats!"
                                      " >> ")
                                battle = False
                        elif monster["hp"] > 0 and monster["mp"] <= 19:
                            truedef = character["def"] / 5
                            truedmg = round(monster["atk"] - truedef)
                            if truedmg < 1:
                                truedmg = 1
                            print("Jake S M A C C E D you with the wider end of his staff, dealing ", truedmg,
                                  " damage!")
                            character["hp"] -= truedmg
                            print("Your HP: ", character["hp"])
                            if character["hp"] <= 0:
                                input("You were knocked out... And lost the tournament... >> ")
                                input("Your stats must be inadequate! Try upgrading your gear, or boosting your stats!"
                                      " >> ")
                                battle = False
                        else:
                            stagewin = True
                            input("A N D  T H E  V I C T O R  I S  D E C I D E D! ")
                            print(character["name"]+ " H A S  W O N  T H E  M A T C H, A L O N G  "
                                                     "W I T H "+ wager.__str__()+ "G!"
                                                     " A N O T H E R  C H A L L E N G E R  W I L L  A R R I V E  "
                                                     "S H O R T L Y! >> ")
                            input("Waiting for player's response... >> ")
                            character["cash"] += wager
                            battle = False
                            character["cash"]
                    if stagewin:
                        stagewin = False
                        input("Y O U R  S E C O N D  M A T C H  I S  W I T H  A  C O N T E S T A N T  C A L L E D"
                              "  H I D E Y O S H I! >> ")
                        wager = random.randrange(60, 200)
                        input("T H E  S P E C T A T O R S  H A V E  W A G E R E D  O N  Y O U  B O T H,  A N D  T H E Y "
                            "H A V E  B E T  " + wager.__str__() + "G  O N  H I D E Y O S H I! >> ")
                        input("L E T  T H E  S E C O N D  M A T C H  O F  T H I S  S E A S O N  B E G I N! >> ")
                        monster = enemy_wizard[1].copy()
                        battle = True
                        print("Name: ", monster["name"])
                        while battle:
                            monster["mp"] += 2
                            monster["hp"] += 20
                            if monster["hp"] / 250 <= 0.5:
                                print("Health: ", monster["hp"])
                            # Display to user option for attacking [kappa]
                            print("1: Give it the S M A C C")
                            print("2: Cast Spell")
                            option = input("Please select action: ")
                            if option == "1":
                                truemdef = round(monster["def"] / 5)
                                truemdmg = character["atk"] - truemdef
                                print("Whack! You dealt ", truemdmg.__str__(), "damage to ", monster["name"],
                                      "!!!!!!1!!!ONE!!!!!!")
                                monster["hp"] -= truemdmg
                            elif option == "2":
                                print("Learned Spells: ")
                                if ThundaStormLearned:
                                    print("1) Thunda Storm || Cost: 20 MP")
                                if IceThornLearned:
                                    print("2) Ice Thorns || Cost:  30 MP")
                                if CombustLearned:
                                    print("3) Combust || Cost: 100 MP")
                                option = input("Which Spell?")
                                if option == '1':
                                    if character["mp"] >= 20:
                                        print("Your T H U N D A  S T O R M  R O F L S T O M P E D ", monster["name"],
                                              "for", 25 * character["magicAtk"], " damage! What a  { [ ("
                                                                                 "T H U N D A  S T O R M) ] }  indeed!")
                                        monster["hp"] -= 25 * character["magicAtk"]
                                        character["mp"] -= 20
                                    else:
                                        print("Too little mana (=o>_<)=o *~*~*~*~*")
                                elif option == '2':
                                    if character["mp"] >= 30 and IceThornLearned:
                                        print("Your ICE THORNS pierced ", monster["name"],
                                              "for", 15 * character["magicAtk"],
                                              " damage, and left DOT damage! What a spell"
                                              " indeed!")
                                        DOT_turns_left = 5
                                        monster["hp"] -= 15 * character["magicAtk"]
                                        character["mp"] -= 30
                                    elif not IceThornLearned:
                                        print("Didn't learn this spell, dummy!")
                                    else:
                                        print("No mana! :(")
                                elif option == '3':
                                    if character["mp"] >= 100 and CombustLearned:
                                        print("You flamed ", monster["name"], " with Combust for",
                                              (150 + 20 * character["magicAtk"]),
                                              " damage! What a powerful spell!")
                                        monster["hp"] -= 150 * character["magicAtk"]
                                        character["mp"] -= 100
                                    elif not CombustLearned:
                                        print(
                                            "You were about to cast a spell, then remembered you didn't know the spell!")
                                    else:
                                        print("No mana! (=o>_<)=o *~*~*~*~*")
                                else:
                                    print("Wrong Choice!")
                            else:
                                print(" S T O P  D A W D L I N G  A N D  A T T A C K !")
                            if DOT_turns_left >= 1:
                                print(monster["name"], " received damage from Ice Thorns!")
                                monster["hp"] -= round(DOT_dmg)
                                DOT_turns_left -= 1
                            if monster["hp"] > 0 and monster["mp"] >= 50:
                                truedmg = monster["matk"]
                                monster["mp"] -= 50
                                print(
                                    "Hideyoshi casted Brilliant Thunder! You were hit by a ray of pure lightning, and was "
                                    "hit for", truedmg," damage!!!!!!1!!!ONE!!!!!!")
                                print("Hideyoshi's Brilliant Thunder Absorbed some of the damage as mp!")
                                character["hp"] -= truedmg
                                amt_absorbed = round((random.randrange(25, 50) / 1000) * monster["matk"])
                                monster["mp"] += amt_absorbed
                                print("Your HP: ", character["hp"])
                                if character["hp"] <= 0:
                                    input("You were knocked out... And lost the tournament... >> ")
                                    input(
                                        "Your stats must be inadequate! Try upgrading your gear, or boosting your stats!"
                                        " >> ")
                                    battle = False
                            elif monster["hp"] > 0 and monster["mp"] <= 49:
                                truedef = character["def"] / 5
                                truedmg = round(monster["atk"] - truedef)
                                if truedmg < 1:
                                    truedmg = 1
                                crit_chance = random.randrange(0, 10)
                                if crit_chance >= 6:
                                    truedmg *= 1.75
                                    round(truedmg, 1)
                                    print("Hideyoshi S T A B B E D you in your flank with a +6 Tesla Blade, landing a "
                                          "critical hit and dealing ", truedmg, " damage!")
                                else:
                                    print("Hideyoshi S T A B B E D you in the side with a +6 Tesla Blade, dealing ", truedmg,
                                      " damage!")
                                character["hp"] -= truedmg
                                print("Your HP: ", character["hp"])
                                if character["hp"] <= 0:
                                    input("You were knocked out... And lost the tournament... >> ")
                                    input(
                                        "Your stats must be inadequate! Try upgrading your gear, or boosting your stats!"
                                        " >> ")
                                    battle = False
                            else:
                                input("A N D  T H E  V I C T O R  I S  D E C I D E D! ")
                                print(character["name"], " H A S  W O N  T H E  M A T C H, A L O N G  W I T H ",
                                      wager.__str__(),
                                      "G! A N O T H E R  C H A L L E N G E R  W I L L  A R R I V E  S H O R T L Y! >> ")
                                input("Waiting for player's response... >> ")
                                character["cash"] += wager
                                battle = False
                                stagewin = True
                    if stagewin:
                        stagewin = False
                        input("Y O U R  L A S T  M A T C H  I S  W I T H  A  S E M I - T R U C K  C A L L E D"
                              "  IHITLIKEATRUCK! >> ")
                        wager = random.randrange(100, 351)
                        if wager == 351:
                            wager = 1545
                        input("T H E  S P E C T A T O R S  H A V E  W A G E R E D  O N  Y O U  B O T H,  A N D  T H E Y "
                            "H A V E  B E T  " + wager.__str__() + "G  O N  T H E  S E M I - T R U C K ! >> ")
                        input("L E T  T H E  L A S T  M A T C H  O F  T H I S  S E A S O N  B E G I N! >> ")
                        monster = enemy_wizard[2].copy()
                        battle = True
                        print("Name: ", monster["name"])
                        while battle:
                            monster["mp"] += 4
                            monster["hp"] += 20
                            if monster["hp"] / 300 <= 0.5:
                                print("Health: ", monster["hp"])
                            # Display to user option for attacking [kappa]
                            print("1: Give it the S M A C C")
                            print("2: Cast Spell")
                            option = input("Please select action: ")
                            if option == "1":
                                truemdef = round(monster["def"] / 5)
                                truemdmg = character["atk"] - truemdef
                                print("Whack! You dealt ", truemdmg.__str__(), "damage to ", monster["name"],
                                      "!!!!!!1!!!ONE!!!!!!")
                                monster["hp"] -= truemdmg
                            elif option == "2":
                                print("Learned Spells: ")
                                if ThundaStormLearned:
                                    print("1) Thunda Storm || Cost: 20 MP")
                                if IceThornLearned:
                                    print("2) Ice Thorns || Cost:  30 MP")
                                if CombustLearned:
                                    print("3) Combust || Cost: 100 MP")
                                option = input("Which Spell?")
                                if option == '1':
                                    if character["mp"] >= 20:
                                        print("Your T H U N D A  S T O R M  R O F L S T O M P E D ", monster["name"],
                                              "for", 25 * character["magicAtk"], " damage! What a  { [ ("
                                                                                 "T H U N D A  S T O R M) ] }  indeed!")
                                        monster["hp"] -= 25 * character["magicAtk"]
                                        character["mp"] -= 20
                                    else:
                                        print("Too little mana (=o>_<)=o *~*~*~*~*")
                                elif option == '2':
                                    if character["mp"] >= 30 and IceThornLearned:
                                        print("Your ICE THORNS pierced ", monster["name"],
                                              "for", 15 * character["magicAtk"],
                                              " damage, and left DOT damage! What a spell"
                                              " indeed!")
                                        DOT_turns_left = 5
                                        monster["hp"] -= 15 * character["magicAtk"]
                                        character["mp"] -= 30
                                    elif not IceThornLearned:
                                        print("Didn't learn this spell, dummy!")
                                    else:
                                        print("No mana! :(")
                                elif option == '3':
                                    if character["mp"] >= 100 and CombustLearned:
                                        print("You flamed ", monster["name"], " with Combust for",
                                              (150 + 20 * character["magicAtk"]),
                                              " damage! What a powerful spell!")
                                        monster["hp"] -= 150 * character["magicAtk"]
                                        character["mp"] -= 100
                                    elif not CombustLearned:
                                        print(
                                           "You were about to cast a spell, then remembered you didn't know the spell!")
                                    else:
                                        print("No mana! (=o>_<)=o *~*~*~*~*")
                                else:
                                    print("Wrong Choice!")
                            else:
                                print(" S T O P  D A W D L I N G  A N D  A T T A C K !")
                            if DOT_turns_left >= 1:
                                print(monster["name"], " received damage from Ice Thorns!")
                                monster["hp"] -= round(DOT_dmg)
                                DOT_turns_left -= 1
                            if monster["hp"] > 0 and monster["mp"] >= 60:
                                truedmg = monster["matk"]
                                monster["mp"] -= 60
                                print(
                                    monster["name"], " casted UberSlam! You were SQUASHED, and was "
                                    "hit for", truedmg," damage!!!!!!1!!!ONE!!!!!!")
                                print(monster["name"], " absorbed the damage as hp and mp!")
                                character["hp"] -= truedmg
                                amt_absorbed = round((random.randrange(25, 50) / 1000) * monster["matk"])
                                monster["mp"] += amt_absorbed
                                monster["hp"] += amt_absorbed
                                print("Your HP: ", character["hp"])
                                if character["hp"] <= 0:
                                    input("You were knocked out... And lost the tournament... >> ")
                                    input(
                                        "Your stats must be inadequate! Try upgrading your gear, or boosting your stats!"
                                        " >> ")
                                    battle = False
                            elif monster["hp"] > 0 and monster["mp"] <= 49:
                                truedef = character["def"] / 5
                                truedmg = round(monster["atk"] - truedef)
                                if truedmg < 1:
                                    truedmg = 1
                                crit_chance = random.randrange(0, 10)
                                if crit_chance >= 8:
                                    truedmg *= 2
                                    round(truedmg, 1)
                                    print("IHitLikeATruck S L A M M E D into your flank with a +10 Fender Bender, "
                                          "landing a critical hit and dealing ", truedmg, " damage!")
                                else:
                                    print("IHitLikeATruck W H E E L I E D you, dealing ", truedmg,
                                      " damage!")
                                character["hp"] -= truedmg
                                print("Your HP: ", character["hp"])
                                if character["hp"] <= 0:
                                    input("You were knocked out... And lost the tournament... >> ")
                                    input(
                                        "Your stats must be inadequate! Try upgrading your gear, or boosting your stats!"
                                        " >> ")
                                    battle = False
                            else:
                                input("A N D  T H E  V I C T O R  I S  D E C I D E D! ")
                                print(character["name"], " H A S  W O N  T H E  M A T C H, A L O N G  W I T H ",
                                      wager.__str__(),
                                      "G! A N O T H E R  C H A L L E N G E R  W I L L  A R R I V E  S H O R T L Y! >> ")
                                input("Waiting for player's response... >> ")
                                character["cash"] += wager
                                battle = False
                                stagewin = True
            elif choice == "e":
                profile_menu = True
                while profile_menu:
                    print("Profile Menu")
                    print("A) Display Profile")
                    print("B) Update Profile")
                    print("C) Equip Weapon")
                    print("X) Back")
                    Choice = input("Enter a choice: ").lower()

                    if Choice == "x":
                        profile_menu = False
                    elif Choice == "a":
                        print("I======Basic======I")
                        print("  Name: " + character["name"])
                        print("  Level: " + character["level"].__str__())
                        print("  XP: ", character["exp"].__str__())
                        print("  XP needed for next level: ", (character["exp_to_lvl"] - character["exp"]).__str__())
                        print("  Applicable Stat points: " + character["statpoints"].__str__())
                        print("I=====Advanced====I")
                        print("  HP: " + character['hp'].__str__() + "/" + character['maxhp'].__str__())
                        print("  MP: " + character['mp'].__str__())
                        print("  ATK: " + character['atk'].__str__())
                        print("  DEF: " + character['def'].__str__())
                        print("I======Items======I")
                        for item in character["inv"]:
                            print(item)
                    elif Choice == 'b':
                        prompt = 0
                        stat_update = True
                        while stat_update:
                            if character['statpoints'] >= 1:
                                print("Stat Machine Is Here For You!")
                                print("Select Desired Stat To Upgrade:")
                                print("   A) ATK")
                                print("   D) DEF")
                                print("   H) MAX HP")
                                print("   R) RANDOMIZE STAT UPGRADE (COULD RESULT IN DECREASE OF STATS, BUT HAS HIGHER "
                                      "YIELD)")
                                print("   X) EXIT")
                                prompt = input("Choose one!").lower()
                                if prompt == "x":
                                    stat_update = False
                                    prompt = 0
                                elif prompt == "a":
                                    input(">>> Boosting ATK... ")
                                    input(">>> Generating Points... ")
                                    input(">>> Success! <<<")
                                    character['statpoints'] -= 1
                                    gained_point = random.randrange(1, 3)
                                    character['atk'] += gained_point
                                    print("ATK STAT BOOSTED BY " + gained_point.__str__() + "! YOU HAVE " +
                                          character["atk"].__str__() + " ATTACK!")
                                    input(">>>Waiting for player response...<<<")
                                elif prompt == 'd':
                                    input(">>> Boosting DEF... ")
                                    input(">>> Generating Points... ")
                                    input(">>> Success! <<<")
                                    character['statpoints'] -= 1
                                    gained_point = random.randrange(5, 15)
                                    character['def'] += gained_point
                                    print("DEF STAT BOOSTED BY " + gained_point.__str__() + "! YOU HAVE " +
                                          character["def"].__str__() + " DEFENSE!")
                                    input(">>>Waiting for player response...<<<")
                                elif prompt == 'h':
                                    input(">>> Boosting MAX HP... ")
                                    input(">>> Generating Points... ")
                                    input(">>> Success! <<<")
                                    character['statpoints'] -= 1
                                    gained_point = random.randrange(5, 15)
                                    character['maxhp'] += gained_point
                                    print("MAX HP STAT BOOSTED BY " + gained_point.__str__() + "! YOU HAVE " +
                                          character['hp'].__str__() + "/" + character["maxhp"].__str__() + " HP!")
                                    input(">>>Waiting for player response...<<<")
                                elif prompt == 'r':
                                    absolutely_certain = input("Are absolutely sure you want to randomize stats? You "
                                                               "could lose stats, or worse, render all fights "
                                                               "unwinnable. (y for yes, anything else for no) ").lower()
                                    if absolutely_certain == 'y':
                                        character["statpoints"] -= 1
                                        the_one = random.randrange(0, 2)
                                        if the_one == 0:
                                            gained_point = random.randrange(-3, 6)
                                            character["atk"] += gained_point
                                            print(gained_point.__str__() + " ATK points obtained.")
                                        elif the_one == 1:
                                            gained_point = random.randrange(-5, 30)
                                            character["def"] += gained_point
                                            print(gained_point.__str__() + " DEF points obtained.")
                                        elif the_one == 2:
                                            gained_point = random.randrange(-15, 60)
                                            character["maxhp"] += gained_point
                                            print(gained_point.__str__() + " MAX HP points obtained.")
                                stat_update = False
                            else:
                                input("Sorry, you don't have the points :/")
                                stat_update = False
                    elif Choice == 'c':
                        #ToDo
                        if hasGrandmaster or hasShield or hasNoobSword or hasSpear or is_knife_bought or golden_knife_bought:
                            print("Equip which weapon?")
                            if hasGrandmaster:
                                print("G) Grandmaster Wand")
                            elif hasNoobSword:
                                print("N) Noob Sword")
                            elif hasSpear:
                                print("S) Spear of Pokey-Pokes")
                            elif is_knife_bought:
                                print("K) Noob Knife")
                            elif golden_knife_bought:
                                print("Go) Golden Knife")
                            initiate = True
                            if initiate:
                                weap = input("Equip your weapon, please!").__lower__()
                                if weap == "g":
                                    weapon.clear()
                                    weapon.append({
                                        "name": "Grandmaster Wand",
                                    })
                        else:
                            print("Don't have any weapons!")
                            profile_menu = False
                    else:
                        profile_menu = False


            elif choice == "s":
                print("Chimichangas")
                exit(1337)
            else:
                print("B A D  C H O I C E ! ! ! !")
            print("   Wizard Menu")
            print(" I------------I")
            print("A) Train")
            print("B) Duel other wizards")
            print("C) Buy / Sell stuff")
            print("D) Adventure")
            print("E) Character Profile")
            print("S) Save")
            print("X) Exit")
            choice = input("Please enter choice: ").lower()




        new_game = True
    elif Choice.capitalize() == "C":
        print("        N O  C R E D I T S  Y E T ,  K A P P A")
    elif Choice.capitalize() == "X":
        exit(1337)
    elif Choice.capitalize() == "B":
        print("       E N T E R  A  G A M E  C O D E  H E R E ")
    else:
        print("   E N T E R  A  V A L I D  C H O I C E ,  K A P P A")






















        #I am the best hamster overlord praise me hahahahahahahahaha
        #you cannot hope to best me kappa
        #ahahahahahahahahahaha
        #you can just try to stop me >:D
        #I am the best hamster overlord praise me hahahahahahahahaha
        #you cannot hope to best me kappa
        #ahahahahahahahahahaha
        #you can just try to stop me >:D
        #I am the best hamster overlord praise me hahahahahahahahaha
        #you cannot hope to best me kappa
        #ahahahahahahahahahaha
        #you can just try to stop me >:D
        #I am the best hamster overlord praise me hahahahahahahahaha
        #you cannot hope to best me kappa
        #ahahahahahahahahahaha
        #you can just try to stop me >:D
        #I am the best hamster overlord praise me hahahahahahahahaha
        #you cannot hope to best me kappa
        #ahahahahahahahahahaha
        #you can just try to stop me >:D
        #I am the best hamster overlord praise me hahahahahahahahaha
        #you cannot hope to best me kappa
        #ahahahahahahahahahaha
        #you can just try to stop me >:D
        #I am the best hamster overlord praise me hahahahahahahahaha
        #you cannot hope to best me kappa
        #ahahahahahahahahahaha
        #you can just try to stop me >:D
        #I am the best hamster overlord praise me hahahahahahahahaha
        #you cannot hope to best me kappa
        #ahahahahahahahahahaha
        #you can just try to stop me >:D
        #I am the best hamster overlord praise me hahahahahahahahaha
        #you cannot hope to best me kappa
        #ahahahahahahahahahaha
        #you can just try to stop me >:D
        #I am the best hamster overlord praise me hahahahahahahahaha
        #you cannot hope to best me kappa
        #ahahahahahahahahahaha
        #you can just try to stop me >:D
        #I am the best hamster overlord praise me hahahahahahahahaha
        #you cannot hope to best me kappa
        #ahahahahahahahahahaha
        #you can just try to stop me >:D
        #I am the best hamster overlord praise me hahahahahahahahaha
        #you cannot hope to best me kappa
        #ahahahahahahahahahaha
        #you can just try to stop me >:D
        #I am the best hamster overlord praise me hahahahahahahahaha
        #you cannot hope to best me kappa
        #ahahahahahahahahahaha
        #you can just try to stop me >:D
        #I am the best hamster overlord praise me hahahahahahahahaha
        #you cannot hope to best me kappa
        #ahahahahahahahahahaha
        #you can just try to stop me >:D
        #I am the best hamster overlord praise me hahahahahahahahaha
        #you cannot hope to best me kappa
        #ahahahahahahahahahaha
        #you can just try to stop me >:D
        #I am the best hamster overlord praise me hahahahahahahahaha
        #you cannot hope to best me kappa
        #ahahahahahahahahahaha
        #you can just try to stop me >:D
        #I am the best hamster overlord praise me hahahahahahahahaha
        #you cannot hope to best me kappa
        #ahahahahahahahahahaha
        #you can just try to stop me >:D
        #I am the best hamster overlord praise me hahahahahahahahaha
        #you cannot hope to best me kappa
        #ahahahahahahahahahaha
        #you can just try to stop me >:D
        #I am the best hamster overlord praise me hahahahahahahahaha
        #you cannot hope to best me kappa
        #ahahahahahahahahahaha
        #you can just try to stop me >:D
        #I am the best hamster overlord praise me hahahahahahahahaha
        #you cannot hope to best me kappa
        #ahahahahahahahahahaha
        #you can just try to stop me >:D
        #I am the best hamster overlord praise me hahahahahahahahaha
        #you cannot hope to best me kappa
        #ahahahahahahahahahaha
        #you can just try to stop me >:D
