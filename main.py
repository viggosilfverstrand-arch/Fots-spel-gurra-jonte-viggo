# SÄTT TILL
from monster import *
import random as rand
from items import *
from character import *
import time
from questions import *
from spara import *
import os

# Characters
tank = Characterclass("Mr.Tank", 200, 10, 0.1, 2)
warrior = Characterclass("Warrior", 100, 25, 0.1, 2)
magi = Characterclass("Magician", 60, 35, 0.2, 1.5)
gambler = Characterclass("Gambler", 100, 1, 0.35, 1000)

# Weapon
Hands = Weapon("Händer", 1, 0.001, 1.2)
weapon_list1 = [Weapon("Svärd", 3, 0.1, 1.5),
                Weapon("Dolk", 2, 0.2, 1.5),
                Weapon("Smörkniv", 1.25, 0.9, 1000),
                Weapon("Yxa", 4, 0.05, 1.5),
                Weapon("Knogjärn", 2, 0.25, 1.25)]

BackseatWeapon = Weapon("Golfklubba", 5, 0.30, 1.4)

# Items
Item_list1 = [Item("Small_Health_Potion", 15, 1),
              Item("Medium_Helth_Potion", 30, 1),
              Item("Big_Health_Potion", 60, 1),
              Item("Damage_boost", 0, 1.1)]

# Monster
monster_list1 = [Monster("Skeleton", 40, 20, 1),
                 Monster("Goblin", 75, 10, 1),
                 Monster("Goon", 35, 5, 1),
                 Monster("Bandit", 50, 13, 1)]

monster_list2 = [Monster("Demon", 175, 28, 1),
                 Monster("Troll", 250, 18, 1),
                 Monster("Vandrande Själ", 100, 35, 1),
                 Monster("Varulv", 200, 23, 1)]

monster_list3 = [Monster("Jätte", 400, 35, 1),
                 Monster("Drake", 300, 45, 1),
                 Monster("Skuggriddare", 275, 50, 1),
                 Monster("Golem", 450, 20, 1)]

sandworm = Monster("Sandworm", 124, 24, 1)
Boss = Monster("The king of darkness", 600, 100, 1)

SkelettRaptor = Monster("Skelett Raptor", 100, 30, 1)
# Gameplay

def slowtype(text, tid):
    for a in text:
        print(a, end="", flush=True)   # End hindrar nyrad,    flush låter termineln skriva ut induviduella tecken innan hela raden är klar
        time.sleep(tid)
    print("\n")

print("""
         Welcome to the Sweelept!""")
loaded = False
while True:
    print(""" 
     Read about the Classes:
     1. Warrior               3. Tank
     2. Magiacan              4. Gambler
     
            5. Choose your class   6. Load save
     """)
    
    infosvar = input("Vad vill du göra? ")
    
    if infosvar == "1":
        print("""
        Född på slagfälten där stål möter storm,
        kan en  Warrior slips till en kompromisslös kombination av kraft,
        disciplin och taktiskt sinne. Deras förfäder vandrade från by till rike som legosoldater,
        vakter och hjältar – men alltid med ett personligt uppdrag som drivit dem vidare.
        Deras styrka ligger i balans: tillräckligt snabba för att slå först,
        tillräckligt tåliga för att överleva, tillräckligt smarta för att anpassa sig.
        För en Warrior är varje strid en chans att bevisa att viljekraft alltid är starkare än ödet
        """)
    elif infosvar == "2":
        print("""
        Magician föddes inte med kraft; de stal den ur kosmos.
        Åratal av studier, förbjudna tomes och riskfyllda ritualer har gett dem förmågan att manipulera eld, rum, tid och energi på avstånd.
        Varje besvärjelse de kastar sliter lite på deras kropp, men deras intellekt och precision gör dem dödligare än de flesta krigare.
        De vandrar världen i jakt på ny kunskap – och på att kontrollera de krafter som lika gärna kan förgöra dem som deras fiender.
        """)
    elif infosvar == "3":
        print("""
        Tank har stått i frontlinjen längre än de vill minnas och bär ärren efter otaliga belägringar.
        De har tränat sina kroppar till att uthärda det ingen annan överlever,
        och deras närvaro får fiender att tveka innan de slår.
        När världen hotas är Tank sista hindret mellan kaos och de oskyldiga – en levande fästning som aldrig ger upp.
        Deras styrka kommer inte bara från muskler, utan från en oböjlig vilja som vägrar låta någon falla bakom dem.
        """)
    elif infosvar == "4":
        print("""
        Gambler föddes med osannolik tur,
        men den välsignelsen visar ofta sina tänder.
        De lever för spänningen i risken: varje slag,
        varje kort, varje beslut är ett spel där universum tycks väga deras öde på en knivsegg.
        Deras strider präglas av vilda svängningar – från förödande kritiska träffar till total kollaps – och de accepterar båda resultaten som en del av spelet.
        Gambler vandrar mellan bord, tavernor och slagfält, alltid jagad av lyckans nyckfulla hand.
        """)
    elif infosvar == "5":
        print(""" 
          Classes:
          1. Warrior               3. Tank
          2. Magiacan              4. Gambler
          """)
        
        val = (input("Vilken karaktär vill du välja? "))
        
        if val == "1":
            playerclass = warrior
            print("Du valde klassen Warrior!")
            break
        elif val == "0":
            continue
        elif val == "2":
            playerclass = magi
            print("Du valde klassen Magician!")
            break
        elif val == "3":
            playerclass = tank
            print("Du valde klassen Tank!")
            break
        elif val == "4":
            playerclass = gambler
            print("Du valde klassen Gambler!")
            break
        else:
            print("skriv ett tal")
    elif infosvar == "6":
        playerclass = load_player()
        loaded = True  
        slowtype(f"Du laddade in dina gammla save som {playerclass.name} med {playerclass.money} guld",0.05)          # Hoppa namgivarnaern
        break
    else:
        print("skriv ett tal")
if loaded == False:
    playername = input("Vad ska din karaktär heta? ")
    print(f"Du valde namnet {playername}!")
    playerclass.weapon = Hands
    print("load false")
alive = True

def the_final_struggle(alive):
    alive = battle(Boss, playerclass, alive)
    if alive == False:
        slowtype("")
        return playerclass.alive

def korsningen():
    if playerclass.skog == True and playerclass.city == True and playerclass.grott == True:
        the_final_struggle(alive)
    plats = rand.randint(1, 3)  # Bestämmer vilken väg som du kommer till
    väghem = rand.randint(1, 2)  # Slumpar om du kan komma hem
    if väghem == 1:  # Väg hem finns
        print("Du kommer till en skog där stigen blir till en väg och till två stigar")
        time.sleep(2)
        vägval = input(
            "Vilken stig väljer du? 1 = Vägen, 2 = Stig nr1, 3 = Steg nr2")
        if vägval == "1":
            gårhem = "ja"
            return gårhem  # returnera värdern som player fått under äventyret
        else:
            print(f"Du går {vägval}")
    else:
        print("Du kommer till en skog där stigen blir till tre stigar")
        time.sleep(2)
        vägval = input(
            "Vilken stig väljer du? 1 = Stig , 2 = Stig nr1, 3 = Steg nr2")
        time.sleep(2)
        print(f"Du går {vägval}")
    return plats

def vägdecision():  # Väg val på de olika vägarna
    vägval3 = input("Vill du vända tillbaka? ja eller nej")
    if len(vägval3) == 2:
        vägsvar3 = 1      # Player vill vända tillbaka
    else:
        vägsvar = 2  # Vill forsätta
    return vägsvar

