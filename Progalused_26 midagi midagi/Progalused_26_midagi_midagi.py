print ("Tere tulemast!")
print ('Tere tulemast!')


print ("Ma õpi",1,". kursusel") #print väljastab info ekraanile
print ("aasta on", 2026)

kursus=1 #int
aasta=2026 #int

print ("Ma õpin,",kursus,". kursusel") #print väljaastab info ekraanile
print ("Aasta on",aasta)

print ("Aasta on",aasta+1, "olen juba", kursus+1," kursusel")

print ("2026", "10", "01", sep="-") #sep"-" määrab, mis eraldab väljastatavaid väärtusi
print ("Sama ", end="") #end="\n" määrab, mis pannakse lõppu, vaikimisi on see reavahetus
print ("rida")

print ("Larp")

# #Sisestamine
# nimi=input("sisesta oma nimi: ") #input on funktsioon, mis võimaldab kasutajal sisestada väärtust
# print("Tere", nimi, "!") #prnt väljastab info ekraanile

# #Teised andmetüübid
# a = input("Esimene arv: ") #str 19->"19"
# b = input ("Teine arv: ") #str
# print(a + b)

# #Teised andmetüübid
# a = input("Esimene arv: ") #int("19")->19, float 19.0->19.0
# b = input ("Teine arv: ")
# print(a + b)

#Põhioperatsioonid
# print ("Liitmine: ")
# a = float(input("Esimene arv: "))
# b = float(input("Teine arv: "))
# print(a,"+",b,"=",a + b)

# print ("Lahutamine: ")
# a = float(input("Esimene arv: "))
# b = float(input("Teine arv: "))
# print(a,"-",b,"=",a - b)

# print ("Korrutamine: ")
# a = float(input("Esimene arv: "))
# b = float(input("Teine arv: "))
# print(a,"*",b,"=",a * b)

#Tõeväärtused
# p = True #5 >3
# q = False #2 >
# print(not p, p and q, p or q)
# print(5 > 3 and 2 > 4) #->False
# print(5 > 3 or 2 > 4) #->True

#Formatimine
nimi="Mari"
puntid=87
print(f"{nimi} sai {punktid} punkt. ")

hind = 19.9
kogus = 3
print(f"Kokku: {hind*kogus:.2f} eurot") #ümardab kahe komakohani

#Matemaatilised funktsioonid
import math

print("Pii väärtus:", math.pi) # Pii väärtus
print("√16 =", math.sqrt(16)) # Ruutelement
print("sin(π/2) =", math.sin(math.pi / 2)) # Sinus
print("sin(30°) =", round(math.sin(math.radians(30)), 2)) #Sinus
print("5! =", math.factorial(5)) # Faktoriaal 1*2*3*4*5=120

