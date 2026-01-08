import pickle       #Alternaitv till json som slipper vissa data typ konvertingar 

def save_player(Characterclass, filename="Characterclass.pkl"): #Tar in Characterclass som man i main skriver som playerclass. och tar in filen  charchter class.pkl
    with open(filename, "wb") as f:    #with är en genväg som stänger filen efter smooth ahh,   wb är write bianry skriver över gammalt i binärt, as f alltså filen
        pickle.dump(Characterclass, f)             # f är filen basically, pickle dumpar charctherclass data i f

def load_player(filename="Characterclass.pkl"):
    with open(filename, "rb") as f:    # read bianry 
        return pickle.load(f)         #laddar up från filen ( f )