def Markanden():
    print("vällkomen till markanden")
    while True:
        time.sleep(2)
        print(f""" Vad vill du kolla på?        DU har {playerclass.money} guld
        Vapen: 1. Svärd      Damage: 3     Crit factor: 5/10    Pris: 30 guld
            2. Dolk          Damage: 2     Crit factor: 6/10    Pris: 20 guld
            3. Smörknikv     Damage: 1,05  Crit factor: 2/10    Pris: 5 guld
            4. Yxa           Damage: 4     Crit factor: 2/10    Pris: 40 guld
            5. Knogjärn      Damage: 2     Crit factor: 7/10    Pris: 30 guld

        Items: 6. Small Health Potion    + 15 Hp            Pris: 10 guld
               7. Medium Helth Potion    + 30 Hp            Pris: 20 guld
               8. Big Health Potion      + 60 Hp            Pris: 30 guld
               9. Damage boost           10 % Damage boost  Pris: 40 guld

               q. Lämna affären
        """)
        köpval = input("Vad vill du köpa")
        time.sleep(2)
        if köpval == "1":   #Svärd
            if playerclass.money >= 30:
                playerclass.amoney(-30)
                Vapen = weapon_list1[0]
                playerclass.weapon = Vapen
                print(f"Ditt nya vapen är ett Svärd!")
            else:
                print("Du har inte tillräckligt med pengar")
        elif köpval == "2":  #dolk
            if playerclass.money >= 20:
                playerclass.amoney(-20)
                Vapen = weapon_list1[1]
                playerclass.weapon = Vapen
            print("Ditt nya vappen är en Dolk")
        elif köpval == "3":  #Smörkniv
            if playerclass.money >= 10:
                playerclass.amoney(-10)
                Vapen = weapon_list1[2]
                playerclass.weapon = Vapen
                print("Ditt nya vappen är Smörkniv")
            else:
                print("Du har inte tillräckligt med pengar")
        elif köpval == "4":   #YXA
            if playerclass.money >= 40:
                playerclass.amoney(-40)
                Vapen = weapon_list1[3]
                playerclass.weapon = Vapen
                print("Ditt nya vappen är Yxa")
            else:
                print("Du har inte tillräckligt med pengar")
        elif köpval == "5":    #Knogjärn
            if playerclass.money >= 30:
                playerclass.amoney(-30)
                Vapen = weapon_list1[4]
                playerclass.weapon = Vapen
                print("Ditt nya vappen är Knogjärn")
            else:
                print("Du har inte tillräckligt med pengar")
        elif köpval == "6":
            if playerclass.money >= 10:
                playerclass.amoney(-10)
                playerclass.add_item(Item_list1[0])
            else:
                print("Du har inte tillräckligt med pengar")
        elif köpval == "7":
            if playerclass.money >= 20:
                playerclass.amoney(-20)
                playerclass.add_item(Item_list1[1])
            else:
                print("Du har inte tillräckligt med pengar")
        elif köpval == "8":
            if playerclass.money >= 30:
                playerclass.amoney(-30)
                playerclass.add_item(Item_list1[2])
            else:
                print("Du har inte tillräckligt med pengar")
        elif köpval == "9":
            if playerclass.money >= 40:
                playerclass.amoney(-40)
                playerclass.add_item(Item_list1[3])
            else:
                print("Du har inte tillräckligt med pengar")
        elif köpval == "q":
            break
        else:
            continue
    return 

def spin_number():
    n = 0.008
    for delay in [n]*129:
        o = rand.randint(1, 4)      
        if o == 1:
            b = "🍒"         
        elif o == 2:
            b = "🔔" 
        elif o == 3:
            b = "🍋"
        elif o == 4:
            b = "💎"

        print(f"\rSpinning: {b}", end=""  , flush=True)
        time.sleep(n)
        n += n*n


    if o == 1:
            b = "🍒"         
    elif o == 2:
            b = "🔔" 
    elif o == 3:
            b = "🍋"
    elif o == 4:
            b == "💎"
    print(f"\rResult:   {b} ")
    return b

def slots():
    slowtype("Välkomen till slotsen", 0.1)
    slowtype("Slots är ett awesome sätt att vinna pengar på", 0.1)
    slowtype("Du måste få tre av samma nummer för att kamma in stor vinsten som är 50", 0.1)
    slowtype("varje spin kostar 5 guld", 0.1)
    while True:
        print(f"Du har {playerclass.money} guld")
        if playerclass.money >= 1:
            slot = input("Vill du spinna? Ja / nej")
            if slot == "nej":           # Gjort med mening för just här måste man säga exact rätt för att dra
                slowtype("kom tillbaka tills slots snart, nästa vinst är bara ett drag ifrån!", 0.1)
                break
            else: 
                playerclass.amoney(-5)
                slot1 = spin_number()
                slot2 = spin_number()
                slot3 = spin_number()
        
            if slot1 == slot2 and slot2 == slot3:
                print("Du vann")
                playerclass.amoney(50)
            else:
                print("Du förlora")
        else:
            print("Du har för lite pengar")
            break
    return


def carddraw(kortlek, num):
    lef = len(num)      # Antal borttagna kort
    ko = rand.randint(0,51-lef)    #Drar bort antal tagna kort från range av index som slumpas fram
    kort = kortlek[ko]            # Drar ett kort vid ett visst index
    kortlek.pop(ko)              #Tar bort det indexet så kortet inte kan dras igen
    slowtype(f"The card {kort} was pulled", 0.1)       # marker vilket kort som dragits
    if kort == 11:             # Gör om korten till rätta värderna 
        kort = 10
    elif kort == 12:
        kort = 10
    elif kort == 13:
        kort = 10
    elif kort == 14:      # Gör 14 till A eftersom A har en speciel funktion i blackjack
        kort = "A"
    num.append(1)       #Lägger till att ett kort dragits
    return kort 
playerclass.amoney(20)

def blackjack():
    kortlek = list(range(2,15))*4          #flyttade in de i de funktion?   Generar en kortelek med 4st av varje kort
    num = []                             #Lagar hur många kort som tagits
    slowtype("Blackjack is one of the most famous card games in the world.",0.05)
    slowtype("You wanna hear about the Rules? Yes or No" , 0.05)
    RUles = input()
    RUles = RUles.upper()
    if RUles == "YES":
        slowtype("In blackjack you play against the dealer. The goal is to have a higher score thean dealer but not exeding 21", 0.05)
        slowtype("Knighs, Queens and kings all have the value of 10, while ace can take the value of both 11 and 1", 0.05)
        slowtype("You start by getting two cards, the dealr gets one visble card", 0.05)
        slowtype("Then you can decide to either Hit (grab another card) or stand (be pleased with your cards) then its the dealar turn to try to match your score", 0.05)
        slowtype("IF the score is equal you get back your own money", 0.1)
    slowtype("If you win, you get 2x the money back", 0.02)
    while True:      # Loop som låter användaren köra flera gånger utan att omvägar
        (slowtype(f"How much you wanna bet? Type 0 to leave. Rn you got {playerclass.money} ", 0.05))
        bet= input()  # Regesterar bet
        try:
            bet = int(bet)           # Sorterar ut tal som inte är intergers
        except:
            continue
        if bet == 0:
            break
        elif  bet <= playerclass.money: #Kontrollerar att playern har råd
            slowtype("Start of round", 0.1)  # Markerar
            spelarsumma = 0                  #Skapar vairbael
            spelar1 = carddraw(kortlek, num)   
            spelar2 = carddraw(kortlek, num) #Ger cardraw arguemenet kortlek och num som sparas från förra carddraw
            spelar2str = str(spelar2)       # Skaar str veriosner i syfte att lägga in det i en lista
            spelar1str = str(spelar1)
            dealer1 = carddraw(kortlek,num)
            spelarlista = [spelar1str] + [spelar2str]   # Skapar lista
            if spelar1 == "A":     # Gör om värdet på på "A" till 11 i syfte att ge det till värde summa
                spelar1 = 11
            if spelar2 == "A":
                spelar2 = 11
            spelarsumma += spelar1    
            spelarsumma += spelar2       #Adderar start korten till värde summan
            dealarlista = [dealer1]    
            dealersumma = 0 
            avgjort = False     # Bool variabel som användes för näst komman while lopp
            s = 1       # Variabeler som används i näst kommande for loopar och som sedan växer i looper för att funka som index till listor
            n=2
            if spelarsumma > 21:             # Nedan gör att om player får 2st A så kommer den ena göras om till värde 1 englit regler
                        if "A" in spelarlista:
                            spelarsumma -= 10 
                            i = spelarlista.index("A")
                            spelarlista[i] = "1"
            
            while spelarsumma<= 21 and dealersumma < 22 and avgjort == False:   # Nedans körs om ingen värde  är över 21 och det inte är avgjort ( sist i stand elif)
                slowtype(f"Du har korten {spelarlista[:n]} summa: {spelarsumma}  Dealarn har {dealarlista[:s]}", 0.05)   # ger infomration om utgångsläget
                slowtype("You wanna hit or stand? H/ S", 0.05)
                ba1 = input()    #Val
                ba1 = ba1.upper()          # Felhantering
                if ba1 == "H":
                    spelar3 = carddraw(kortlek,num)
                    va = str(spelar3)
                    spelarlista.append(va)
                    spelarlistanum = spelarlista
                    if "A" in spelarlistanum:
                        for i in range(len(spelarlistanum)):    #Kollar varje elemt i listan
                            if spelarlistanum[i] == "A":        # Om elementet på sen specfik plats är lika med A så byts den till värdet 11
                                spelarlistanum[i] = "11"
                    spelarsumma  += int(spelarlistanum[n])
                    if spelarsumma > 21:
                        
                        if "11" in spelarlista:
                            spelarsumma -= 10 
                            i = spelarlista.index("11")
                            spelarlista[i] = "1"
                        
                    n+=1
                
                elif ba1 == "S":
                    if dealer1 == "A":
                        dealer1 = 11
                    dealersumma += dealer1
                    while dealersumma <= 21 and dealersumma < spelarsumma:
                        slowtype(f"Du har {spelarlista[:n]} summa: {spelarsumma}. Delarn har {dealarlista[:s]} summa: {dealersumma}", 0.07)
                        slowtype("Dealern pulls", 0.1)
                        dealarnew = carddraw(kortlek,num)
                        vas = str(dealarnew)
                        dealarlista.append(vas)
                        dealernum = dealarlista
                        if "A" in dealernum:
                                for i in range(len(dealernum)):    #Kollar varje elemt i listan
                                    if dealernum[i] == "A":        # Om elementet på sen specfik plats är lika med A så byts den till värdet 11
                                        dealernum[i] = "11"
                        dealersumma  += int(dealernum[s])
                        s += 1
                        if dealersumma > 21:
                            if "11" in dealarlista:
                                dealersumma -= 10 
                                s = dealarlista.index("11")
                                dealarlista[i] = "1"
                        time.sleep(2)
                    avgjort = True

                    
                else:
                    print("Say H or S")
            slowtype(f"Dealern fick {dealersumma}",0.05)
            slowtype(f"Du fick {spelarsumma}",0.05)
            if spelarsumma > 21:
                print("Du förlora")
                playerclass.amoney(-bet)
            elif spelarsumma == dealersumma:
                print("Det är lika")
            elif dealersumma>21:
                print("you won")
                playerclass.amoney(bet)
            elif spelarsumma > dealersumma:
                print("Du vann")
                playerclass.amoney(bet)
            elif dealersumma > spelarsumma:
                print("Du förlorade")
                playerclass.amoney(-bet)
                
        else:
            slowtype("You dont have enough money",0.05)
    return

