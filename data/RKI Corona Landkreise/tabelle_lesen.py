#Spaltennamen:
IdBundesland = 0
Bundesland = 1
Landkreis = 2
Altersgruppe = 3
Geschlecht = 4
AnzahlFall = 5
AnzahlTodesfall = 6
ObjectId = 7
Meldedatum = 8
LandkreisID = 9


summe = 0
with open("RKI_COVID19.csv") as f:
    print(next(f))
    for line in f:
        spalten = line.split(",")
        summe+= int(spalten[AnzahlFall])
print("Summe der Infizierten:", summe)
