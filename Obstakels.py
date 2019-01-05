import math
import time

snelheid = raw_input ("Hoe snel gaat de auto?: ")
afstand_obstakel = raw_input("Hoever is het obstakel van de auto af?(Alleen getal!): ")
remmen = 0

snelheid_remmen = snelheid / afstand_obstakel

if snelheid >= 100 and snelheid < 170:
  if float(afstand_obstakel) <= 15 and float(afstand_obstakel) > 14:
    remmen = float(remmen) + 1.3
  elif float(afstand_obstakel) <= 14 and float(afstand_obstakel) > 13:
    remmen = float(remmen) + 1.3
  elif float(afstand_obstakel) <= 13 and float(afstand_obstakel) > 12:
    remmen = float(remmen) + 1.3 
  elif float(afstand_obstakel) <= 12 and float(afstand_obstakel) > 11:
    remmen = float(remmen) + 1.3
  elif float(afstand_obstakel) <= 11 and float(afstand_obstakel) > 10:
    remmen = float(remmen) + 1.3
  elif float(afstand_obstakel) <= 10 and float(afstand_obstakel) > 9:
    remmen = float(remmen) + 1.3
  elif float(afstand_obstakel) <= 9 and float(afstand_obstakel) > 8:
    remmen = float(remmen) + 1.3
  elif float(afstand_obstakel) <= 8 and float(afstand_obstakel) > 7:
    remmen = float(remmen) + 1.3
  elif float(afstand_obstakel) <= 7 and float(afstand_obstakel) > 6:
    remmen = float(remmen) + 1.3
  elif float(afstand_obstakel) <= 6 and float(afstand_obstakel) > 5:
    remmen = float(remmen) + 1.3
  elif float(afstand_obstakel) <= 5 and float(afstand_obstakel) > 4:
    remmen = float(remmen) + 1.3
  elif float(afstand_obstakel) <= 4 and float(afstand_obstakel) > 3:
    remmen = float(remmen) + 1.3
  elif float(afstand_obstakel) <= 3 and float(afstand_obstakel) > 2:
    remmen = float(remmen) + 1.3
  elif float(afstand_obstakel) <= 2 and float(afstand_obstakel) > 1:
    remmen = float(remmen) + 1.3
  elif float(afstand_obstakel) <= 1 and float(afstand_obstakel) > 0:
    remmen = float(remmen) + 1.3
  else:
    print("Gas blijven geven")
elif snelheid >= 0 and snelheid < 100:
  if float(afstand_obstakel) <= 15 and float(afstand_obstakel) > 14:
    remmen = float(remmen) + 1.3
  elif float(afstand_obstakel) <= 14 and float(afstand_obstakel) > 13:
    remmen = float(remmen) + 1.3
  elif float(afstand_obstakel) <= 13 and float(afstand_obstakel) > 12:
    remmen = float(remmen) + 1.3 
  elif float(afstand_obstakel) <= 12 and float(afstand_obstakel) > 11:
    remmen = float(remmen) + 1.3
  elif float(afstand_obstakel) <= 11 and float(afstand_obstakel) > 10:
    remmen = float(remmen) + 1.3
  elif float(afstand_obstakel) <= 10 and float(afstand_obstakel) > 9:
    remmen = float(remmen) + 1.3
  elif float(afstand_obstakel) <= 9 and float(afstand_obstakel) > 8:
    remmen = float(remmen) + 1.3
  elif float(afstand_obstakel) <= 8 and float(afstand_obstakel) > 7:
    remmen = float(remmen) + 1.3
  elif float(afstand_obstakel) <= 7 and float(afstand_obstakel) > 6:
    remmen = float(remmen) + 1.3
  elif float(afstand_obstakel) <= 6 and float(afstand_obstakel) > 5:
    remmen = float(remmen) + 1.3
  elif float(afstand_obstakel) <= 5 and float(afstand_obstakel) > 4:
    remmen = float(remmen) + 1.3
  elif float(afstand_obstakel) <= 4 and float(afstand_obstakel) > 3:
    remmen = float(remmen) + 1.3
  elif float(afstand_obstakel) <= 3 and float(afstand_obstakel) > 2:
    remmen = float(remmen) + 1.3
  elif float(afstand_obstakel) <= 2 and float(afstand_obstakel) > 1:
    remmen = float(remmen) + 1.3
  elif float(afstand_obstakel) <= 1 and float(afstand_obstakel) > 0:
    remmen = float(remmen) + 1.3 
else:
  print("Auto gaat zoiezo botsen") 


snelheidmpers = float(snelheid) / 3.6
remafstand = float(snelheidmpers) * float(snelheidmpers) / (2 * 8)

if remafstand > afstand_obstakel:
  print("Auto gaat zoiezo botsen") 

snelheid_remmen = float(snelheid) / float(remmen)

if float(snelheid) == 0:
  print("Auto staat stil!")
else:
  print(float(snelheid_remmen))


snelheid_2 = snelheid_remmen / 3.6

print(snelheid_2)


time.sleep(1)

if float(afstand_obstakel) <= 5 and float(afstand_obstakel) > 4:
  remmen = float(remmen) + 1.2
elif float(afstand_obstakel) <= 4 and float(afstand_obstakel) > 3:
  remmen = float(remmen) + 2.4
elif float(afstand_obstakel) <= 3 and float(afstand_obstakel) > 2:
  remmen = float(remmen) + 4.8
elif float(afstand_obstakel) <= 2 and float(afstand_obstakel) > 1:
  remmen = float(remmen) + 9.6
elif float(afstand_obstakel) <= 1 and float(afstand_obstakel) > 0:
  remmen = float(remmen) + 19.2
else:
  print("Gas blijven geven")
  
snelheid_remmen = float(snelheid) / float(remmen)

if float(snelheid) == 0:
  print("Auto staat stil!")
else:
  print(float(snelheid_remmen))   