def baren():
    slowtype("You feel your worth taking a couple of drinks at the bar",0.1)
    slowtype("The bar is sleek and modern, featuring a long marble desk", 0.06)
    slowtype("At the moment it's pretty calm but you can see broken chair in a corner... \n probably the rest of a earlier bar fight",0.05)
    slowtype("You look for the bartender but he is nowwhere to be seen",0.1)
    slowtype("At the stools there is only two people filling the more than 20 seats", 0.07)
    slowtype("The first person is male who looks forty and has put his forhead agianst the counter, perhaps resting his neck while he continuously scrols through reels", 0.05)
    slowtype("And a girl look kinda sus", .07)
    while True:
        slowtype("What do you want to do?   1: Talk to the man  2. Sit alone  3. Leave the bar",0.07)
        barsvar = input()
        if barsvar == "1":
            slowtype("You approach the scrolling man", 0.1)
            slowtype("Mind me takeing a seat? you saying while trying to look laidback",0.07)
            slowtype("No at all. He responds without looking up from his phone",0.07)
            slowtype("What are you watching, looks imporant to you", .1)
            slowtype("It isnt, that's why it works", .1)
            slowtype("He puts his phone down and yells for the bartender", .1)
            slowtype("What can i get you? A voice answers",0.1)
            slowtype("Give me two dry martini",0.1)
            slowtype("You look aorund but dont see the bartender, only thingh you see is some women who is sitting a on the other side of the room", .1)
            slowtype("Where is he? you ask the man",.1)
            slowtype("It's all automated now. The old bartender got his left eye blind after some asshole threw glass bottle at him",0.1)
            slowtype("He was nice guy. The casion decided to replace him with some robot, they said it was to dangerous to work here",0.1)
            slowtype("That good right? You reply",0.1)
            slowtype("Maybe.. I think the company was happy to swap him out as he was popular and they had go give him a good salary",0.1)
            slowtype("I even think they hired the guy who threw the bottle",0.1)
            slowtype("Oh... yeay these casions are allway greedy",0.1)
            slowtype("Suddenly two glasses are elevated up from the desk, filled with liquour",0.1)
            slowtype("You like Dry Martini? you ask",0.1)
            slowtype("Not really, ever since my wife left me they havent tasted as good. I just drink it for the...",0.1)
            time.sleep(5)
            slowtype("Why do you drink it?",.1)
            slowtype("The man downs his drink and then stands up",0.1)
            slowtype("I think i gotta go to the toilet",0.1)
            slowtype("He walks away heading towards the toilet",0.1)
            slowtype("After a minute or two you hear a loud bang", 0.1)
            time.sleep(0.5)
            slowtype("You jump up", 0.1)
            slowtype("What the hell, what the hell was thhat!", 0.1)
            time.sleep(2)
            slowtype("Calm down little boy",0.1)
            slowtype("You turn around and see the women you saw earlier looking at you",0.1)
            slowtype("She is around thrity with brown hair",0.1)
            slowtype("This happen all the time here stopp screaming",0.1)
            slowtype("What happen all the time?", 0.1)
            slowtype("People killing thmeself, especally guys like him, alcholic men, puh!", 0.1)
            slowtype("They have nothing to do anymore, just relics like the dinousaurs, if i were in there boots i would also do it",.1)
            slowtype("Take seat with meeee, young man and we can talk", 0.1)
            slowtype("Do you want to talk to the women or leave the bar      1. Talk     2. Leave", 0.1)
            barval2 = input()
            if barval2 == "1":  
                slowtype("You walk forward and sit down beside her", 0.1)
                slowtype("She looks at you, want a drink? yes or no", 0.1)
                barval3 = input()
                barval3 = barval3.upper()
                if barval3 == "YES":
                    slowtype("She calls for a drink",0.1)
                    slowtype("What do you work with? you ask",0.1)
                    slowtype("Well im a hooker, she replies",0.1)
                    slowtype("A hooker why would you want to be hooker ",0.1)
                    slowtype("I dont want to but I made some stupid choices over the year and this is where I ended up",0.1)
                    slowtype("Im sorry to hear that, have you tried switching carrer? If I can call it a carrer", 0.1)
                    slowtype("Haha, but yes I tired but I dont really have the facilites needed",0.1)
                    slowtype("Two drinks now appear from the table as before",0.1)
                    slowtype("You cast a galnce towards the bathroom no sign that he is coming out ",0.1)
                    slowtype("You look back at your drinks and take a big sip to cool your anxiety",0.1)
                    slowtype("How does it taste, she asks you",0.1)
                    slowtype("Good I suppose maybe a tad strange like someone had dropped a pill in",0.1)
                    slowtype("You start feeling a bit sleepy suddenly and then everything goes black",0.1)
                    time.sleep(5)
                    slowtype("You wake upp on hard floor. You notice a strange smell that is unfamiliar",0.1)
                    slowtype("You manage to open your eyes when you realise that your in a bathroom",0.1)
                    slowtype("Still dizzy your manage to stand up, you go through your belongings",0.1)
                    slowtype("Weapons check, items check, wallet? That filthy whore took my walllet!",0.1)
                    playerclass.amoney = 0
                    slowtype("You burst trought the toilet door in pure rage",0.1)
                    slowtype("Outside lays the bar guy all messed up",0.1)
                    slowtype("This cant be for real, as you jump over his corpse to get to the door",0.1)
                    slowtype("This is the last time I will visit this bar",0.1)
            else: 
                slowtype("What do you work with? you ask",0.1)
                slowtype("Well im a hooker, she replies",0.1)
                slowtype("A hooker why would you want to be hooker ",0.1)
                slowtype("I dont want to but I made some stupid choices over the year and this is where I ended up",0.1)
                slowtype("Im sorry to hear that, have you tried switching carrer? If i can call it a carrer", 0.1)
                slowtype("Haha, but yes i tired but i dont really have the facilites needed",0.1)
                slowtype("Anyway i have to go now, got a client, Goodbye",0.1)
                slowtype("Do you want to stay in the bar or leave?     Yes or no")
                barsvar4 = input()
                barsvar4 = barsvar4.upper()
                if barsvar4 == "YES":
                    slowtype("Infront of you there is a instruction",.1)
                    slowtype("Just call for a drink if you need one!",0.1)
                    for ias in range(1,6):
                        if ias == 4:
                            slowtype("Things are looking all blurry now",0.1)
                        if ias == 5:
                            slowtype("Thingh are looking all fruity now",0.1)
                        slowtype("Want to order a drink?  it cost 2 gold.   Yes or no",0.07)
                        dricksvar = input()
                        
                        dricksvar = dricksvar.upper()
                        if dricksvar == "YES":
                            slowtype("-Give me Dry Martini!",0.1)
                            playerclass.amoney(-2)
                            slowtype("-Okay, one dry Martini, answers a robo voice",0.05)
                            time.sleep(2)
                            slowtype("One dry martini appears from inside the desk",0.1)
                            slowtype("You drink it",0.1)
                            
                        else:
                            slowtype("You know how to keep it moderate, and decide that's enough for now",0.1)
                            time.sleep(1)
                            break
                            return
                    slowtype("Everything goes black",0.2)                        #Blackout
                    time.sleep(5)
                    slowtype("You wake upp on hard floor, you notice a strange smell that is unfamiliar",0.1)
                    slowtype("You manage to open your eyes when you realise that your in a bathroom",0.1)
                    slowtype("Still dizzy your manage to stand up, you go troguht through your belongings",0.1)
                    slowtype("Weapons check, items check, wallet? Someone took my walllet!",0.1)
                    playerclass.amoney = 0
                    slowtype("You burst trought the toilet door in pure rage",0.1)
                    slowtype("Outside lays the guy who sat in the bar before, he is all messed up",0.1)
                    slowtype("This cant be for real.. you think, as you jump over his corpse to get to the door",0.1)
                    slowtype("This is the last place i visit this bar",0.1)
                
                break
        if barsvar == "2":
                slowtype("You take a free seat at the counter",0.1)
                slowtype("Infront of you there is a instruction",.1)
                slowtype("Just call for a drink if you need one!",0.1)
                for ias in range(1,6):
                    if ias == 4:
                        slowtype("Thingh are looking all blurry now",0.1)
                    if ias == 5:
                        slowtype("Thingh are looking all fruity now",0.1)
                    slowtype("Want to order a drink?  it cost 2 gold.   Yes or no",0.07)
                    dricksvar = input()
                    
                    dricksvar = dricksvar.upper()
                    if dricksvar == "YES":
                        slowtype("-Give me Dry Martini!",0.1)
                        playerclass.amoney(-2)
                        slowtype("-Okay, one dry Martini, answers a robo voice",0.05)
                        time.sleep(2)
                        slowtype("One dry martini appears from inside the desk",0.1)
                        slowtype("You drink it",0.1)
                        
                    else:
                        slowtype("You know how to keep it moderate, and decide that's enough for now",0.1)
                        time.sleep(1)
                        break
                        return
                slowtype("Everything goes black",0.2)                        #Blackout
                time.sleep(5)
                slowtype("You wake upp on hard floor, you notice a strange smell that is unfamiliar",0.1)
                slowtype("You manage to open your eyes when you realise that your in a bathroom",0.1)
                slowtype("Still dizzy your manage to stand up, you go troguht through your belongings",0.1)
                slowtype("Weapons check, items check, wallet? Someone took my walllet!",0.1)
                playerclass.money = 0
                slowtype("You burst trought the toilet door in pure rage",0.1)
                slowtype("Outside lays the guy who sat in the bar before, he is all messed up",0.1)
                slowtype("This cant be for real.. you think, as you jump over his corpse to get to the door",0.1)
                slowtype("This is the last place i visit this bar",0.1)
                break
        else:
            break
    slowtype("You leave the bar",0.1)
    return

