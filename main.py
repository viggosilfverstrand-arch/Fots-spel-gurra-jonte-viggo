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
tank = Characterclass("Mr.Tank", 200, 15, 0.1, 2)   # Eftersom hp är en attribut som inte har ett tak och som man kan förlora. Så förhållanden i gubbarna hp och Dmg
warrior = Characterclass("Warrior", 100, 20, 0.15, 2)  # Inte vara proportionelig. T.ex. så blir man av med hp varje battle som man sedan måste köpa i affären
magi = Characterclass("Magician", 60, 30, 0.2, 2)    # Eftersom hp boost för all genom köp av poitions i makrnaden är points och inte % av start hp eller ett hp tak
gambler = Characterclass("Gambler", 100, 1, 0.3, 200)  # Däför är en högre INITIAL dmg / hp generelt att föredra. Eftersom det låte dig scale bättre late game
                                                       # Genom den exponentiell öking av stats genom lvl upp bidrar till att den oförändrade dmg staten scalar bättre
                                                      # Än dmg som ibland kan vara låg pga battle. Detta är flaw som jag känner till. Vilket gör om man timear lvl dåligt
                                                   # Så kan man inte uttnyttja hp lvl up bra.

# Weapon

Hands = Weapon("Händer", 1, 0.001, 1.2)
weapon_list1 = [Weapon("Svärd", 1.5, 0.1, 1.5),
                Weapon("Dolk", 1.2, 0.2, 1.5),
                Weapon("Smörkniv", 1.25, 0.9, 100),
                Weapon("Yxa", 2, 0.05, 1.5),
                Weapon("Knogjärn", 1.2, 0.25, 1.25)]

BackseatWeapon = Weapon("Golfklubba", 5, 0.30, 1.4)

# Items
Item_list1 = [Item("Small Health Potion", 15, 1),
              Item("Medium Health Potion", 30, 1),
              Item("Big Health Potion", 60, 1),
              Item("Damage Potion", 0, 1.1)]