def casion():
    slowtype("Welcome to the Freedom Casion!", 0.05)
    while True:
        slowtype(f""" What do want to play?     You have {playerclass.money} gold \n
              1. Slots   2.  Black Jack    3. The freedom bar   \n
                    4. Quiz         5. Leave""", 0.02)
        casval = input()
        if casval == "1":
            slowtype("You choose to play slots", 0.05)
            slots()
        elif casval == "2":
            blackjack()
        elif casval == "3":
            baren()
        elif casval == "4":
            slowtype("You decide to try your smarts in some quizzes", 0.05)
            Quiz()
        elif casval == "5":
            break
fråde = []
def Quiz():
    antalr = 0      # antal rätt i rad
    pwon = 0  # sparar hur mycket player vunnit totalt så kasinot kan ta tillbaka det
    slowtype("Welcome to our quiz there are a total of 20 questions you can answer",0.05)
    slowtype("You will only be able to answer each question once",.05)
    slowtype("Each question is a bet of 5 gold, if you answer right you get 10 gold back",.05)
    
    while True:
        if len(fråde) == 21:                 # Gjort för att man inte ska kunnas vara på frågor man redan fått och därmed kan 
            slowtype("It appears that you have answerd all questions we have...",0.05) 
            return                               # Går att runda genom att load saven så kommer fråde omställas
        ras = rand.randint(5,8)
        qr = rand.randint(5,7)
        if qr in fråde:
            continue
        if antalr >= ras:
            slowtype("The casino thinks you might be cheating they throw you out and take bake the money you won",.05)
            playerclass.amoney(-pwon)-j
            break
        slowtype("Do you want a question?    Yes or no",.05)
        quizval = input()
        quizval = quizval.upper()
        if quizval == "YES":
            fråde.append(qr)
            slowtype(questions[qr],.1)
            slowtype("What your answer ?      ( Answer with a number, example:  5  ))",.05)
            
            try:
                qsvar = int(input())
                if qsvar == qr:
                        slowtype("Right answer!",.05)
                        playerclass.amoney(5)
                        antalr += 1
                        pwon += 5
                
                if qsvar != qr:
                            slowtype("Wrong answer dumb ass!",.05)
                            slowtype(f"THe right answer was {qr}",0.05)
                            playerclass.amoney(-5)
                            antalr = 0

            except:
                slowtype("Your answer didn't have the correct format, there by the casions rules page two section one conercing answering of questions",.05)
                slowtype("It says \"If the patron can't formulate a answer by the rules we have the freedom to still charge him the inital bet \"",.05)
                playerclass.amoney(-5)
        else:
                slowtype("You leave the quiz",0.05)
                break
    return

    

def vägescape():  # Väg val på de olika vägarna
    while True:
        vägval4 = input("Vill du gå vänster eller höger?")
        try:
            if vägval3 == "vänster":
                vägsvar3 = 1      # Player vill gå vänstern
            else:
                vägsvar = 2  # Vill gå höger
                return vägsvar
            break
        except:
            print("Skriv om skriv rätt")

def monsterpullar():
    if playerclass.lvl < 5:
        monsterlista = monster_list1
    elif playerclass.lvl >= 5 and playerclass.lvl < 10:
        monsterlista = monster_list2
    else:
        monsterlista = monster_list3
    monsterval = rand.choice(monsterlista)
    print(f"Du ser monstret {monsterval.name}")
    return monsterval





def battle(monsterval, playerclass, alive):
    while playerclass.hp > 0 and monsterval.hp > 0:

        battlec = input(slowtype(f"""Vad vill du göra?   Du har {playerclass.hp} hp,
        {monsterval.name} har {monsterval.hp} hp
        1. Attackera
        2. Heala
        3. Försök att fly """,0.02))

        if battlec == "1":

            dmg = playerclass.str * playerclass.weapon.damage

            all_critrate = playerclass.critrate + playerclass.weapon.critrate
            if rand.random() <= all_critrate:
                dmg *= playerclass.crit_damage * playerclass.weapon.crit_damage
                print(f"Du fick en crit!, nu gör du {dmg} skada")
            else:
                print(f"Du attackerar och gör {dmg} skada")

            monsterval.hp -= dmg
            print(
                f"Du skadade {monsterval.name} med {dmg}! Nu har {monsterval.name} {monsterval.hp} hp kvar.")
        elif battlec == "2":
            pass
        # Heal

        elif battlec == "3":
            if rand.randint(1, 2) == 1:
                print("Du flydde från Monstret(fegis)")
                return
            else:
                print("Du misslyckades att fly")

        else:
            print("Skriv 1, 2 eller 3")
            continue

        if monsterval.hp <= 0:
            print("Du dödade monstret!")
            time.sleep(1)
            reward = monsterval.exp_reward()
            playerclass.add_exp(reward)
            belopp = monsterval.money_reward()
            print(f"Du fick {belopp} guld")
            playerclass.amoney(reward)
            print(f"Du fick {reward} xp")
            
            return 
        print(f"{monsterval.name} attackerar dig och gör {monsterval.dmg} skada!")
        playerclass.hp -= monsterval.dmg
        print(f"Nu har du {playerclass.hp}hp kvar")

        if playerclass.hp <= 0:
            print("Du blev besegrad av monstret!")
            playerclass.alive = False
            return playerclass



def grottvägen(alive):
    print("Efter att gått på stigen en tag kommer du fram till en grott öppning")
    time.sleep(2)

    print("Du kikar ner i den, grottan ser fuktig ut och har droppande stalaktiter")
    if vägdecision() == 1:  # Om man vänder så kommer man tillbaka till vägvalet
        return
    else:  # Forsätte
        print("Du går ner i grottan")
        time.sleep(2)
        print("Det är brant och dina knän får jobba hårt")
        time.sleep(2)
        print("Plöstlsigt halkar du till och ramlar")
        time.sleep(2)
        print("Du tumlar neråt, det gör ont,")
        time.sleep(2)
        print("Efter vad som känns som en evighet så stannar du entligen")
        time.sleep(2)
        print("Du reser dig upp och kollar dig omkring")
        time.sleep(2)
        print("En lång rak grotta du inte kan se slutet på")
        time.sleep(2)
        print("I perferin ser du rörelser, du vänder dig snabbt om och ser nåting springa mot dig")
        monsterval = monsterpullar()
        alive = battle(monsterval, playerclass, alive)
        if alive == False:          # Alive ändras i battle func
            return playerclass.alive        # Om du dör så slutar funk köras
    print("Efter du dödat monsteret går du vidare")
    time.sleep(3)  # import time
    print("Du hinner bara gå ett par minuter innan du hör något mullra, du vänder dig om och ser massor stenar rulla mot dig")
    time.sleep(5)
    print("Du lowkey ser ett samband i stenarna, nummrena 13 98 flashar i din hjärna")
    time.sleep(5)  # Låter användaren kolla på nummrerna
    os.system('cls' if os.name == 'nt' else 'clear')
  # Rensar temrinel
    stensvar = input("vilka var talen?  xx xx")
    time.sleep(2)
    if stensvar == "13 98":
        print("Du fick rätt, du undivker stenarna")
    else:
        print("Du såg inte visionen och blev träffad av en sten")
        playerclass.hp -= 10  # Tar bort liv från gubben
        print(f"Du har nu {playerclass.hp} hp")
    print("Efter stenraset går du vidare")
    time.sleep(5)
    print("Efter ett tag kommer du till en korsning")
    time.sleep(3)
    print("En skylt sitter uppsatt, på den står det")
    time.sleep(3)
    print("Gå vänster om du vill leva")
    if vägescape() == 1:
        print("Du går vänster")
        time.sleep(3)
        print("Grottan börjar snart ljusna och du känner luften bli varmare")
        if vägdecision == 1:  # playern vänder
            print("Du vänder tillbaka")
            time.sleep(3)
            print("Du kommer tillbaka till korsning och går förbi skylten ")
        else:
            print("Du går upp ur grottan")
            return               # Går upp ur grottan och cancela grott äventyret
    else:
        print("Du trotsar skyltens råd och går höger")
    time.sleep(3)
    print("Gången krymper, luften blir kallare. Eko av droppande vatten hörs överallt.")
    time.sleep(2)
    print("Grottan forsätter gå ner snart når vattnet dig upp till midjan")
    time.sleep(2)
    print("Det är svängar överallt, det känns som lybyrint")
    time.sleep(2)
    print("Plötsligt hör du ett isande skrik bakom dig,")
    time.sleep(2)
    afb = input("Vill du, 1 Gå mot ljudet eller 2 gå vidare")
    if afb == "1":
        print("Du vänder dig om och börjar gå")
        time.sleep(2)
        print("Allt ser normalt ut, inget konstigt")
        time.sleep(2)
        print("Kanske inbildade du dig bara")
        time.sleep(2)
        print("Efter ett tag ser du nåt som glimmar på vägen")
        time.sleep(2)
        print("En stor guldtand, intryck i en glipa")
        time.sleep(2)
        print("Den här kan noga vara värd en kosing tänker du")
    else:
        print("Du forsäter gå framåt")
        time.sleep(2)
        print("Rarariarar!")
        time.sleep(2)
        print("Någonting drar dig ner under vattnet")
        alive = battle(monsterval, playerclass, alive)
        if alive == False:          # Alive ändras i battle func
            return playerclass.alive
            
    print("Du fick 15 guldmynt")
    playerclass.amoney(15)
    # Öka pengar varibeln
    time.sleep(2)
    print("Du går vidare fast du är trött")
    time.sleep(2)
    print("Långsamt börjar grottan bli torrare")
    time.sleep(3)
    print("Efter en stund märker du att marken blir mjukare, nästan som sand")
    time.sleep(2)
    print("Det luktar fuktigt och mögel, luften känns tung")
    time.sleep(2)
    print("Du hör ett svagt ljud av något som rör sig under sanden")
    time.sleep(2)
    choice = input("Vill du, 1 undersöka ljudet eller 2 fortsätta framåt? ")

    if choice == "1":
        print("Du hukar dig ner och tittar försiktigt")
        time.sleep(2)
        print("Ett par små ögon som iaktar dig från sanden..")
        time.sleep(2)
        print("Du drar fram ditt vapen och förbereder dig för strid!")
        alive = battle(sandworm, playerclass, alive)
        if alive == False:
            return playerclass.alive
        time.sleep(2)
        print("Efter striden andas du ut och fortsätter vidare")
    else:
        print("Du väljer att inte störa det mystiska ljudet och fortsätter framåt")
        time.sleep(2)
        print("Sanden knastrar under dina fötter och gångarna blir smalare")
        print("Plötsligt ser du en stor hiss")
        print("Den ser gammal ut men den kanska funkar")
        hissvar = input("Vill du trycka på hissknappen?")
        if hissvar.len == 2:
            pass

    time.sleep(1)
    print("Plötsligt öppnar grottan upp sig till en enorm sal")
    time.sleep(2)
    print("Takets stalaktiter glittrar av fukt, och små floder rinner kors och tvärs")
    time.sleep(3)
    print("I mitten av salen ser du något som får ditt hjärta att slå snabbare")
    time.sleep(2)
    print("En gigantisk, glittrande drake sover bland högar av guld och skatter")
    time.sleep(2)
    choice2 = input(
        "Vill du, 1 smyga förbi draken eller 2 försöka ta lite skatt? ")

    if choice2 == "1":
        print("Du håller andan och smyger längs väggarna")
        time.sleep(2)
        print("Draken rör inte en muskel och du kommer fram till andra sidan salen")
        print("Du känner dig nöjd men adrenalinet pumpar fortfarande")
    else:
        print("Du tar ett steg mot skatten")
        print("Draken öppnar ett öga och låter ett öronbedövande vrål")
        time.sleep(2)
        # Kalla draken som monster
        alive = battle(monsterval, playerclass, alive)
        if alive == False:          # Alive ändras i battle func
            return playerclass.alive
        print("Efter en hård strid lämnar du salen med en bit av skatten")
    time.sleep(1)
    print("När du går vidare från salen blir grottan smalare och luften varmare")
    time.sleep(2)
    print("Du börjar se ljus som sipprar in från små sprickor ovanför")
    time.sleep(2)
    print("Det känns som att du närmar dig grottans slut")
    time.sleep(2)
    print("Men plötsligt hör du ett eko av fotsteg bakom dig")
    choice3 = input(
        "Vill du, 1 vända dig om eller 2 fortsätta framåt snabbt? ")
    if choice3 == "1":
        print("Du vänder dig om och ser en grupp skuggfigurer")
        time.sleep(2)
        print("De verkar inte se dig än, kanske kan du smyga undan?")
        stealth_choice = input(
            "Vill du, 1 smyga undan eller 2 konfrontera dem? ")
        if stealth_choice == "1":
            print("Du kryper längs väggarna och lyckas ta dig förbi utan problem")
        else:
            print("Du drar fram ditt vapen och striden börjar")
            # Slåss mot mystical men
            alive = battle(monsterval, playerclass, alive)
            if alive == False:          # Alive ändras i battle func
                return playerclass.alive
    else:
        print("Du rusar framåt och ignorerar fotstegen bakom dig")
        time.sleep(2)
        print("Pulsen dunkar i öronen men du känner ljuset bli starkare för varje steg")

    time.sleep(1)
    print("Slutligen når du grottans mynning")
    time.sleep(2)
    print("Solens ljus träffar ditt ansikte, och du andas de1n friska luften")
    playerclass.grott = True
    return 

grottvägen(alive)