# Monster
monster_list1 = [Monster("Skeleton", 40, 20, 1),
                 Monster("Goblin", 75, 10, 1),
                 Monster("Goon", 35, 20, 1),
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
LevandeTräd = Monster("Levande Träd",150,20,1 )
FiskMänniska =Monster("FiskMänniska",100,25,1)
# Gameplay

def slowtype(text, tid):
    for a in text:
        print(a, end="", flush=True)   # End hindrar nyrad,    flush låter termineln skriva ut induviduella tecken innan hela raden är klar
        time.sleep(tid)
    print("\n")

slowtype("""
         Welcome to the Sweelept!""", 0.05)
loaded = False
while True:
    slowtype(""" 
     Read about the Classes:
     1. Warrior               3. Tank
     2. Magiacan              4. Gambler
     
            5. Choose your class   6. Load save
     """, 0.01)
    
    infosvar = input("Vad vill du göra? ")
    
    if infosvar == "1":
        slowtype("""
        Född på slagfälten där stål möter storm,
        kan en  Warrior slips till en kompromisslös kombination av kraft,
        disciplin och taktiskt sinne. Deras förfäder vandrade från by till rike som legosoldater,
        vakter och hjältar – men alltid med ett personligt uppdrag som drivit dem vidare.
        Deras styrka ligger i balans: tillräckligt snabba för att slå först,
        tillräckligt tåliga för att överleva, tillräckligt smarta för att anpassa sig.
        För en Warrior är varje strid en chans att bevisa att viljekraft alltid är starkare än ödet
        
        HP: 5/10    Dmg: 5/10   Critrate: 10%   Crit multiplier: 2x
        """, 0.01)
        input("Tryck enter för att fortsätta -> ")
    elif infosvar == "2":
        slowtype("""
        Magician föddes inte med kraft; de stal den ur kosmos.
        Åratal av studier, förbjudna tomes och riskfyllda ritualer har gett dem förmågan att manipulera eld, rum, tid och energi på avstånd.
        Varje besvärjelse de kastar sliter lite på deras kropp, men deras intellekt och precision gör dem dödligare än de flesta krigare.
        De vandrar världen i jakt på ny kunskap – och på att kontrollera de krafter som lika gärna kan förgöra dem som deras fiender.
        
        HP: 4/10    Dmg: 6/10   Critrate: 20%   Crit multiplier: 2x
        """, 0.01)
        input("Tryck enter för att fortsätta -> ")
    elif infosvar == "3":
        slowtype("""
        Tank har stått i frontlinjen längre än de vill minnas och bär ärren efter otaliga belägringar.
        De har tränat sina kroppar till att uthärda det ingen annan överlever,
        och deras närvaro får fiender att tveka innan de slår.
        När världen hotas är Tank sista hindret mellan kaos och de oskyldiga – en levande fästning som aldrig ger upp.
        Deras styrka kommer inte bara från muskler, utan från en oböjlig vilja som vägrar låta någon falla bakom dem.
        
        HP: 9/10    Dmg: 3/10   Critrate: 10%   Crit multiplier: 2x
        """, 0.01)
        input("Tryck enter för att fortsätta -> ")
    elif infosvar == "4":
        slowtype("""
        Gambler föddes med osannolik tur,
        men den välsignelsen visar ofta sina tänder.
        De lever för spänningen i risken: varje slag,
        varje kort, varje beslut är ett spel där universum tycks väga deras öde på en knivsegg.
        Deras strider präglas av vilda svängningar – från förödande kritiska träffar till total kollaps – och de accepterar båda resultaten som en del av spelet.
        Gambler vandrar mellan bord, tavernor och slagfält, alltid jagad av lyckans nyckfulla hand.
        
        HP: 5/10    Dmg: 1/10   Critrate: 30%   Crit multiplier: 200x
        """, 0.01)
        input("Tryck enter för att fortsätta -> ")
    elif infosvar == "5":
        slowtype(""" 
          Classes:
          1. Warrior               3. Tank
          2. Magiacan              4. Gambler
          """, 0.01)
        
        val = (input("Vilken karaktär vill du välja? "))
        
        if val == "1":
            playerclass = warrior
            slowtype("Du valde klassen Warrior!", 0.05)
            break
        elif val == "0":
            continue
        elif val == "2":
            playerclass = magi
            slowtype("Du valde klassen Magician!", 0.05)
            break
        elif val == "3":
            playerclass = tank
            slowtype("Du valde klassen Tank!", 0.05)
            break
        elif val == "4":
            playerclass = gambler
            slowtype("Du valde klassen Gambler!", 0.05)
            break
        else:
            slowtype("skriv ett tal", 0.05)
    elif infosvar == "6":
        playerclass = load_player()
        loaded = True  
        slowtype(f"Du laddade in dina gammla save som {playerclass.name} med {playerclass.money} guld",0.05)          # Hoppa namgivarnaern
        break
    else:
        slowtype("skriv ett tal", 0.05)
if loaded == False:
    playername = input("Vad ska din karaktär heta? ")
    slowtype(f"Du valde namnet {playername}!", 0.05)
    input("Tryck enter för att fortsätta -> ")
    os.system('cls' if os.name == 'nt' else 'clear')
    playerclass.weapon = Hands
alive = True


def the_final_struggle(alive):
    slowtype("Du förväntar dig att se de tre stigarna men den här gången så finns de inte",0.05)
    slowtype("Mörka moln drar in över himlen och det börjar regna",0.08)
    slowtype("Träden vajar och blixtar slår ner runt omkring dig",0.08)
    time.sleep(2)
    slowtype("Plöstlsigt så öppnas marken framför dig",0.08)
    slowtype(f"\" {playername} du har irriterat mig länge nu \"",0.08)
    slowtype(" \"Du har besegrat alla mina undersåtar... Men inte mej  \"",0.08)
    slowtype(" \"Jag är kungen av mörkret och du förtjänar att dö!   \"",0.08)
    alive = battle(Boss, playerclass, alive)
    if alive == False:
        return playerclass.alive


def korsningen():
    if playerclass.skog == True and playerclass.city == True and playerclass.grott == True:
        the_final_struggle(alive)
    plats = rand.randint(1, 3)  # Bestämmer vilken väg som du kommer till
    väghem = rand.randint(1, 2)  # Slumpar om du kan komma hem
    if väghem == 1:  # Väg hem finns
        slowtype("Du kommer till en skog där vägen delar sig till två stigar", 0.05)
        time.sleep(1)
        vägval = input(
            "1 = Gå hem, 2 = Fram, 3 = höger -> ")
        if vägval == "1":
            gårhem = "ja"
            return gårhem  # returnera värdern som player fått under äventyret
        else:
            slowtype(f"Du går stig {vägval}", 0.05)
    else:
        slowtype("Du går in i en skog och vägen försvinner bakom dig, eftert ett ag ser tre stigar", 0.05)
        time.sleep(2)
        vägval = input(
            "1 = Vänster , 2 = Fram, 3 = Höger -> ")
        time.sleep(2)
        slowtype(f"Du går stig {vägval}", 0.05)
    return plats

def vägdecision():  # Väg val på de olika vägarna
    while True:
        vägval3 = input("Vill du vända tillbaka? Ja eller Nej -> ").upper()
        try:
            if vägval3 == "JA" or vägval3 == "YES":
                os.system('cls' if os.name == 'nt' else 'clear')
                vägsvar = 1      # Player vill vända tillbaka
            elif vägval3 == "NEJ" or vägval3 == "NO":
                os.system('cls' if os.name == 'nt' else 'clear')
                vägsvar = 2  # Vill Fortsätta
            return vägsvar
        except:
            slowtype("gör om gör rätt", 0.05)

def Marknaden():
    slowtype("välkommen till marknaden", 0.05)
    while True:
        
        slowtype(f""" Vad vill du kolla på?        Du har {playerclass.money} guld
     Vapen: 1. Svärd         Damage: 1.5x     Crit factor: 10%    Pris: 30 guld
            2. Dolk          Damage: 1.2x     Crit factor: 20%    Pris: 20 guld
            3. Smörknikv     Damage: 1,05x    Crit factor: 5%     Pris: 5 guld
            4. Yxa           Damage: 2x       Crit factor: 5%     Pris: 40 guld
            5. Knogjärn      Damage: 1.2x     Crit factor: 25%    Pris: 30 guld

        Items: 6. Small Health Potion    + 15 Hp            Pris: 10 guld
               7. Medium Helth Potion    + 30 Hp            Pris: 20 guld       OBS!!! Du kan bara heala i menyn
               8. Big Health Potion      + 60 Hp            Pris: 30 guld
               9. Damage boost           10 % Damage boost  Pris: 40 guld

               q. Lämna affären
        """, 0.005)
        köpval = input("Vad vill du köpa? -> ")
        time.sleep(2)
        if köpval == "1":   #Svärd
            if playerclass.money >= 30:
                playerclass.amoney(-30)
                Vapen = weapon_list1[0]
                playerclass.weapon = Vapen
                slowtype(f"Ditt nya vapen är ett Svärd!", 0.05)
            else:
                slowtype("Du har inte tillräckligt med guld", 0.05)
        elif köpval == "2":  #dolk
            if playerclass.money >= 20:
                playerclass.amoney(-20)
                Vapen = weapon_list1[1]
                playerclass.weapon = Vapen
            slowtype("Ditt nya vapen är en Dolk", 0.05)
        elif köpval == "3":  #Smörkniv
            if playerclass.money >= 5:
                playerclass.amoney(-5)
                Vapen = weapon_list1[2]
                playerclass.weapon = Vapen
                slowtype("Ditt nya vapen är Smörkniv", 0.05)
            else:
                slowtype("Du har inte tillräckligt med guld", 0.05)
        elif köpval == "4":   #YXA
            if playerclass.money >= 40:
                playerclass.amoney(-40)
                Vapen = weapon_list1[3]
                playerclass.weapon = Vapen
                slowtype("Ditt nya vapen är Yxa", 0.05)
            else:
                slowtype("Du har inte tillräckligt med guld", 0.05)
        elif köpval == "5":    #Knogjärn
            if playerclass.money >= 30:
                playerclass.amoney(-30)
                Vapen = weapon_list1[4]
                playerclass.weapon = Vapen
                slowtype("Ditt nya vapen är Knogjärn", 0.05)
            else:
                slowtype("Du har inte tillräckligt med guld", 0.05)
        elif köpval == "6":
            if playerclass.money >= 10:
                playerclass.amoney(-10)
                playerclass.add_item(Item_list1[0])
            else:
                slowtype("Du har inte tillräckligt med guld", 0.05)
        elif köpval == "7":
            if playerclass.money >= 20:
                playerclass.amoney(-20)
                playerclass.add_item(Item_list1[1])
            else:
                slowtype("Du har inte tillräckligt med guld", 0.05)
        elif köpval == "8":
            if playerclass.money >= 30:
                playerclass.amoney(-30)
                playerclass.add_item(Item_list1[2])
            else:
                slowtype("Du har inte tillräckligt med guld", 0.05)
        elif köpval == "9":
            if playerclass.money >= 40:
                playerclass.amoney(-40)
                playerclass.add_item(Item_list1[3])
            else:
                slowtype("Du har inte tillräckligt med guld", 0.05)
        elif köpval == "q":
            os.system('cls' if os.name == 'nt' else 'clear')
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
    return

def slots():
    slowtype("Välkommen till slotsen", 0.05)
    slowtype("Slots är ett awesome sätt att vinna guld på", 0.05)
    slowtype("Du måste få tre av samma nummer för att kamma in stor vinsten som är 50", 0.05)
    slowtype("varje spin kostar 5 guld", 0.05)
    while True:
        slowtype(f"Du har {playerclass.money} guld", 0.05)
        if playerclass.money >= 1:
            slot = input("Vill du spinna? Ja / nej").upper()
            if slot == "NEJ":           # Gjort med mening för just här måste man säga exact rätt för att dra
                slowtype("kom tillbaka tills slots snart, nästa vinst är bara ett drag ifrån!", 0.05)
                break
            else: 
                playerclass.amoney(-5)
                slot1 = spin_number()
                slot2 = spin_number()
                slot3 = spin_number()
        
            if slot1 == slot2 and slot2 == slot3:
                slowtype("Du vann", 0.05)
                playerclass.amoney(50)
            else:
                slowtype("Du förlora", 0.05)
        else:
            slowtype("Du har för lite guld", 0.05)
            break
    return


def carddraw(kortlek, num):
    lef = len(num)      # Antal borttagna kort
    ko = rand.randint(0,51-lef)    #Drar bort antal tagna kort från range av index som slumpas fram
    kort = kortlek[ko]            # Drar ett kort vid ett visst index
    kortlek.pop(ko)              #Tar bort det indexet så kortet inte kan dras igen
    slowtype(f"The card {kort} was pulled", 0.05)       # marker vilket kort som dragits
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
        slowtype("IF the score is equal you get back your own money", 0.05)
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
            slowtype("Start of round", 0.05)  # Markerar
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
                        slowtype("Dealern pulls", 0.05)
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
                    slowtype("Say H or S", 0.05)
            slowtype(f"Dealern fick {dealersumma}",0.05)
            slowtype(f"Du fick {spelarsumma}",0.05)
            if spelarsumma > 21:
                slowtype("Du förlora", 0.05)
                playerclass.amoney(-bet)
            elif spelarsumma == dealersumma:
                slowtype("Det är lika", 0.05)
            elif dealersumma>21:
                slowtype("you won", 0.05)
                playerclass.amoney(bet)
            elif spelarsumma > dealersumma:
                slowtype("Du vann", 0.05)
                playerclass.amoney(bet)
            elif dealersumma > spelarsumma:
                slowtype("Du förlorade", 0.05)
                playerclass.amoney(-bet)
                
        else:
            slowtype("You dont have enough money",0.05)
    return

def baren():
    slowtype("You feel your worth taking a couple of drinks at the bar",0.05)
    slowtype("The bar is sleek and modern, featuring a long marble desk", 0.06)
    slowtype("At the moment it's pretty calm but you can see broken chair in a corner... \n probably the rest of a earlier bar fight",0.05)
    slowtype("You look for the bartender but he is nowwhere to be seen",0.05)
    slowtype("At the stools there is only two people filling the more than 20 seats", 0.07)
    slowtype("The first person is male who looks forty and has put his forhead agianst the counter, perhaps resting his neck while he continuously scrols through reels", 0.05)
    slowtype("And a girl look kinda sus", .07)
    while True:
        slowtype("What do you want to do?   1: Talk to the man  2. Sit alone  3. Leave the bar",0.07)
        barsvar = input()
        if barsvar == "1":
            slowtype("You approach the scrolling man", 0.05)
            slowtype("Mind me takeing a seat? you saying while trying to look laidback",0.07)
            slowtype("No at all. He responds without looking up from his phone",0.07)
            slowtype("What are you watching, looks imporant to you", 0.05)
            slowtype("It isnt, that's why it works", 0.05)
            slowtype("He puts his phone down and yells for the bartender", 0.05)
            slowtype("What can i get you? A voice answers",0.05)
            slowtype("Give me two dry martini",0.05)
            slowtype("You look aorund but dont see the bartender, only thingh you see is some women who is sitting a on the other side of the room", 0.05)
            slowtype("Where is he? you ask the man", 0.05)
            slowtype("It's all automated now. The old bartender got his left eye blind after some asshole threw glass bottle at him",0.05)
            slowtype("He was nice guy. The casion decided to replace him with some robot, they said it was to dangerous to work here",0.05)
            slowtype("That good right? You reply",0.05)
            slowtype("Maybe.. I think the company was happy to swap him out as he was popular and they had go give him a good salary",0.05)
            slowtype("I even think they hired the guy who threw the bottle",0.05)
            slowtype("Oh... yeay these casions are allway greedy",0.05)
            slowtype("Suddenly two glasses are elevated up from the desk, filled with liquour",0.05)
            slowtype("You like Dry Martini? you ask",0.05)
            slowtype("Not really, ever since my wife left me they havent tasted as good. I just drink it for the...",0.05)
            time.sleep(5)
            slowtype("Why do you drink it?",.1)
            slowtype("The man downs his drink and then stands up",0.05)
            slowtype("I think i gotta go to the toilet",0.05)
            slowtype("He walks away heading towards the toilet",0.05)
            slowtype("After a minute or two you hear a loud bang", 0.05)
            time.sleep(0.5)
            slowtype("You jump up", 0.05)
            slowtype("What the hell, what the hell was thhat!", 0.05)
            time.sleep(2)
            slowtype("Calm down little boy",0.05)
            slowtype("You turn around and see the women you saw earlier looking at you",0.05)
            slowtype("She is around thrity with brown hair",0.05)
            slowtype("This happen all the time here stopp screaming",0.05)
            slowtype("What happen all the time?", 0.05)
            slowtype("People killing thmeself, especally guys like him, alcholic men, puh!", 0.05)
            slowtype("They have nothing to do anymore, just relics like the dinousaurs, if i were in there boots i would also do it", 0.05)
            slowtype("Take seat with meeee, young man and we can talk", 0.05)
            slowtype("Do you want to talk to the women or leave the bar      1. Talk     2. Leave", 0.05)
            barval2 = input()
            if barval2 == "1":  
                slowtype("You walk forward and sit down beside her", 0.05)
                slowtype("She looks at you, want a drink? yes or no", 0.05)
                barval3 = input()
                barval3 = barval3.upper()
                if barval3 == "YES":
                    slowtype("She calls for a drink",0.05)
                    slowtype("What do you work with? you ask",0.05)
                    slowtype("Well im a hooker, she replies",0.05)
                    slowtype("A hooker why would you want to be hooker ",0.05)
                    slowtype("I dont want to but I made some stupid choices over the year and this is where I ended up",0.05)
                    slowtype("Im sorry to hear that, have you tried switching carrer? If I can call it a carrer", 0.05)
                    slowtype("Haha, but yes I tired but I dont really have the facilites needed",0.05)
                    slowtype("Two drinks now appear from the table as before",0.05)
                    slowtype("You cast a galnce towards the bathroom no sign that he is coming out ",0.05)
                    slowtype("You look back at your drinks and take a big sip to cool your anxiety",0.05)
                    slowtype("How does it taste, she asks you",0.05)
                    slowtype("Good I suppose maybe a tad strange like someone had dropped a pill in",0.05)
                    slowtype("You start feeling a bit sleepy suddenly and then everything goes black",0.05)
                    time.sleep(5)
                    slowtype("You wake upp on hard floor. You notice a strange smell that is unfamiliar",0.05)
                    slowtype("You manage to open your eyes when you realise that your in a bathroom",0.05)
                    slowtype("Still dizzy your manage to stand up, you go through your belongings",0.05)
                    slowtype("Weapons check, items check, wallet? That filthy whore took my walllet!",0.05)
                    playerclass.amoney = 0
                    slowtype("You burst trough the toilet door in pure rage",0.05)
                    slowtype("Outside lays the bar guy all messed up",0.05)
                    slowtype("This cant be for real, as you jump over his corpse to get to the door",0.05)
                    slowtype("This is the last time I will visit this bar",0.05)
            else: 
                slowtype("What do you work with? you ask",0.05)
                slowtype("Well im a hooker, she replies",0.05)
                slowtype("A hooker why would you want to be hooker ",0.05)
                slowtype("I dont want to but I made some stupid choices over the year and this is where I ended up",0.05)
                slowtype("Im sorry to hear that, have you tried switching carrer? If i can call it a carrer", 0.05)
                slowtype("Haha, but yes i tired but i dont really have the facilites needed",0.05)
                slowtype("Anyway i have to go now, got a client, Goodbye",0.05)
                slowtype("Do you want to stay in the bar or leave?     Yes or no", 0.05)
                barsvar4 = input()
                barsvar4 = barsvar4.upper()
                if barsvar4 == "YES":
                    slowtype("Infront of you there is a instruction", 0.05)
                    slowtype("Just call for a drink if you need one!",0.05)
                    for ias in range(1,6):
                        if ias == 4:
                            slowtype("Things are looking all blurry now",0.05)
                        if ias == 5:
                            slowtype("Thingh are looking all fruity now",0.05)
                        slowtype("Want to order a drink?  it cost 2 gold.   Yes or no",0.07)
                        dricksvar = input()
                        
                        dricksvar = dricksvar.upper()
                        if dricksvar == "YES":
                            slowtype("-Give me Dry Martini!",0.05)
                            playerclass.amoney(-2)
                            slowtype("-Okay, one dry Martini, answers a robo voice",0.05)
                            time.sleep(2)
                            slowtype("One dry martini appears from inside the desk",0.05)
                            slowtype("You drink it",0.05)
                            
                        else:
                            slowtype("You know how to keep it moderate, and decide that's enough for now",0.05)
                            time.sleep(1)
                            break
                            return
                    slowtype("Everything goes black",0.05)                        #Blackout
                    time.sleep(5)
                    slowtype("You wake upp on hard floor, you notice a strange smell that is unfamiliar",0.05)
                    slowtype("You manage to open your eyes when you realise that your in a bathroom",0.05)
                    slowtype("Still dizzy your manage to stand up, you go troguht through your belongings",0.05)
                    slowtype("Weapons check, items check, wallet? Someone took my walllet!",0.05)
                    playerclass.amoney = 0
                    slowtype("You burst through the toilet door in pure rage",0.05)
                    slowtype("Outside lays the guy who sat in the bar before, he is all messed up",0.05)
                    slowtype("This cant be for real.. you think, as you jump over his corpse to get to the door",0.05)
                    slowtype("This is the last place i visit this bar",0.05)
                
                break
        if barsvar == "2":
                slowtype("You take a free seat at the counter",0.05)
                slowtype("Infront of you there is a instruction", 0.05)
                slowtype("Just call for a drink if you need one!",0.05)
                for ias in range(1,6):
                    if ias == 4:
                        slowtype("Thingh are looking all blurry now",0.05)
                    if ias == 5:
                        slowtype("Thingh are looking all fruity now",0.05)
                    slowtype("Want to order a drink?  it cost 2 gold.   Yes or no",0.07)
                    dricksvar = input()
                    
                    dricksvar = dricksvar.upper()
                    if dricksvar == "YES":
                        slowtype("-Give me Dry Martini!",0.05)
                        playerclass.amoney(-2)
                        slowtype("-Okay, one dry Martini, answers a robo voice",0.05)
                        time.sleep(2)
                        slowtype("One dry martini appears from inside the desk",0.05)
                        slowtype("You drink it",0.05)
                        
                    else:
                        slowtype("You know how to keep it moderate, and decide that's enough for now",0.05)
                        time.sleep(1)
                        break
                        return
                slowtype("Everything goes black",0.2)                        #Blackout
                time.sleep(5)
                slowtype("You wake upp on hard floor, you notice a strange smell that is unfamiliar",0.05)
                slowtype("You manage to open your eyes when you realise that your in a bathroom",0.05)
                slowtype("Still dizzy your manage to stand up, you go through your belongings",0.05)
                slowtype("Weapons check, items check, wallet? Someone took my walllet!",0.05)
                playerclass.money = 0
                slowtype("You burst through the toilet door in pure rage",0.05)
                slowtype("Outside lays the guy who sat in the bar before, he is all messed up",0.05)
                slowtype("This cant be for real.. you think, as you jump over his corpse to get to the door",0.05)
                slowtype("This is the last place i visit this bar",0.05)
                break
        else:
            break
    slowtype("You leave the bar",0.05)
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
            
            qsvar = int(input())
            try:
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
        vägval3 = input("Vill du gå vänster eller höger? -> ")
        try:
            if vägval3 == "vänster" :
                vägsvar = 1      # Player vill gå vänstern
            elif vägval3 == "höger":
                vägsvar = 2  # Vill gå höger
            else:
                slowtype("Du skrev fel", 0.05)
            return vägsvar
            break
        except:
            slowtype("Skriv om skriv rätt", 0.05)

def monsterpullar():
    if playerclass.lvl < 4:
        monsterlista = monster_list1
    elif playerclass.lvl >= 4 and playerclass.lvl < 8:
        monsterlista = monster_list2
    else:
        monsterlista = monster_list3
    monsterval = rand.choice(monsterlista)
    slowtype(f"Du ser monstret {monsterval.name}", 0.1)
    time.sleep(1)
    return monsterval





def battle(monsterval, playerclass, alive):
    while playerclass.hp > 0 and monsterval.hp > 0:

        slowtype(f"""Vad vill du göra?   Du har {playerclass.hp} hp,
        {monsterval.name} har {monsterval.hp} hp
        1. Attackera
        2. Försök att fly """,0.02)
        battlec = input("-> ")

        if battlec == "1":

            dmg = playerclass.str * playerclass.weapon.damage 

            all_critrate = playerclass.critrate + playerclass.weapon.critrate
            if rand.random() <= all_critrate:
                dmg *= playerclass.crit_damage * playerclass.weapon.crit_damage # Här gör man multipcirar man vapen_skada * karaktär_skada * karaktär_crit * vapen_crit
                slowtype(f"Du fick en crit!, nu gör du {dmg} skada", 0.02)
            else:
                pass

            monsterval.hp -= dmg
            slowtype(
                f"Du skadade {monsterval.name} och gjorde {dmg} skada! Nu har {monsterval.name} {monsterval.hp} hp kvar.", 0.02)

        elif battlec == "2":
            if rand.randint(1, 2) == 1:
                slowtype("Du flydde från Monstret(fegis)", 0.02)
                return
            else:
                slowtype("Du misslyckades att fly", 0.07)

        else:
            slowtype("Skriv 1, 2 eller 3", 0.02)
            continue

        if monsterval.hp <= 0:
            slowtype("Du dödade monstret!", 0.05)
            time.sleep(1)
            reward = monsterval.exp_reward()
            playerclass.add_exp(reward)
            belopp = monsterval.money_reward()
            slowtype(f"Du fick {belopp} guld", 0.05)
            playerclass.amoney(belopp)
            slowtype(f"Du fick {reward} xp", 0.05)
            
            return 
        if rand.random() < 0.1:
            monsterval.dmg *=1.2
            monsterval.dmg = round(monsterval.dmg)
            slowtype("Monstret fick en crit!!!", 0.02)
        slowtype(f"{monsterval.name} attackerar dig och gör {monsterval.dmg} skada!", 0.02)
        playerclass.hp -= monsterval.dmg
        slowtype(f"Nu har du {playerclass.hp}hp kvar", 0.02)
        input("Tryck enter för att fortsätta ->")
        os.system('cls' if os.name == 'nt' else 'clear')

        if playerclass.hp <= 0:
            slowtype("Du blev besegrad av monstret!", 0.1)
            playerclass.alive = False
            return playerclass.alive

def grottvägen(alive):
    slowtype("Efter att du har gått på stigen ett tag kommer du fram till en grott öppning.", 0.05)
    time.sleep(1)

    slowtype("Du kikar ner i den, grottan ser fuktig ut och har droppande stalaktiter.", 0.05)
    if vägdecision() == 1:  # Om man vänder så kommer man tillbaka till vägvalet
        return
    else:  # Forsätte
        slowtype("Du går ner i grottan", 0.05)
        slowtype("Det är brant och dina knän får jobba hårt", 0.05)
        slowtype("Plöstlsigt halkar du till och ramlar", 0.05)
        slowtype("Du tumlar neråt, det gör ont,", 0.05)
        slowtype("Efter vad som känns som en evighet så stannar du äntligen", 0.05)
        slowtype("Du reser dig upp och kollar dig omkring", 0.05)
        slowtype("Du är i en lång rak grotta du inte kan se slutet på", 0.05)
        time.sleep(1)
        slowtype("I perferin ser du rörelser, du vänder dig snabbt om och ser någonting springa mot dig", 0.05)
        os.system('cls' if os.name == 'nt' else 'clear')
        monsterval = monsterpullar()
        alive = battle(monsterval, playerclass, alive)
        if alive == False:          # Alive ändras i battle func
            return playerclass.alive        # Om du dör så slutar funk köras
    slowtype("Efter du dödat monsteret går du vidare", 0.05)
    time.sleep(1)  # import time
    slowtype("Du hinner bara gå ett par minuter innan du hör något mullra, du vänder dig om och ser massor stenar rulla mot dig", 0.05)
    time.sleep(1)
    slowtype("Du lowkey ser ett samband i stenarna, nummrena 13 98 flashar i din hjärna", 0.05)
    time.sleep(5)  # Låter användaren kolla på nummrerna
    os.system('cls' if os.name == 'nt' else 'clear')
  # Rensar temrinel
    stensvar = input("""vilka var talen?  xx xx 
                -> """)
    time.sleep(2)
    if stensvar == "13 98":
        slowtype("Du fick rätt och på något sätt undivker stenarna", 0.05)
    else:
        slowtype("Du såg inte visionen och blev träffad av en sten", 0.05)
        playerclass.hp -= 10
        slowtype(f"Du har nu {playerclass.hp} hp", 0.05)
        input()

    slowtype(str(playerclass.money), 0.05)
    slowtype("Efter stenraset går du vidare", 0.05)
    slowtype("Efter ett tag kommer du till en korsning", 0.05)
    slowtype("En skylt sitter uppsatt, på den står det", 0.05)
    slowtype("Gå vänster om du vill leva", 0.05)

    if vägescape() == 1:
        slowtype("Du går vänster", 0.05)
        slowtype("Grottan börjar snart ljusna och du känner luften bli varmare", 0.05)
        if vägdecision() == 1:
            slowtype("Du vänder tillbaka", 0.05)
            slowtype("Du kommer tillbaka till korsning och går förbi skylten ", 0.05)
        else:
            slowtype("Du går upp ur grottan", 0.05)
            return
    else:
        slowtype("Du trotsar skyltens råd och går höger", 0.05)

    slowtype("Gången krymper, luften blir kallare. Eko av droppande vatten hörs överallt.", 0.05)
    slowtype("Grottan forsätter att gå ner och snart når vattnet upp till din midja", 0.05)
    slowtype("Det är svängar överallt, det känns som labyrint", 0.05)
    slowtype("Plötsligt hör du ett isande skrik bakom dig,", 0.05)

    afb = input("Vill du, 1 Gå mot ljudet eller 2 gå vidare? -> ")
    if afb == "1":
        slowtype("Du vänder dig om och börjar gå", 0.05)
        slowtype("Allt ser normalt ut, inget konstigt", 0.05)
        slowtype("Kanske inbildade du dig bara", 0.05)
        slowtype("Efter ett tag ser du nåt som glimmar på vägen", 0.05)
        slowtype("En stor guldtand, intryck i en glipa", 0.05)
        slowtype("Den här kan nog vara värd en kosing tänker du", 0.05)
    else:
        slowtype("Du fortsätter gå framåt", 0.05)
        slowtype("Rarariarar!", 0.05)
        slowtype("Någonting drar dig ner under vattnet", 0.05)
        alive = battle(FiskMänniska, playerclass, alive)
        if alive == False:
            return playerclass.alive

    slowtype("Du går vidare fast du är trött", 0.05)
    slowtype("Långsamt börjar grottan bli torrare", 0.05)
    slowtype("Efter en stund märker du att marken blir mjukare, nästan som sand", 0.05)
    slowtype("Det luktar fuktigt och mögel, luften känns tung", 0.05)
    slowtype("Du hör ett svagt ljud av något som rör sig under sanden", 0.05)

    choice = input("Vill du, 1 undersöka ljudet eller 2 fortsätta framåt? ")

    if choice == "1":
        slowtype("Du hukar dig ner och tittar försiktigt", 0.05)
        slowtype("Ett par små ögon som iaktar dig från sanden..", 0.05)
        slowtype("Du drar fram ditt vapen och förbereder dig för strid!", 0.05)
        alive = battle(sandworm, playerclass, alive)
        if alive == False:
            return playerclass.alive
        slowtype("Efter striden andas du ut och fortsätter vidare", 0.05)
    else:
        slowtype("Du väljer att inte störa det mystiska ljudet och fortsätter framåt", 0.05)
        slowtype("Sanden knastrar under dina fötter och gångarna blir smalare", 0.05)
        slowtype("Plötsligt ser du en stor hiss", 0.05)
        slowtype("Den ser gammal ut men den kanska funkar", 0.05)
        hissvar = input("Vill du trycka på hissknappen?")
        if hissvar == "ja":
            pass

    slowtype("Plötsligt öppnar grottan upp sig till en enorm sal", 0.05)
    slowtype("Takets stalaktiter glittrar av fukt, och små floder rinner kors och tvärs", 0.05)
    slowtype("I mitten av salen ser du något som får ditt hjärta att slå snabbare", 0.05)
    slowtype("En gigantisk, glittrande drake sover bland högar av guld och skatter", 0.05)

    choice2 = input(
        "Vill du, 1 smyga förbi draken eller 2 försöka ta lite skatt? ")

    if choice2 == "1":
        slowtype("Du håller andan och smyger längs väggarna", 0.05)
        time.sleep(2)
        slowtype("Draken rör inte en muskel och du kommer fram till andra sidan salen", 0.05)
        slowtype("Du känner dig nöjd men adrenalinet pumpar fortfarande", 0.05)
    else:
        slowtype("Du tar ett steg mot skatten", 0.05)
        slowtype("Draken öppnar ett öga och låter ett öronbedövande vrål", 0.05)
        time.sleep(2)
        # Kalla draken som monster
        monsterval = monsterpullar()
        alive = battle(monsterval, playerclass, alive)
        if alive == False:          # Alive ändras i battle func
            return playerclass.alive
        slowtype("Efter en hård strid lämnar du salen med en bit av skatten", 0.05)
    time.sleep(1)
    slowtype("När du går vidare från salen blir grottan smalare och luften varmare", 0.05)
    time.sleep(2)
    slowtype("Du börjar se ljus som sipprar in från små sprickor ovanför", 0.05)
    time.sleep(2)
    slowtype("Det känns som att du närmar dig grottans slut", 0.05)
    time.sleep(2)
    slowtype("Men plötsligt hör du ett eko av fotsteg bakom dig", 0.05)
    choice3 = input(slowtype(
        "Vill du, 1 vända dig om eller 2 fortsätta framåt snabbt? ", 0.05))
    if choice3 == "1":
        slowtype("Du vänder dig om och ser en grupp skuggfigurer", 0.05)
        time.sleep(2)
        slowtype("De verkar inte se dig än, kanske kan du smyga undan?", 0.05)
        stealth_choice = input(
            "Vill du, 1 smyga undan eller 2 konfrontera dem? ", 0.05)
        if stealth_choice == "1":
            slowtype("Du kryper längs väggarna och lyckas ta dig förbi utan problem", 0.05)
        else:
            slowtype("Du drar fram ditt vapen och striden börjar", 0.05)
            # Slåss mot mystical men
            alive = battle(Skuggriddare, playerclass, alive)
            if alive == False:          # Alive ändras i battle func
                return playerclass.alive
    else:
        slowtype("Du rusar framåt och ignorerar fotstegen bakom dig", 0.05)
        time.sleep(2)
        slowtype("Pulsen dunkar i öronen men du känner ljuset bli starkare för varje steg", 0.05)

    time.sleep(1)
    slowtype("Slutligen når du grottans mynning", 0.05)
    time.sleep(2)
    slowtype("Solens ljus träffar ditt ansikte, och du andas den friska luften", 0.05)
    time.sleep(1)
    slowtype("Grattis, du överlevde Grottvägen! Som belöning får du 50 guld och exp.", 0.05)
    playerclass.amoney(50)
    playerclass.add_exp(50)
    
    playerclass.grott = True
    return alive



def skogsvägen(alive):
    slowtype("Efter ett tag kommer du fram till en mörk skog.", 0.05)
    time.sleep(1)
    slowtype("Du kliver in i den mörka skogen. Ljuset bakom dig försvinner nästan direkt när träden sluter sig över dig. Luften blir kylig och stilla. Något prasslar mellan stammarna, men du kan inte se vad. Skuggorna rör sig, och en obehaglig känsla kryper längs ryggen.", 0.05)
    time.sleep(4)
    if vägdecision() == 1:
        slowtype("Du fegar ut och bestämmer dig för att vandra hem.", 0.05)
        return 
    else:
        slowtype("Du går djupare in i skogen.", 0.05)
        time.sleep(2)
        slowtype("Efter ett tag hör du grenarna prassla bakom dig och du vänder dig snabbt om.", 0.05)
        monsterval = monsterpullar()
        alive = battle(monsterval, playerclass, alive)
        if alive == False: 
            return playerclass.alive         # Alive ändras i battle funktionen
    input("Tryck enter för att fortsätta -> ")
    os.system('cls' if os.name == 'nt' else 'clear')
    
    slowtype("Efter fighten så fortsätter du in i den mörka skogen.", 0.05)
    slowtype("Du går sakta och samtdigt njuter av den lugna och stilla miljön.", 0.05)
    slowtype("Men helt plötsligt så börjar vinden ta sig rejält och skyn går om till svart.", 0.05)
    time.sleep(1)
    slowtype("Det föredetta lugnet har nu gått om till en kraftfull storm och träden vajar rejält.", 0.05)
    slowtype("Bakifrån dig hörs ett högt knak och vänder dig om för att se ett gigantiskt träd falla mot din riktning", 0.05)
    skogsträdfall = int(input("""                            Vill du:
1. Undvika vänster   2. Undvika höger   3. Slå sönder trädet oskadad
                          -> """))
    if skogsträdfall == 1:
        slowtype("Du undvek trädet genom att göra en dramatisk rull åt vänster och kom ut oskaddad.", 0.05)
    elif skogsträdfall == 2:
        slowtype("Du undvek trädet genom att göra en dramatisk rull åt höger och kom ut oskaddad.", 0.05)
    elif skogsträdfall == 3:
        slowtype("Du försökte stoppa trädet med all din kraft, men blir till slut mosad.", 0.05)
        alive = battle(monsterval, playerclass, alive)
        if alive == False:          # Alive ändras i battle func
            return playerclass.alive
    else:
        slowtype("Du svarade inte korrekt och hinner därför inte reagera på det fallande trädet.", 0.05)
        slowtype("Du dog.", 0.05)
        alive = battle(monsterval, playerclass, alive)
        if alive == False:          # Alive ändras i battle func
            return playerclass.alive
    
    input("Tryck enter för att fortsätta -> ")
    os.system('cls' if os.name == 'nt' else 'clear')
    slowtype("Efter katastrofen så fortsätter du djupare in i den mörka skogen medans du vandrar mellan de höga vajande träden, tills du känner att någonting inte riktigt stämmer.",0.05)
    slowtype("Två röda ögon ses blinka mellan träden, och de verkar spana in just dig.",0.05)
    slowtype("På mindre än en sekund springer monstret och hoppar på dig!",0.05)

    monsterval = monsterpullar()
    alive = battle(monsterval, playerclass, alive)
    if alive == False:        # Alive ändras i battle func
        return playerclass.alive
        
    slowtype("Efter ännu en till attack så känner du dig utmattad och fortsätter vandra med hopp om att du snart kommer ut ur denna läskiga skog.",0.05)
    slowtype("Efter ett långt äventyr så ser du ett glimmer från skogens kant och bestämmer dig för att gå denns håll.",0.05)
    slowtype("När du närmrar dig så inser du att det är en liten stuga.",0.05)

    
    while True:
        Stuga_val = int(input("""           Vill du:
            1. Inspektera stugan       2. Strunta i stugan och fortsätta vandra
    -> """))
        try: 
           
            if Stuga_val == 1:
                slowtype("Du bestämmer dig för att ta en liten titt runt stugan.",0.05)
                slowtype("Du går fram till den lilla stugan och tar en kollar in genom fönstret.",0.05)
                slowtype("Stugans insida är i fint skick, nästan som att någon bodde här ute i skogen.", 0.05)
                slowtype("Helt plötsligt hörs ett prassel bakom dig och du vänder dig hastigt om.",0.05)
                input("Tryck enter för att fortsätta ->")
                os.system('cls' if os.name == 'nt' else 'clear')
                slowtype("Framför dig står en kort gammal dam som kollar på dig med nyfikna ögon.",0.05)
                slowtype("Men hallå där! Säger Damen.", 0.05)
                slowtype("H-hej, säger du osäkert tillbaks.",0.05)
                slowtype("Vad gör en ung äventyrare som dig här ute i denna farliga skog? Undrar kvinnan.",0.05)   
                damfråga = int(input("""                           Vad svarar du?
    1. Skulle kunna fråga detsamma.      2. Inget för dig att veta! 
    -> """))
                if damfråga == 1:
                    slowtype("Om du inte redan visste det så bor jag här i stuga som du just snokade runt. Svarade Damen.",0.05)
                    slowtype("Jag hoppas du vet att det inte är särskilt trevligt att snoka runt andras hus. Säger hon besviket.",0.05)
                elif damfråga ==2:
                    slowtype("Förlåt för att jag frågade, menade inte att kränka dig. Svarade Damen.",0.05)
                else:
                    slowtype("Du gav inte ett giltigt svar och svarar därför inte på frågan.",0.05)
                    slowtype("Jahopp, inget svar? Sa damen besviket.",0.05)
                
                slowtype("Kom in i min stuga, denna skog är inte säker under nätterna, dessutom ser det ut som att du behöver vila lite.",0.05)
                while True: 
                    damfråga2 = int(input("""       Vad gör du?
            1. Följer med damen in i stugan.   2. Säger nej och fortsätter att vandra i skogen.
            -> """))
                    try:   
                        if damfråga2 == 1:
                            slowtype("Du följer med damen.",0.05)
                            slowtype("Stugan är full med olika växter och massor av annat från skogen.",0.05)
                            slowtype("Varför bor du här ute? Frågar du damen.",0.05)
                            slowtype("Jag har alltid bott i dessa skogar. De är hela min barndom och jag kan inte få mig själv att flytta där ifrån. Det är också lungt dagarna om och jag slipper oftast personer som dig. Svarar damen", 0.05)
                            slowtype("Jahopp då. Får du ur dig.",0.05)
                            slowtype("Jag gjorde min favoritgryta till middag, vill du ha? Frågar damen.",0.05)
                            time.sleep(1)
                            
                            damfråga3 = int(input("""                   Vad gör du?
            1. Du tar villigt emot maten        2. Du avstår
            -> """))
                            if damfråga3 ==1:
                                slowtype("Gärna! Säger du och tar emot en varm skål av grytan.",0.05)
                                slowtype("Vad är det för gryta? Frågar du.",0.05)
                                slowtype("Det är bara ett simpelt recept på en kaningryta jag brukade äta när jag var liten. Svarade damen.",0.05)
                                slowtype("Du villigt tar ett stort slurp ur grytan.",0.05)
                                slowtype("WOW! Nästan skriker du ut.",0.05)
                                slowtype("Vad är det pojk? Undrar damen.",0.05)
                                slowtype("Detta är den bästa grytan jag någonsin ätit i hela mitt liv! Säger du till damen.",0.05)
                                slowtype("Jag känner mig typ starkare!!! Skriker du glatt.",0.05)
                                slowtype("Men vad roligt att du gil... försöker damen säga då hon blev avbruten av ett högt vrål.",0.05)
                                slowtype("Det är nog dags att gå och lägga oss säger damen nervöst.",0.05)
                                input("Tryck enter för att fortsätta ->")
                                os.system('cls' if os.name == 'nt' else 'clear')
                                slowtype("Nästa dag vaknar du av att solen strålar i ditt ansikte",0.05)
                                slowtype("Du går upp och hälsar på damen som redan står och lagar frukost.",0.05)
                                slowtype("Det är nog dags för mig att gå min väg, men tack för att jag fick stanna här i natt. Säger du till damen.",0.05)
                                slowtype("Innan du går! säger damen snabbt.",0.05)
                                slowtype("Så vill jag ge dig en sak... fortsätter damen.",0.05)
                                slowtype("Min man var en äventyrare innan han gick bort och han hade en styrkedryck som nu inte används.",0.05)
                                slowtype("Jag tycker att du borde ta den om det kan hjälpa dig på något sätt.",0.05)
                                slowtype("Du tar villigt emot drycken.",0.05)
                                playerclass.add_item(Item_list1[3])
                                slowtype("Tack. Säger du.",0.05)
                                slowtype("Detta kan vara väldigt hjälpsamt.",0.05)
                                slowtype("Du säger adjö till damen och går din väg.",0.05)

                    
                            elif damfråga3 ==2:
                                slowtype("Jag kan avstå. Säger du.",0.05)
                                slowtype("Skyll dig själv, mumlar damen.",0.05)
                                slowtype("Du går istället och lägger dig efter en lång dag.",0.05)
                                slowtype("Du går upp tidigt nästa morgon och drar iväg utan att säga adjö.",0.05)
                            else:
                                slowtype("Eftersom att du svarade tror jag att du inte vill ha. Antar damen",0.05)
                                slowtype("Precis. Säger du ohyfsat.",0.05)
                                slowtype("Du går sedan och lägger dig för att sova efter den långa dagen.",0.05)
                                slowtype("Du vaknar tidigt nästa dag och går din väg utan att kolla tillbaka",0.05)
                            break
                        
                        elif damfråga2 ==2:
                            slowtype("Nej, svarar du och fortsätter gå utan att kolla tillbaka.",0.05)
                            break
                        else:
                            slowtype("Du gav inte ett giltigt svar, svara om.", 0.05)
                    except ValueError:
                        slowtype("Du gav inte ett giltigt svar, svara om.", 0.05)
                break
            elif Stuga_val == 2:
                slowtype("Du bestämmer dig för att struna i stugan och fortsätter att vandra genom den täta skogen.",0.05)
                break
            else:
                slowtype("Du gav inte ett giltigt svar, svara om.", 0.05)
        except ValueError:
            slowtype("Du gav inget ett giltigt svar, svara om.", 0.05)
    
    slowtype("Efter ännu ett tag av vandrande känner du att vinden blir starkare och starkare och framför dig ses en öppning mellan träden.",0.05)
        
    slowtype("Du har äntligen kommit ut ur den täta skogen och du kan nu fortsätta ditt äventyr starkare än någonsin.",0.05)
    slowtype("Grattis, du överlevde Skogsvägen! Som belöning får du 50 guld och exp.",0.05)
    playerclass.amoney(50)
    playerclass.add_exp(50)
    playerclass.skog = True
    return alive


def abanondedcity(alive):
    slowtype("Efter ett tag kommer du fram till vad du tror är en helt vanlig stad.", 0.05)
    slowtype("Men du märker att någonting är fel.", 0.05)
    slowtype("Fönstren är krossade, det växer gräs ur asfalten och det är helt tyst förutom vindens brus.", 0.05)
    slowtype("Det var nästan som att staden är övergiven.", 0.05)
    input("Tryck enter för att fortsätta ->")
    os.system('cls' if os.name == 'nt' else 'clear')
    slowtype("När du funderar på vart du ska ta vägen så ser du en hög skyskrapa som bara kallar ditt namn och du bestämmer dig för att gå dit.", 0.05)
    slowtype("Du tar dig genom de övergivna gatorna och efter en lång vandring så kommer du äntligen fram till en otroligt hög byggnad.", 0.05)
    slowtype("Du går in genom porten på den föredetta lyxiga byggnaden i hopp om att hitta resureser.", 0.05)
    slowtype("Du kollar runt i den lyxiga entrén som ser oväntande fräsh ut.", 0.05)
    slowtype("Allt verkar alldels för avkopplande tills...", 0.05)

    monsterval = monsterpullar()
    alive = battle(monsterval, playerclass, alive)
    if alive == False:        # Alive ändras i battle func
        playerclass.alive 
    if vägdecision() ==1:
        slowtype("Du bestämmer dig för att vända tillbaks.", 0.05)
        return
    slowtype("Efter fighten så fortsätter du att gå runt i skyskrapan tills du hittar ett par trappor.", 0.05)
    time.sleep(3)
    while True:
        trapporupellerner = int(input("""Vill du:
        1. Gå upp för trappan     2. Gå ner för trappan
        -> """))
        try:
            if trapporupellerner == 1:
                time.sleep(1)
                slowtype("Du bestämde dig för att gå upp för trappan.", 0.05)
                slowtype("Denna våning verkar vara ett gammalt spelrum med otroligt många olika maskiner och kortspel.", 0.05)
                slowtype("Du kollar på alla olika slotmachines och märker att en av dem skapar ett konstigt pling ljud.", 0.05)
                slowtype("Du går fram till maskinen och bestämmer dig för att slå lite på den i hopp om att den kanske fortfarande fungerar.", 0.05)
                slowtype("Helt plötsligt så börjar den spela ett högt ljud och en lucka öppnar sig.", 0.05)
                slowtype("Ut kom runt 40 guld, det värkar vara din lyckodag!", 0.05)
                slowtype("Du plockar upp mynten och går din väg.", 0.05)
                playerclass.amoney(40)
                break
                        
            elif trapporupellerner == 2:
                slowtype("Du bestämde dig för att gå ner för trappan.", 0.05)
                slowtype("Det verkar som att du gått in på föredetta garagevåningen.", 0.05)
                slowtype("Det finns lyxiga bilar på din vänster och höger men den som faktiskt väcker ditt intresse är en gammal mint condition Volkswagen Golf.", 0.05)
                slowtype("Du går fram till den vackra bilen och bestämmer dig för att se om den fungerar så du bryter dig in via fönsterrutan.", 0.05)
                slowtype("Solklart glömmer du ju bort att det behövs nycklar så du går ut ur bilen i misstro fast någonting glimmade till i baksätet och bestämmer dig för att tar ännu en tit in i bilen.", 0.05)
                slowtype("Det visade sig vara ett golfsett.", 0.05)
                while True:
                        time.sleep(2)
                        Tauppbackseatweapon = int(input(f"""Vill du plocka upp en golfklubba och byta ut den mot ditt nuvarande vapnet {Weapon.name}?
                        1. Ja     2. Nej"""))
                        try:
                            if Tauppbackseatweapon == 1:
                                slowtype(f"Du bytte ut {Weapon.name} mot en golfklubba", 0.05)
                                Vapen = Weapon("Golfklubba")
                                playerclass.weapon = Vapen
                                break
                            elif Tauppbackseatweapon == 2:
                                slowtype(f"Du behöll {Weapon.name} som ditt vapen.", 0.05)
                                break
                            else:
                                slowtype("Du gav inte ett giltigt svar, svara om.", 0.05)
                        except:
                            slowtype("Du gav inte ett giltigt svar, svara om.", 0.05)
                            
                slowtype("Efteråt återvände du tillbaks till stadens gator.", 0.05)
                break
                        
            else:
                slowtype("Du gav inte ett giltigt svar, svara om.", 0.05)
        except:
            slowtype("Du gav inte ett giltigt svar, svara om.", 0.05)
    time.sleep(2)
    slowtype("Efter ett långt äventyr så blev du klar med att undersöka skyskrapan och du kan äntligen fortsätta din väg.", 0.05)
    input("Tryck enter för att fortsätta ->")
    os.system('cls' if os.name == 'nt' else 'clear')
    slowtype("I det trista väderet tar du dig över de sprukna gatorna.", 0.05)
    slowtype("Det är knäpptyst i staden förutom vindens sus.", 0.05)
    slowtype("Men plötsligt så hörs ett skräckinjagande vrål mitt i det lugna.", 0.05)
    while True:
        museumfortsättaellerundersöka = int(input("""Vill du undersöka vrålet eller vill du fortsätta ut ur staden?
        1. Undersöka     2. Fortsätta
                -> """))
        try:
            if museumfortsättaellerundersöka == 1:
                os.system('cls' if os.name == 'nt' else 'clear')
                slowtype("Du bestämmer dig för att undersöka vrålet och ändrar din gåriktning.", 0.05)
                slowtype("Vrålet forsätter och blir högre och högre för varje steg du tar.", 0.05)
                slowtype("Du börjar närma dig vrålets källa och kan snart se var detta skrämmande ljudet kommer ifrån.", 0.05)
                slowtype("Framför dig syns en otroligt stor och urgammal byggnad, det ser ut att vara ett sorts museum.", 0.05)
                time.sleep(1)
                if vägdecision() ==1:
                    slowtype("Du bestämmer dig för att vända tillbaks.", 0.05)
                    return
                time.sleep(0.5)
                slowtype("Vrålet har ännu än inte slutat och du bestämmer dig för att går in och äntligen få reda på vad som skapar oljudet.", 0.05)
                slowtype("Du öppnar lätt dörren och tar en liten titt in i museets entré.", 0.05)
                slowtype("Det chockande rent eftersom att det troligen inte varit någon här på flera decennier.", 0.05)
                slowtype("Du går in genom dörren och sekunden som porten stängs så slutar plötsligt vrålandet och det blir helt knäpptyst.", 0.05)
                input("Tryck enter för att fortsätta ->")
                os.system('cls' if os.name == 'nt' else 'clear')
                slowtype("Efter lite inspektion visar det sig att museumet verkar vara ett gammalt naturhistorisk museum med massor med utrotade varelser, så som dinosaurier.", 0.05)
                slowtype("Du går runt och kollar på alla uppvisade dinosaurieskelett en efter en, men plötsligt så märker du att någonting inte riktigt stämmer.", 0.05)
                slowtype("En av uppvisningsplattformarna är tomma.",0.05)
                slowtype("Medans då står och klurar på varför en av uppvisningsplattformarna är tommma så känner du ett kyligt andetag gå nerför din nacke.",0.05)
                slowtype("Med hjälp av dina snabba reflexer så hoppar du precis undan en dödlig attack som slår i golvet med ett högt klang.", 0.05)
                alive = battle(SkelettRaptor, playerclass, alive)
                if alive == False:
                    return playerclass.alive
                os.system('cls' if os.name == 'nt' else 'clear')
                slowtype("Efter den farliga fighten mot Skelett Raptorn bestämmer du dig för att äntligen lämna denna övergivna stad och museum bakom dig och fortsätta med ditt huvudäventyr.",0.05)
                slowtype("Efter ännu en lång tur kommer du till slut fram till där du lämnade för att undersöka vrålet, fast nu är det tyst och fridfullt.",0.05)
                break
            elif museumfortsättaellerundersöka ==2:
                os.system('cls' if os.name == 'nt' else 'clear')
                time.sleep(1)
                slowtype("Du bestämmer dig för att strunta i vrålet och fortsätter istället åt samma håll som du först tänkte gå.",0.05)
                break
            else:
                slowtype("Du gav inte ett giltigt svar, svara om.", 0.05)
        except:
            slowtype("Du gav inte ett giltigt svar, svara om.", 0.05)
    
    slowtype("Efter denna otroligt långa och spännande turen genom staden så kan du äntligen fortsätta frammåt och besegra alla som kommer i din väg.",0.05)
    slowtype("Grattis, du överlevde Stadsvägen! Som belöning får du 50 guld och exp.", 0.05)
    playerclass.amoney(50)
    playerclass.add_exp(50)
    playerclass.city = True
    return alive

def biblloktekt():
    while True:
            slowtype("""        Var vill du gå?
                        1. Monster boks hyllan        2. Natur boks hyllan      3. Den vise mannen
                                                4. Gå tillbaka
                        """, 0.05)
            bok_val = int(input())
            os.system('cls' if os.name == 'nt' else 'clear')
            

            if bok_val == 1:
                        slowtype("""    Vilket monster skulle du vilja läsa om?
                                        1. Skeleton     2. Goblin       3. Goon        4. Bandit
                                                        5. Troll        6. Varulv 
                                                                7. Lämna
                        """, 0.05)
                        monster_val = int(input())
                        os.system('cls' if os.name == 'nt' else 'clear')
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
                                slowtype("Skriv ett av de 7 nummer", 0.05)
                        except:
                            slowtype("Skriv om skriv rätt", 0.05)

            elif bok_val == 2:
                slowtype("""       Vilken natur vill du läsa om?
                                    1. Grottvägen       2. Skogsvägen       3. Abanonded City
                                                            4. Lämna
                            """, 0.05)
                natur_val = int(input())
                os.system('cls' if os.name == 'nt' else 'clear')
                try:
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
                        slowtype("Skriv ett av de 4 nummer"), 0.05
                except:
                    slowtype("Skriv om och skriv rätt", 0.05)
                    
            elif bok_val == 3:
                    if playerclass.hybris == True:                         #chekar om playern har hybris
                        slowtype("The old man is not here anymore, wonder why...", 0.05)
                    else:
                            slowtype("Hello there young man", 0.15) 
                            slowtype("I'am the wise man of the village", 0.05)
                            gusval = input("Do you want to hear about my life? Ja / Nej")
                            gusval = gusval.upper()
                            if gusval == "NEJ":
                                slowtype("All these young men", 0.05)
                                time.sleep(0.5)
                                slowtype("How many have walked past me",0.05)
                                time.sleep(0.5)
                                slowtype("To never return ",0.05)
                                time.sleep(0.5)
                                slowtype("I have seen them all but not even Leonard Euler could have counted them ",0.05)
                                time.sleep(0.5)
                                slowtype("Goodbye", 0.05)
                                playerclass.hybris = True     #Sätter playern som hybris
                                
                            else:
                                slowtype("In my youth i was a adeventurer", 0.1)
                                time.sleep(0.5)
                                slowtype("I walked through caves that were so dark", 0.1)
                                time.sleep(0.5)
                                slowtype("Even god didn't know what lived down there", 0.1)
                                time.sleep(0.5)
                                slowtype("I walked in forests with tress so tall", 0.1)
                                time.sleep(0.5)
                                slowtype("Even the birds didnt know were they ended", 0.1)
                                time.sleep(0.5)
                                slowtype("And i walked through cities that were soo haunted", 0.1)
                                time.sleep(0.5)
                                slowtype("Even the devil had stoped counting the lost souls", 0.1)
                                time.sleep(0.5)
                                slowtype("After all my experinces abroad i returned home with fainted heart", 0.15)
                                time.sleep(0.5)
                                slowtype("I settled down and became the old man you see before you", 0.1)
                                time.sleep(2)
                                slowtype("But now on the sunset of my life", 0.12)
                                time.sleep(0.5)
                                slowtype("I wished i walked out there one more time", 0.05)
                                time.sleep(2)
                                slowtype("Becuase there is still something out there", 0.05)
                                time.sleep(0.5)
                                slowtype("A creature i only felt the aura from", 0.05)
                                time.sleep(0.5)
                                slowtype("Only when that king of darkness is erased can the world's darkness disappaear", 0.05)
                                time.sleep(0.5)
                                slowtype("Now son, i wish that you get out there deafeat him",0.05)
                                time.sleep(2)
                                slowtype("Only then can i die happy", 0.05)
                    break
                        
                    
            elif bok_val == 4: 
                        break
            else:
                        slowtype("Skriv ett av de 4 nummer", 0.05)
    return playerclass.hybris       #Skickar tillbaka om playern har hybris eller inte

#Om du vill prova något lägg till det här!!!



def main(alive):
    while alive == True:
        time.sleep(1)
        slowtype(f"""
                    Välkommen till Sweelept
        1. Äventyr       2. Marknaden       3. Bibloteket
    
                4. Inventory     5. Casino
            
                        6. Save game  
            """, 0.01)
        Platsval = input("Vad vill du välja? ")
        if Platsval == "1":
            os.system('cls' if os.name == 'nt' else 'clear')
            slowtype("Du har valt att äventyra!", 0.1)
            slowtype("Du traskar ut ur staden", 0.1)

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
                 slowtype("error i main", 0.05)
            if alive == False:
                slowtype("DU är död", 0.05)

        elif Platsval == "2":
            os.system('cls' if os.name == 'nt' else 'clear')
            slowtype("Du har valt att gå till marknaden", 0.05)
            Marknaden()
        elif Platsval == "3":
            os.system('cls' if os.name == 'nt' else 'clear')
            slowtype("Du har valt att gå till biblloktekt", 0.05)
            playerclass.hybris = biblloktekt()   #Sparar om playern har hybris eller inte
            

        elif Platsval == "4":
            os.system('cls' if os.name == 'nt' else 'clear')
            playerclass.show_inventory()
            playerclass.show_weapon()
            slowtype("Vill du konsumera nåt i dtt inventory?  Ja eller Nej",0.05)
            invval = input()
            invval = invval.upper()
            if invval == "JA":
                if len(playerclass.inventory) > 0:
                    slowtype("Vad vill du ha använda för item? Koperia namnet från item listan",0.05)
                    cons = input()
                    playerclass.use_item(cons)
                    continue
            elif invval == "NEJ":
                continue
            else:
                continue
            
           
            # Stats allocation och stat check
        elif Platsval == "5":
            os.system('cls' if os.name == 'nt' else 'clear')
            casion()
        elif Platsval == "6":
            save_player(playerclass)   
            slowtype("Sparningen lyckades",0.1)
        else:
            pass


main(alive)