def skogsvägen(alive):
    print("Efter ett tag kommer du fram till en mörk skog.")
    time.sleep(1)
    print("Du kliver in i den mörka skogen. Ljuset bakom dig försvinner nästan direkt när träden sluter sig över dig. Luften blir kylig och stilla. Något prasslar mellan stammarna, men du kan inte se vad. Skuggorna rör sig, och en obehaglig känsla kryper längs ryggen.")
    time.sleep(4)
    if vägdecision() == 1:
        print("Du fegar ut och bestämmer dig för att vandra hem.")
        return 
    else:
        print("Du går djupare in i skogen.")
        time.sleep(2)
        print("Efter ett tag hör du grenarna prassla bakom dig och du vänder dig snabbt om.")
        monsterval = monsterpullar()
        alive = battle(monsterval, playerclass, alive)
        if alive == False: 
            return playerclass.alive         # Alive ändras i battle func
            # global adventuring
            # adventuring = False
            # return
    print("Du fick 15 guldmynt eftersom att du beserade monstret!")
    playerclass.amoney(15)
    time.sleep(2)
    print("Efter fighten så fortsätter du in i den mörka skogen.")
    time.sleep(3)
    print("Du går sakta och samtdigt njuter av den lugna och stilla miljön.")
    time.sleep(2)
    print("Men helt plötsligt så börjar vinden ta sig och skyn går om till svart.")
    time.sleep(2)
    print("Det föredetta lugnet har nu gått om till en kraftfull storm och träden vajar rejält.")
    time.sleep(2)
    print("Bakifrån dig hörs ett högt knak och vänder dig om för att se ett gigantiskt träd falla mot din riktning")
    time.sleep(3)
    skogsträdfall = int(input("""                            Vill du:
1. Undvika vänster   2. Undvika höger   3. Slå sönder trädet oskadad"""))
    if skogsträdfall == 1:
        print("Du undvek trädet genom att göra en dramatisk rull åt vänster och kom ut oskaddad.")
    elif skogsträdfall == 2:
        print("Du undvek trädet genom att göra en dramatisk rull åt höger och kom ut oskaddad.")
    elif skogsträdfall == 3:
        print("Du försökte stoppa trädet med all din kraft, men blir till slut mosad.")
        alive = battle(monsterval, playerclass, alive)
        if alive == False:          # Alive ändras i battle func
            return playerclass.alive
        # global alive
        # alive = False
        # global adventuring
        # adventuring = False
        # return
    else:
        print(
            "Du svarade inte korrekt och hinner därför inte reagera på det fallande trädet.")
        time.sleep(3)
        print("Du dog.")
        alive = battle(monsterval, playerclass, alive)
        if alive == False:          # Alive ändras i battle func
            return playerclass.alive
        # global alive
        # alive = False
        # global adventuring
        # adventuring = False
        # return
    time.sleep(2)
    
    if vägdecision() == 1:
        print("Du bestämmer dig för att vända tillbaks.")
        return
    else:
        print("Efter katastrofen så fortsätter du djupare in i den mörka skogen medans du vandrar mellan de höga vajande träden, tills du känner att någonting inte riktigt stämmer.")
        time.sleep(4)
        print("2 röda ögon ses blinka mellan träden, och de verkar spana in just dig.")
        time.sleep(2)
        print("På mindre än en sekund löpar monstret och hoppar på dig!")
        time.sleep(2)
        monsterval = monsterpullar()
        alive = battle(monsterval, playerclass, alive)
        if alive == False:        # Alive ändras i battle func
            return playerclass.alive        
            # global adventuring
            # adventuring = False
            # return
        print("Efter ännu en till attack så känner du dig utmattad och fortsätter vandra med hopp om att du snart kommer ut ur denna läskiga skog.")
        time.sleep(4)
        print("Efter ett långt äventyr så ser du ett glimmer från skogens kant och bestämmer dig för att gå denns håll.")
        time.sleep(3)
        print("När du närmrar dig så inser du att det är en liten stuga.")
        time.sleep(2)
    while True:
        try: 
            Stuga_val = int(input("""      Vill du:
            1. Gå in i stugan       2. Strunta i stugan och fortsätta vandra"""))
            if Stuga_val == 1:
                slowtype("Du bestämmer dig för att gå in i stugan i hopp om resurser som kan hjälpa dig komma ut ur skogen.",0.1)
                slowtype("Du går fram till den lilla stugan och tar en titt in genom fönstret.",0.1)
                slowtype("Stugans insida ser väl behandlad ut, nästan som att någon bodde här ute i skogen.", 0.1)
                slowtype("Helt plötsligt hör du ett prassel bakom dig och du vänder dig hastigt om.",0.1)
                slowtype("Framför dig står en kort gammal dam som kollar på dig med nyfikna ögon.",0.1)
                slowtype("Men hallå där! Säger Damen.", 0.05)
                slowtype("H-hej, säger du osäkert tillbaks.",0.05)
                slowtype("Vad gör en ung äventyrare som dig här ute i denna farliga skog? undrar kvinnan.",0.05)
                while True:
                    try:   
                        damfråga = int(input("""Vad svarar du?
                        1. Skulle kunna fråga detsamma. 2. Inget för dig att veta! """))
                        if damfråga == 1:
                            slowtype("Om du inte redan visste det så bor jag här i min stuga som du just snokade runt. Svarade Damen.",0.05)
                            slowtype("Jag hoppas du vet att det inte är särskilt trevligt att snoka runt andras hus. Säger hon besviket.",0.05)
                            break
                        elif damfråga ==2:
                            slowtype("Förlåt för att jag frågade, menade inte att kränka dig. Svarade Damen.",0.05)
                            break
                        else:
                            print("Du gav inte ett giltigt svar, svara om.")
                    except:
                        print("Du gav inte ett giltigt svar, svara om.")
                
                slowtype("Kom in i min stuga, denna skog är inte säker under nätterna, dessutom ser det ut som att du behöver vila lite.")
                while True:
                    try:
                        damfråga2 =int(input("""Vad gör du?
                        1. Följer med damen in i stugan.   2. Säger nej och fortsätter att vandra i skogen."""))
                        if damfråga2 == 1:
                            slowtype("Du följer med damen.",0.05)
                            slowtype("Stugan är full med olika grejer, massor med olika växter och annat från skogen.",0.05)
                            slowtype("Varför bor du här ute? Frågar du damen.")
                            slowtype("Jag har alltid bott i dessa skogar. De är hela min barndom och jag kan inte få mig själv att flytta där ifrån. Det är också lungt dagarna om och jag slipper oftast personer som dig. Svarar damen", 0.05)
                            slowtype("Jahopp då, får du ur dig.",0.05)
                            time.sleep(1)
                            while True:
                                try:
                                    damfråga3 = int(input("""jag gjorde min favoritgryta till middag, vill du ha? Frågar damen. Vad gör du?
                                    1. Du tar villigt emot maten    2. Du avstår"""))
                                    if damfråga3 ==1:
                                        slowtype("Gärna! Säger du och tar emot en varm skål av grytan.",0.05)
                                        slowtype("Vad är det för gryta? Frågar du.")
                                        slowtype("Det är bara ett simpelt recept på en kaningryta jag brukade äta när jag var liten. Svarade damen.",0.1)
                                        slowtype("Du gladligt tar ett stort slurp ur grytan.",0.05)
                                        slowtype("WOW! Nästan skriker du rakt ut.",0.05)
                                        slowtype("Vad är det pojk? Undrar damen.",0.1)
                                        slowtype("Detta är den bästa grytan jag någonsin ätit i hela mitt liv! Säger du till damen.",0.05)
                                        slowtype("Jag känner mig typ starkare!!! Skriker du glatt.",0.05)
                                        slowtype("Men vad roligt att du gil... vad damen påväg att säga då hon blev avbruten av ett högt vrål.",0.05)
                                        slowtype("Det är nog dags att gå och lägga oss säger damen nervöst.",0.05)
                                        slowtype("Nästa dag vaknar du av att solen strålar i ditt ansikte",0.05)
                                        slowtype("Du går upp och hälsar på damen som redan står och lagar frukost.",0.05)
                                        slowtype("Det är nog dags för mig att gå min väg, men tack för att jag fick stanna här i natt. Säger du till damen.",0.05)
                                        slowtype("Innan du går! säger damen snabbt.",0.05)
                                        slowtype("Så vill jag ge dig en sak... fortsätter damen.",0.05)
                                        slowtype("Min man var en äventyrare innan han gick bort och han hade en styrkedryck som nu inte används.",0.05)
                                        slowtype("Jag tycker att du borde ta den om det kan hjälpa dig på något sätt.",0.05)
                                        
                                        
                                        break
                                    if damfråga3 ==2:
                                        slowtype("Jag kan avstå. Säger du.",0.05)
                                        slowtype("Skyll dig själv, mumlar damen.",0.05)
                                        break
                                    else:
                                        print("Du gav inte ett giltigt svar, svara om.")
                                except:
                                    print("Du gav inte ett giltigt svar, svara om.")
                            break
                        
                        elif damfråga2 ==2:
                            slowtype("Nej, svarar du och går din väg djupare in i skogen utan att kolla tillbaka.")
                            break
                        else:
                            print("Du gav inte ett giltigt svar, svara om.")
                    except:
                        print("Du gav inte ett giltigt svar, svara om.")
                break
            elif Stuga_val == 2:
                slowtype("Du bestämmer dig för att struna i stugan och fortsätter att vandra genom den täta skogen.",0.05)
                break
            else:
                print("Du gav inte ett giltigt svar, svara om.")
        except: 
            print("Du gav inte ett giltigt svar, svara om.")
        slowtype("Vinden blir starkare och starkare och framför dig ses en öppning mellan träden.",0.05)
        slowtype("Du har äntligen kommit ut ur den täta skogen och du kan nu fortsätta ditt äventyr starkare än någonsin.",0.05)
        playerclass.skog = True
        break


def abanondedcity(alive):
    print("Efter ett tag kommer du fram till vad du tror är en helt vanlig stad.")
    time.sleep(3)
    print("Men du märker att någonting är fel.")
    time.sleep(2)
    print("Fönstren är krossade, det växer gräs ur asfalten och det är helt tyst förutom vindens brus.")
    time.sleep(4)
    print("Det var nästan som att staden är övergiven.")
    time.sleep(2)
    print("När du funderar på vart du ska ta vägen så ser du en hög skyskrapa som bara kallar ditt namn och du bestämmer dig för att gå dit.")
    time.sleep(4)
    print("Du tar dig genom de övergivna gatorna och efter en lång vandring så kommer du äntligen fram till en otroligt höga byggnaden.")
    time.sleep(5)
    print("Du går in genom porten på den föredetta lyxiga byggnaden i hopp om att hitta resureser.")
    time.sleep(3)
    print("Du kollar runt i den lyxiga entrén som ser oväntande fräsh ut.")
    time.sleep(2)
    print("Allt verkar alldels för avkopplande tills...")
    time.sleep(2)
    monsterval = monsterpullar()
    alive = battle(monsterval, playerclass, alive)
    if alive == False:        # Alive ändras i battle func
        return playerclass.alive 
    if vägdecision() ==1:
        print("Du bestämmer dig för att vända tillbaks.")
        return
    print("Efter fighten så fortsätter du att gå runt i skyskrapan tills du hittar ett par trappor.")
    time.sleep(3)
    while True:
        try:
            trapporupellerner = int(input("""Vill du:
            1. Gå ner för trappan     2. Gå upp för trappan
            """))
            if trapporupellerner == 1:
                time.sleep(1)
                print("Du bestämde dig för att gå upp från trappan.")
                time.sleep(2)
                print("Denna våning verkar vara ett gammalt spelrum med otroligt många olika maskiner och kortspel.")
                time.sleep(3)
                print("Du kollar på alla olika slotmachines och märker att en av dem skapar ett konstigt pling ljud.")
                time.sleep(3)
                print("Du går fram till maskinen och bestämmer dig för att slå lite på den i hopp om att den kanske fortfarande fungerar.")
                time.sleep(3)
                print("Helt plötsligt så börjar den spela ett högt ljud och en lucka öppnar sig.")
                time.sleep(2) 
                print("Ut kom runt 20 mynt, det värkar vara din lyckodag!")
                time.sleep(2)
                print("Du plockar upp mynten och går din väg.")
                amoney(20)
                break
                        
            elif trapporupellerner == 2:
                time.sleep(1)
                print("Du bestämde dig för att gå ner för trappan.")
                time.sleep(2)
                print("Det verkar som att du gått in på föredetta garagevåningen.")
                time.sleep(2)
                print("Det finns lyxiga bilar på din vänster och höger men den som faktiskt väcker ditt intresse är en gammal mint condition Volkswagen Golf.")
                time.sleep(3)
                print("Du går fram till den vackra bilen och bestämmer dig för att se om den fungerar så du bryter dig in via fönsterrutan.")
                time.sleep(3)
                print("Solklart glömmer du ju bort att det behövs nycklar så du går ut ur bilen i misstro fast någonting glimmade till i baksätet och bestämmer dig för att tar ännu en tit in i bilen.")
                time.sleep(5)
                print("Det visade sig vara ett golfsett.")
                time.sleep(1)
                while True:
                    try:
                        time.sleep(2)
                        Tauppbackseatweapon = int(input(f"""Vill du plocka upp en golfklubba och byta ut den mot ditt nuvarande vapnet {Weapon.name}?
                        1. Ja     2. Nej"""))
                        if Tauppbackseatweapon == 1:
                            print(f"Du bytte ut {Weapon.name} mot en golfklubba")
                            Vapen = Weapon("Golfklubba")
                            playerclass.weapon = Vapen
                            break
                        elif Tauppbackseatweapon == 2:
                            print(f"Du behöll {Weapon.name} som ditt vapen.")
                            break
                        else:
                            print("Du gav inte ett giltigt svar, svara om.")
                    except:
                        print("Du gav inte ett giltigt svar, svara om.")
                            
                print("Efteråt återvände du tillbaks till stadens gator.")
                break
                        
            else:
                print("Du gav inte ett giltigt svar, svara om.")
        except:
            print("Du gav inte ett giltigt svar, svara om.")
    time.sleep(2)
    print("Efter ett långt äventyr så blev du klar med att undersöka skyskrapan och du kan äntligen gå hem.")
    time.sleep(3)
    print("I det trista väderet går du över de sprukna gatorna.")
    time.sleep(2)
    print("Det är knäpptyst i staden förutom vindens sus.")
    time.sleep(2)
    print("Men i tystnaden så hörs ett skräckinjagande vrål.")
    time.sleep(2)
    while True:
        try:
            museumfortsättaellerundersöka = int(input("""Vill du undersöka vrålet eller vill du fortsätta ut ur staden?
            1. Undersöka     2. Fortsätta"""))
            if museumfortsättaellerundersöka == 1:
                time.sleep(1)
                print("Du bestämmer dig för att undersöka vrålet och ändrar din gåriktning.")
                time.sleep(2)
                print("Vrålet forsätter och blir högre och högre för varje steg du tar.")
                time.sleep(2)
                print("Du börjar närma dig vrålets källa och kan snart se var detta skrämmande ljud kommer ifrån.")
                time.sleep(3)
                print("Framför dig syns en otroligt stor och urgammal byggnad, det verkar vara ett sorts museum.")
                time.sleep(2)
                if vägdecision() ==1:
                    print("Du bestämmer dig för att vända tillbaks.")
                    return
                time.sleep(2)
                print("Vrålet har ännu än inte slutat och du bestämmer dig för att går in och äntligen få reda på vad som skapar oljudet")
                time.sleep(3)
                print("Du öppnar lätt dörren och tar en liten titt in i museets entré.")
                time.sleep(2)
                print("Det chockande rent eftersom att det troligen inte varit någon här på flera decennier.")
                time.sleep(3)
                print("Du går in genom dörren och sekunden som porten stängs bakom dig så slutar plötsligt vrålandet och det blir helt knäpptyst.")
                time.sleep(3)
                slowtype("Efter lite inspektion visar det sig att museumet verkar vara ett gammalt naturhistorisk museum med massor med utrotade varelser, så som dinosaurier.", 0.05)
                slowtype("När du går runt och kollar på alla uppvisade dinosaurieskelett så märker du att någonting inre riktigt stämmer.", 0.05)
                time.sleep(2)
                slowtype("En av uppvisningsplattformarna är tomma.",0.05)
                slowtype("Medans då står och klurar på varför den är tom så känner du ett kyligt andetag gå nerför din nacke.",0.05)
                slowtype("Med hjälp av dina snabba reflexer så hoppar du precis undan en dödlig attack som slår i golvet med ett högt klang.", 0.05)
                alive = battle(SkelettRaptor, playerclass, alive)
                if alive == False:
                    return playerclass.alive
                slowtype("Grattis du besegrade monstret, som belöning får du 30 guldmynt!",0.05)
                playerclass.amoney(30)
                slowtype("Efter den farliga fighten mot Skelett Raptorn bestämmer du dig för att äntligen lämna denna övergivna stad och museum bakom dig och fortsätta med ditt primära äventyr.",0.05)
                slowtype("Efter ännu en lång tur kommer du till slut fram till där du lämnade för att undersöka vrålet, fast nu är det tyst och fridfullt.",0.05)
                break
            elif museumfortsättaellerundersöka ==2:
                time.sleep(1)
                slowtype("Du bestämmer dig för att strunta i vrålet och fortsätter istället åt samma håll som du först tänkte gå.",0.05)
                break
            else:
                print("Du gav inte ett giltigt svar, svara om.")
        except:
            print("Du gav inte ett giltigt svar, svara om.")
    slowtype("Efter denna otroligt långa och spännande turen genom staden så kan du äntligen fortsätta frammåt och besegra alla som kommer i din väg.",0.05)
    playerclass.city = True
    return

def biblloktekt():
    while True:
            bok_val = int(input("""        Var vill du gå?
                        1. Monster boks hyllan        2. Natur boks hyllan      3. Den vise mannen
                                                4. Gå tillbaka
                        """))
            

            if bok_val == 1:
                        monster_val = int(input("""    Vilket monster skulle du vilja läsa om?
                                        1. Skeleton     2. Goblin       3. Goon        4. Bandit
                                                        5. Troll        6. Varulv 
                                                                7. Lämna
                        """))
                        try:
                            if monster_val == 1:
                                    slowtype("""En forntida krigare vars själ aldrig fann ro. Benen är sammanbundna av förbannad vilja,\n
och i ögonhålorna lyser ett svagt blått sken. Skeletons vaknar där strider en gång rasade,
alltid redo att fortsätta ett krig som för länge sedan tagit slut.""", 0.05)
                            elif monster_val == 2:
                                    slowtype("""Små, gröna och evigt irriterande. Goblins trivs i skuggorna där de skrattar åt sina egna dumma skämt.\n
Deras svaga kroppar gör dem fega, men deras hastighet och list gör dem farliga i grupp.\n
En ensam goblin är ett problem – en flock är en katastrof.
""", 0.05)
                            elif monster_val == 3:
                                    slowtype(""" En trasig själ med en kropp som verkar ihopslängd av kaos självt. Goons är förvirrade, oberäkneliga och farliga.\n
De förstår inte rädsla, inte smärta och ibland inte ens att de är i en strid. Deras slumpslag kan vara både värdelösa – eller dödliga.
""", 0.05)
                            elif monster_val == 4:
                                    slowtype("""En före detta människa som valde mörka vägar.\n
Deras snabbhet, vassa knivar och ännu vassare instinkter gör dem dödliga plågoandar längs vägarna.\n
Banditer attackerar inte för nöje – utan för överlevnad.
""", 0.05)
                            elif monster_val == 5:
                                    slowtype(""" Troll föds ur jordens djup, formade av lera och sten.\n
De är långsamma i både huvud och kropp, men när de slår – skälver världen.\n
Många äventyrare föraktar troll, men få vet att deras hjärtan slår med sorg efter förlorade skogar.
                                    """, 0.05)
                            elif monster_val == 6:
                                    slowtype(""" En människa förbannad av månen. När skymningen faller förlorar de förståndet och förvandlas till en snabb, brutal predator.\n
Deras ylande ekar genom nattens skogar och deras klor lämnar djupa ärr i både trä och kött.
""", 0.05)
                            elif monster_val == 7:
                                break
                            else:
                                print("Skriv ett av de 7 nummer")
                        except:
                            print("Skriv om skriv rätt")

            elif bok_val == 2:
                        try:
                            natur_val = int(input("""       Vilken natur vill du läsa om?
                                        1. Grottvägen       2. Skogsvägen       3. Abanonded City
                                                            4. Lämna
                            """))
                            if natur_val == 1:
                                slowtype("""Grottvägen är en labyrint av trånga tunnlar och fuktiga gångar som har formats under tusentals år av rinnande vatten och erosion.\n
Droppstenar och stalaktiter hänger hotfullt från taket, och marken är halt och stenig.\n
Den här platsen har alltid varit en passage mellan världens yttre landskap och de djupare, hemliga underjordiska gångarna – fylld av mystik och faror.
""", 0.05)
                            elif natur_val == 2:
                                slowtype("""Skogsvägen slingrar sig genom täta skogar, där träden sträcker sig högt mot himlen och dimman ofta ligger tät mellan stammarna.\n
Marken är mjuk av mossa och fallna löv, och vinden får trädens grenar att knaka hotfullt.\n
Skogsvägen har funnits i århundraden som en naturlig passage för resande och äventyrare, men dess orörda djup rymmer både skönhet och fara\n
""", 0.05)
                            elif natur_val == 3:
                                slowtype(f"""Den övergivna staden är en ruin från en svunnen civilisation. \n
Krossade byggnader, trasiga gator och murar som rasat under tidens gång ger staden ett spöklikt utseende.\n
Staden byggdes en gång som ett centrum för handel och magi, men drabbades av okända katastrofer och övergavs.\n
Nu ekar tystnaden mellan ruinerna, och platsen bär på historiens mysterier och glömda hemligheter.
""", 0.05)
                            elif natur_val == 4:
                                break
                            else:
                                print("Skriv ett av de 4 nummer")
                        except:
                            print("Skriv om och skriv rätt")
                    
            elif bok_val == 3:
                    if playerclass.hybris == True:                         #chekar om playern har hybris
                        slowtype("The old man is not here anymore, wonder why...", 0.1)
                    else:
                            slowtype("Hello there young man", 0.15) 
                            slowtype("I'am the wise man of the village", 0.1)
                            gusval = input("Do you want to hear about my life? Ja / Nej")
                            gusval = gusval.upper()
                            if gusval == "NEJ":
                                slowtype("All these young men", 0.1)
                                time.sleep(0.5)
                                slowtype("How many have walked past me",0.1)
                                time.sleep(0.5)
                                slowtype("To never return ",0.1)
                                time.sleep(0.5)
                                slowtype("I have seen them all but not even Leonard Euler could have counted them ",0.1)
                                time.sleep(0.5)
                                slowtype("Goodbye", 0.1)
                                playerclass.hybris = True     #Sätter playern som hybris
                                
                            else:
                                slowtype("In my youth i was a adeventurer", 0.15)
                                time.sleep(0.5)
                                slowtype("I walked through caves that were so dark", 0.15)
                                time.sleep(0.5)
                                slowtype("Even god didn't know what lived down there", 0.15)
                                time.sleep(0.5)
                                slowtype("I walked in forests with tress so tall", 0.15)
                                time.sleep(0.5)
                                slowtype("Even the birds didnt know were they ended", 0.15)
                                time.sleep(0.5)
                                slowtype("And i walked through cities that were soo haunted", 0.15)
                                time.sleep(0.5)
                                slowtype("Even the devil had stoped counting the lost souls", 0.15)
                                time.sleep(0.5)
                                slowtype("After all my experinces abroad i returned home with fainted heart", 0.15)
                                time.sleep(0.5)
                                slowtype("I settled down and became the old man you see before you", 0.15)
                                time.sleep(2)
                                slowtype("But now on the sunset of my life", 0.12)
                                time.sleep(0.5)
                                slowtype("I wished i walked out there one more time", 0.1)
                                time.sleep(2)
                                slowtype("Becuase there is still something out there", 0.1)
                                time.sleep(0.5)
                                slowtype("A creature i only felt the aura from", 0.1)
                                time.sleep(0.5)
                                slowtype("Only when that king of darkness is erased can the world's darkness disappaear", 0.1)
                                time.sleep(0.5)
                                slowtype("Now son, i wish that you get out there deafeat him",0.1)
                                time.sleep(2)
                                slowtype("Only then can i die happy", 0.1)
                    break
                        
                    
            elif bok_val == 4: 
                        break
            else:
                        slowtype("Skriv ett av de 4 nummer", 0.2)
    return playerclass.hybris       #Skickar tillbaka om playern har hybris eller inte


        
            


def main(alive):
    while alive == True:
        time.sleep(1)
        print(f"""          Sweelept
        1. Äventyr       2. Markanden       3. Bibloteket
    
            4. Inventory     5. Casino
            
                         6. Save  
            """)
        time.sleep(1)
        Platsval = input("Vad vill du välja? ")
        if Platsval == "1":
            print("Du har valt att äventyra!")
            time.sleep(1)
            print("Du traskar ut ur staden och snart uppenbarare sig en skog där vägen försvinner till tre stigar")
            time.sleep(1)

            plats = korsningen()
            if plats == "ja":
                continue      # Slutar while loopen
            elif plats == 1:
                alive = grottvägen(alive)
            elif plats == 2:
                alive =skogsvägen(alive)
            elif plats == 3:
                alive = abanondedcity(alive)
            else:
                 print("error i main")
            if alive == False:
                print("fnaj")

        elif Platsval == "2":
            print("Du har valt att gå till markanden")
            Markanden()
        elif Platsval == "3":
            print("Du har valt att gå till biblloktekt")
            playerclass.hybris = biblloktekt()   #Sparar om playern har hybris eller inte
            

        elif Platsval == "4":
            playerclass.show_inventory()
            playerclass.show_weapon()
            # Stats allocation och stat check
        elif Platsval == "5":
            casion()
        elif Platsval == "6":
            save_player(playerclass)   
        else:
            pass


main(alive)
# li = []


# for i in range(10):
#     m = Monster("goblin", 10, 15, 22)
#     li.append(m)


# healthpotion = Items("Health_potion", 10, 0, 1)
# strengthpotion = Items("strength_potion", 0, 10, 1)


# svärd = Weapon("Snopp", 25, 1, 1)

# print(svärd)
